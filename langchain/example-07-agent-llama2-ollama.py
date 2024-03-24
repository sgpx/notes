#!/usr/bin/env python3
import c
from langchain import hub
from langchain.chains import LLMChain
from langchain_community.llms import Ollama
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
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import re

open("output.txt","w").write("output start here\n\n")
llm = Ollama(model="llama2")
summary_model_token_limit = 100000
ff = webdriver.Firefox(keep_alive=False)
ff.install_addon("./ublock.xpi", temporary=False)
summary_template = "summarize this text:\n`{mydata}` put all the valid URL links found in the bottom of the text. remove any invalid links or URLs. remove any duplicate URLs or URLs that might be corrupted or contain special characters. if the text is garbage, do not return anything"

summary_prompt_template = PromptTemplate(
    input_variables=["mydata"], template=summary_template
)
summary_llm_chain = LLMChain(
    llm=Ollama(model="llama2"), prompt=summary_prompt_template
)

summarize = lambda x: summary_llm_chain.invoke({"mydata": x}).get("text") or ""


def count_llm_tokens(text):
    return len([i for i in text.split(" ") if i])


def split_long_text(mytext):
    words = mytext.split(" ")
    split_lines = []
    acc = []
    for i in words:
        acc.append(i)
        if len(acc) == 3000:
            print(len(acc))
            split_lines.append(" ".join(acc))
            acc = []
    if acc:
        split_lines.append(" ".join(acc))
    return split_lines


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
    ff.get("https://www.google.com/")
    textarea = ff.find_element(value="textarea", by=By.CSS_SELECTOR)
    textarea.send_keys(searchTerm)
    textarea.send_keys(Keys.ENTER)
    sleep(2)
    raw_text = ""
    for ctag in ["span", "a"]:
        elem = ff.find_elements(value=ctag, by=By.TAG_NAME)
        for i in elem:
            if ctag == "a":
                link = i.get_attribute("href")
                if link:
                    raw_text += link + "\n"
            raw_text += i.text

    # ff.close()
    token_count = count_llm_tokens(raw_text)
    text_list = [raw_text]
    print("before split the token_count is", token_count)
    if token_count > summary_model_token_limit:
        print("splitting text")
        text_list = split_long_text(raw_text)

    print("summarizing...")
    rv2 = ""
    for i in text_list:
        res2 = summarize(i)
        rv2 += res2 + "\n"
    return rv2[0:1000]


def visit_web_link(link):
    """
    takes a web URL as input and returns all the text contained on the page at that URL. link must be in a valid HTTP URL format

    args:
        link - type: str, the URL for the page to be visited
    """
    crap_domains = ["educba.com", "investors.com"]
    if any([crap in link.lower() for crap in crap_domains]):
        return "INVALID LINK"
    ff.get(link)
    raw_text = ""
    for ctag in wanted_tags:
        print("looking for tag", ctag)
        elem = ff.find_elements(value=ctag, by=By.TAG_NAME)
        for i in elem:
            try:
                raw_text += i.text
            except:
                pass
    print("splitting..")
    split_lines = split_long_text(raw_text)
    print("split ok")
    rv = ""
    llx = len(split_lines)
    for ctr, i in enumerate(split_lines):
        print(f"summarizing line {ctr+1} of {llx}")
        rv += summarize(i)
        sleep(2)
    rv = summarize(rv)
    print("final summary OK")
    return rv


def google_search_link_getter(searchTerm) -> str:
    """
    takes a search term as input and returns the google search URL for that as output

    args:
        searchTerm - type: str
    """
    searchTerm = quote_plus(searchTerm)
    return f"https://www.google.com/search?q={searchTerm}"

def save_text(text):
    """
    saves text to hard disk

    args:
        text - str, text to be saved
    """
    open("output.txt","a").write(text)

def run_my_agent(my_prompt):
    my_tools = [
        # Tool(
        #     name="wikisearch",
        #     func=wikisearch,
        #     description="searches wikipedia and returns a multiline string containing all the links found for the searchTerm given",
        # ),
        Tool(
            name="get_google_search_results",
            func=get_google_search_results,
            description="takes a search term string as input and returns the output of the google search result for it",
        ),
        Tool(
            name="visit_web_link",
            func=visit_web_link,
            description="open a web URL (link) and get all the text listed on the page. link must be in a valid HTTP URL format",
        ),
        # Tool(name="save_text", func=save_text, description="saves input text to hard disk")
        # Tool(
        #     name="ask_chatgpt",
        #     func=ask_chatgpt,
        #     description="ask a question to chatgpt for any information before 2022. takes a question string as input for chatgpt and returns the answer as a string",
        # ),
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
    result = aexec.invoke(input={"input": my_prompt})
    print(result)
    ff.close()


if __name__ == "__main__":
    print("testing..")
    from sys import argv
    try:
        my_prompt = argv[-1]
        run_my_agent(my_prompt=my_prompt)
    finally:
        ff.close()
