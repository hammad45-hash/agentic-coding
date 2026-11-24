
from agents import Agent, Runner, function_tool
from llm import model


@function_tool
def get_weather(city: str) -> str:
    """Get sample weather information for a city."""

    weather_data = {
        "karachi": "Sunny, 32°C",
        "lahore": "Cloudy, 27°C",
        "islamabad": "Rainy, 22°C",
        "hyderabad": "Sunny, 34°C"
    }

    return weather_data.get(
        city.lower(),
        "Weather information not available"
    )


agent = Agent(
    name="WeatherAgent",
    instructions="You are a helpful assistant. Use the weather tool when users ask about weather.",
    model=model,
    tools=[get_weather]
)


while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        break

    result = Runner.run_sync(agent, user_input)
    print("Agent:", result.final_output)

