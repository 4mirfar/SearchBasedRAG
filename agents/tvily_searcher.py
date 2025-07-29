from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

def search(query):
    """
    Search for a query using the Tavily API.

    Args:
        query (str): The query string to search for.

    Returns:
        dict: The response from the Tavily API.
    """

    
    tavily_client = TavilyClient(TAVILY_API_KEY)

    response = tavily_client.search(query=query)

    return response

