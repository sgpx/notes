#!/usr/bin/env python3
import c
from langchain import hub
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
import requests as r
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from langchain_community.document_loaders.chromium import AsyncChromiumLoader
from langchain_community.document_transformers.beautiful_soup_transformer import (
    BeautifulSoupTransformer,
)
from sys import argv
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


llm = ChatOpenAI(model_name="gpt-4-vision-preview")

wanted_tags = [
    "p",
    "li",
    "div",
    "a",
    "td",
    "span",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
]


def wikisearch(searchTerm: str) -> list:
    """
    searches wikipedia and returns a multiline string containing all the links found for the searchTerm given

    args:
        searchTerm - type: str, the search string
    """
    print(searchTerm)
    searchTerm = quote_plus(searchTerm)

    target_selector = "li.mw-search-result"
    session = r.Session()
    wikilink = f"https://en.wikipedia.org/w/index.php?search={searchTerm}&title=Special:Search&profile=advanced&fulltext=1&ns0=1&searchToken=4tay5n1v9mxnayjznc5d060d6"
    print(wikilink)
    resp = session.get(wikilink)
    rv = []
    if resp.status_code == 200:
        html = resp.text
        page = BeautifulSoup(html, features="html.parser")
        rset = page.select(selector=target_selector)
        for i in rset:
            elem = i.select_one("a")
            link = elem.get("href")
            if link:
                rv.append(f"https://en.wikipedia.org/{link}")  # {"link": f})
    print(rv)
    return "\n".join(rv)


def direct_scraper(link):
    """
    takes a web link as input and returns a string with its contents after opening the page with the requests module in python

    args:
        link - the link for the required page
    """
    session = r.Session()
    resp = session.get(link)
    soup = BeautifulSoup(resp.text, "html.parser")
    result = ""
    for text in soup.stripped_strings:
        tmp = result + " " + text
        tmp = re.sub(string=tmp, repl=" ", pattern=r" +", flags=re.IGNORECASE)
        token_count = len(result.split(" "))
        # print("token_count", token_count)
        if token_count < 5000:
            result = tmp
        else:
            return result
    return result


def chrome_link_loader(link: str) -> str:
    """
    takes a web link as input and returns a string with its contents as output after opening the page using headless chromium

    args:
        link - the link to the wikipedia page wanted
    """
    loader = AsyncChromiumLoader([link])
    html = loader.load()
    bs_transformer = BeautifulSoupTransformer()
    docs_transformed = bs_transformer.transform_documents(
        html,
        tags_to_extract=wanted_tags,
    )
    return docs_transformed[0].page_content[0:1000]


def get_google_search_results(searchTerm):
    """
    takes a search term string as input and returns the output of the google search result for it

    args:
        searchTerm - type: str, the search term string
    """
    ff = webdriver.Firefox(keep_alive=False)
    ff.get("https://www.google.com/")
    textarea = ff.find_element(value="textarea", by=By.CSS_SELECTOR)
    textarea.send_keys(searchTerm)
    textarea.send_keys(Keys.ENTER)
    sleep(2)
    rv = ""
    elem = ff.find_elements(value="span", by=By.TAG_NAME)
    for i in elem:
        rv += i.text + " "
    ff.close()
    return rv[0:1000]


def google_search_link_getter(searchTerm) -> str:
    """
    takes a search term as input and returns the google search URL for that as output

    args:
        searchTerm - type: str
    """
    searchTerm = quote_plus(searchTerm)
    return f"https://www.google.com/search?q={searchTerm}"


def run_my_agent(template):
    my_tools = [
        Tool(
            name="wikisearch",
            func=wikisearch,
            description="searches wikipedia and returns a multiline string containing all the links found for the searchTerm given",
        ),
        Tool(
            name="get_google_search_results",
            func=get_google_search_results,
            description="takes a search term string as input and returns the output of the google search result for it",
        ),
        # Tool(
        #     name="google_search_link_getter",
        #     func=google_search_link_getter,
        #     description="takes a search term as input and returns the google search URL for that as output",
        # ),
        # Tool(
        #     name="chrome_link_loader",
        #     func=chrome_link_loader,
        #     description="takes a web link as input and returns a string with its contents as output after opening the page in chrome using playwright",
        # ),
        # Tool(
        #     name="direct_scraper",
        #     func=direct_scraper,
        #     description="takes a web link as input and returns a string with its contents after opening the page with the requests module in python",
        # ),
    ]
    react_prompt = hub.pull("hwchase17/react")
    my_agent = create_react_agent(llm=llm, tools=my_tools, prompt=react_prompt)
    aexec = AgentExecutor(agent=my_agent, tools=my_tools, verbose=True)
    prompt_template = PromptTemplate(
        input_variables=["entity"],
        template=template,
    )
    result = aexec.invoke(input={"input": prompt_template})
    print(result)


if __name__ == "__main__":
    print("testing..")
    run_my_agent(argv[-1])
