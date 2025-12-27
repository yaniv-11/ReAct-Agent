import os
from dotenv import load_dotenv

load_dotenv()  

from langchain_community.utilities import WikipediaAPIWrapper, SerpAPIWrapper
from langchain_community.tools import WikipediaQueryRun


wiki = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper(top_k_results=2)
)

google = SerpAPIWrapper(
    serpapi_api_key=os.getenv("SERPAPI_API_KEY")
)

def wikipedia(query: str) -> str:
    return wiki.run(query)

def search(query: str) -> str:
    return google.run(query)
