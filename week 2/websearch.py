
import os
from dotenv import load_dotenv
from tavily import TavilyClient
from agents import function_tool

load_dotenv()

tavily = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

@function_tool
def web_search(query: str) -> str:
    """Search the internet for information."""

    try:
        response = tavily.search(
            query=query,
            max_results=5
        )

        results = response.get("results", [])

        if not results:
            return "No search results found."

        output = []

        for item in results:
            output.append(
                f"Title: {item.get('title')}\n"
                f"Content: {item.get('content')}\n"
                f"URL: {item.get('url')}"
            )

        return "\n\n".join(output)

    except Exception as e:
        return f"Search Error: {str(e)}"