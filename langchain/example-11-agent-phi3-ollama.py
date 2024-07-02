#!/usr/bin/env python3
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
from time import sleep, time
import re

output_filename = f"output-{int(time())}.txt"
open(output_filename, "w").write("text dump starts here:\n\n")
llm = Ollama(model="phi3")
summary_model_token_limit = 100000
ff = None
summary_template = "summarize this text:\n`{mydata}` put all the URL links found in the bottom of the text. if the text is garbage, do not return anything"

summary_prompt_template = PromptTemplate(
    input_variables=["mydata"], template=summary_template
)
summary_llm_chain = LLMChain(llm=Ollama(model="phi3"), prompt=summary_prompt_template)


def summarize(x: str):
    if not x:
        return
    open(output_filename, "a").write("\n\n" + x + "\n\n")
    rv = summary_llm_chain.invoke({"mydata": x}).get("text") or ""
    open(output_filename, "a").write("\n\n" + rv + "\n\n")
    return rv


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


def get_google_news_results(searchTerm):
    """
    takes a search term string as input and returns the output of the google news search result for it

    args:
        searchTerm - type: str, the search term string
    """
    ff.get(google_news_link(searchTerm=searchTerm))
    sleep(2)
    raw_text = ""
    for ctag in ["span", "a"]:
        elem = ff.find_elements(value=ctag, by=By.TAG_NAME)
        for i in elem:
            if ctag == "a":
                if not i.text:
                    continue
                link = i.get_attribute("href")
                if link and "./articles" in link and link.index("./articles") == 0:
                    link = link.replace(
                        "./articles", "https://news.google.com/articles"
                    )
                    visit_web_link(link=link)
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
    print(rv2)
    return rv2[0:1000]


def visit_web_link(link):
    """
    takes a web URL as input and returns all the text contained on the page at that URL. link must be in a valid HTTP URL format

    args:
        link - type: str, the URL for the page to be visited
    """
    blocked_domains = ["educba.com", "investors.com"]
    if any([bad_domain in link.lower() for bad_domain in blocked_domains]):
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
    print(rv)
    print("final summary OK")
    return rv


def google_news_link(searchTerm) -> str:
    """
    takes a search term as input and returns the google news URL for that as output

    args:
        searchTerm - type: str
    """
    searchTerm = quote_plus(searchTerm)
    return f"https://news.google.com/search?q={searchTerm}&hl=en-IN&gl=IN&ceid=IN%3Aen"


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
    open(output_filename, "a").write(text+"\n\n")


def run_agent(agent_prompt):
    my_tools = [
        Tool(
            name="get_google_news_results",
            func=get_google_news_results,
            description="takes a search term string as input and returns the output of the google news search result for it",
        ),
        Tool(
            name="visit_web_link",
            func=visit_web_link,
            description="open a web URL (link) and get all the text listed on the page. link must be in a valid HTTP URL format",
        ),
        # Tool(
        #     name="direct_scraper",
        #     func=direct_scraper,
        #     description="takes a web link as input and returns a string with its contents after opening the page with the requests module in python",
        # ),
    ]
    react_prompt = hub.pull("hwchase17/react")
    my_agent = create_react_agent(llm=llm, tools=my_tools, prompt=react_prompt)
    aexec = AgentExecutor(agent=my_agent, tools=my_tools, verbose=True)
    result = aexec.invoke(input={"input": agent_prompt})
    print(result)


if __name__ == "__main__":
    print("testing..")
    try:
        ff = webdriver.Firefox(keep_alive=False)
        ff.install_addon("./ublock.xpi", temporary=False)
        run_agent(agent_prompt="find as many articles about financial frauds in india as possible")
    finally:
        ff.close()
