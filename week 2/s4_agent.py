
from agents import Agent, Runner, function_tool
from llm import model
from ddgs import DDGS

# Web Search Tool
@function_tool
def web_search(query: str) -> str:
    """Search the internet and return useful results."""

    try:
        results = DDGS().text(query, max_results=5)

        if not results:
            return "No search results found."

        output = ""

        for item in results:
            output += f"""
Title: {item.get('title', 'No title')}
Website: {item.get('href', 'No link')}
Description: {item.get('body', 'No description')}

"""

        return output

    except Exception as e:
        return f"Search error: {str(e)}"


INSTRUCTIONS = """
You are a helpful AI assistant.
When the user asks for current information or web research,
use the web_search tool.
Explain results in simple language.
"""

agent = Agent(
    name="WebSearchAssistant",
    instructions=INSTRUCTIONS,
    model=model,
    tools=[web_search]
)

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        break

    result = Runner.run_sync(agent, user_input)
    print(f"Agent: {result.final_output}")
