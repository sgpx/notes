#!/usr/bin/env python3
import dotenv

dotenv.load_dotenv()
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
import re
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from token_count import TokenCount

token_counter = TokenCount(model_name="gpt-4o")

from sys import argv

SPLITTER_ACC_SIZE = 10000

summarize_enabled = True
mini_disabled = False
verbose = True

if "--4o" in argv:
    mini_disabled = True

if "-s" in argv or "--summarize" in argv:
    summarize_enabled = True

print("summarize", summarize_enabled)

verbose = "--verbose" in argv or "-v" in argv

model_id = "gpt-4o" if mini_disabled else "gpt-4o-mini"

print(model_id)

llm = ChatOpenAI(model_name=model_id)

summary_token_limit = 100000
options = Options()
#options.add_argument("--headless")
ff = webdriver.Firefox(keep_alive=False, options=options)
ff.install_addon("./ublock.xpi", temporary=False)
my_prompt = ""
summary_template = "summarize this text to find information relevant to `{my_prompt}` :\n`{mydata}` put all the valid text found valid URL links found in the bottom of the text. remove any unusable text."

summary_prompt_template = PromptTemplate(
    input_variables=["mydata"], template=summary_template
)
summary_llm_chain = LLMChain(llm=llm, prompt=summary_prompt_template)


def summarize(x):
    rv = (
        summary_llm_chain.invoke({"mydata": x, "my_prompt": my_prompt}).get("text")
        or ""
    )
    if verbose:
        print(rv)
    return rv


def count_llm_tokens(text):
    return token_counter.num_tokens_from_string(text)


def split_long_text(mytext):
    words = mytext.split(" ")
    split_lines = []
    acc = []
    for i in words:
        acc.append(i)
        if len(acc) == SPLITTER_ACC_SIZE:
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
        page = BeautifulSoup(html, features="lxml")
        rset = page.select(selector=target_selector)
        for i in rset:
            elem = i.select_one("a")
            link = elem.get("href")
            if link:
                rv.append(f"https://en.wikipedia.org/{link}")  # {"link": f})
    # print(rv)
    return "\n".join(rv)


def direct_scraper(link):
    """
    takes a web link as input and returns a string with its contents after opening the page with the requests module in python

    args:
        link - the link for the required page
    """
    session = r.Session()
    resp = session.get(link)
    soup = BeautifulSoup(resp.text, features="lxml")
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


def search_amazon_india(searchTerm):
    """
    takes a search term string as input and returns the output of the google search result for it

    args:
        searchTerm - type: str, the search term string
    """
    st = quote_plus(searchTerm)
    ff.get("https://www.amazon.in")
    amazon_link = f"https://www.amazon.in/s?k={st}&ref=nav_bb_sb"
    ff.get(amazon_link)
    sleep(1)
    soup = BeautifulSoup(ff.page_source)
    result = ""
    for text in soup.stripped_strings:
        result += text + " "
    result = re.sub(string=result, repl=" ", pattern=r" +", flags=re.IGNORECASE)
    if summarize_enabled:
        rt2 = llm.invoke(
            f"select all the valid links related to {my_prompt}\n" + result
        )
        return rt2.content
    return result


def search_pubmed(searchTerm: str) -> str:
    """
    takes a search term string as input and returns the output of the pubmed search result for it

    args:
        searchTerm - type: str, the search term string
    """
    st1 = quote_plus(searchTerm)
    link = f"https://pubmed.ncbi.nlm.nih.gov/?term={st1}"
    ff.get(link)
    raw_text = ""
    for ctag in wanted_tags + ["a"]:
        # print("looking for tag", ctag)
        elem = ff.find_elements(value=ctag, by=By.TAG_NAME)
        for i in elem:
            try:
                if ctag == "a":
                    raw_text += "\n"
                    raw_text += i.text + " - " + i.get_attribute("href")
                    raw_text += "\n"
                else:
                    raw_text += i.text

            except:
                pass
    if summarize_enabled:
        return split_and_summarize(raw_text)
    return raw_text


def get_indiamart_search_results(searchTerm):
    """
    takes a search term string as input and returns the output of the indiamart search results for it

    args:
        searchTerm - type: str, the search term string
    """
    qp = quote_plus(searchTerm)
    ff.get(f"https://dir.indiamart.com/search.mp?ss={qp}")
    raw_text = ""
    for ctag in ["span", "a"]:
        elem = ff.find_elements(value=ctag, by=By.TAG_NAME)
        for i in elem:
            if ctag == "a":
                link = i.get_attribute("href")
                if link:
                    raw_text += link + "\n"
            raw_text += i.text + "\n"
    return raw_text

def get_duckduckgo_search_results(searchTerm):
    """
    takes a search term string as input and returns the output of the duckduckgo search result for it

    args:
        searchTerm - type: str, the search term string
    """
    qp = quote_plus(searchTerm)
    ff.get(f"https://duckduckgo.com/?t=h_&q={qp}")
    raw_text = ""
    for ctag in ["span", "a"]:
        elem = ff.find_elements(value=ctag, by=By.TAG_NAME)
        for i in elem:
            if ctag == "a":
                link = i.get_attribute("href")
                if link:
                    raw_text += link + "\n"
            raw_text += i.text + "\n"    
    return raw_text

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
    if "Our systems have detected unusual traffic" in ff.page_source:
        print("Paused for captcha, press any key")
        z = input("Press any key when captcha is solved: ")
        print("continue")
    raw_text = ""
    for ctag in ["span", "a"]:
        elem = ff.find_elements(value=ctag, by=By.TAG_NAME)
        for i in elem:
            if ctag == "a":
                link = i.get_attribute("href")
                if link:
                    raw_text += link + "\n"
            raw_text += i.text + "\n"
    raw_text = re.sub(r"https\:\/\/www.google.com.+", "", raw_text)
    if summarize_enabled:
        rt2 = llm.invoke(
            f"select all the valid links related to {my_prompt}\n" + raw_text
        )
        return rt2.content
    return raw_text


def split_and_summarize(x):
    rv = ""
    rj = "\n".join([summarize(i) for i in split_long_text(x)])
    rv = summarize(rj)
    return rv


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
        # print("looking for tag", ctag)
        elem = ff.find_elements(value=ctag, by=By.TAG_NAME)
        for i in elem:
            try:
                raw_text += i.text
            except:
                pass
    if summarize_enabled:
        return split_and_summarize(raw_text)
    return raw_text


def google_search_link_getter(searchTerm) -> str:
    """
    takes a search term as input and returns the google search URL for that as output

    args:
        searchTerm - type: str
    """
    searchTerm = quote_plus(searchTerm)
    return f"https://www.google.com/search?q={searchTerm}"


def ask_chatgpt(question) -> str:
    """
    takes a question for chatgpt and returns the answer as a string. only valid for information before 2022

    args:
        question : str
    """
    l2c = LLMChain(
        llm=ChatOpenAI(model="gpt-3.5-turbo"),
        prompt=PromptTemplate(template="{input}", input_variables=["input"]),
    )
    return l2c.invoke({"input": question}).get("text")


def save_text(text):
    """
    saves text to hard disk

    args:
        text - str, text to be saved
    """
    open("output.txt", "a").write(text)


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
        Tool(
            name="search_amazon_india",
            func=search_amazon_india,
            description="takes a search term and returns information from amazon.in",
        ),
        Tool(
            name="get_indiamart_search_results",
            func=get_indiamart_search_results,
            description="takes a search term and returns information from indiamart",
        ),
        Tool(
            name="search_pubmed",
            func=search_pubmed,
            description="takes a search term and returns information from pubmed",
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
    aexec = AgentExecutor(agent=my_agent, tools=my_tools, verbose=verbose)
    result = aexec.invoke(
        input={
            "input": my_prompt
            + ". remember to cite the source you used and output its link"
        },
        handle_parsing_errors=True,
    )
    print("Question: ", result.get("input"))
    print("Output: ", result.get("output"))
    try:
        ff.close()
        ff.quit()
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(e)


if __name__ == "__main__":
    try:
        my_prompt = argv[-1]
        print(argv[-1])
        run_my_agent(my_prompt=my_prompt)
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(e)
