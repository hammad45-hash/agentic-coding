from agents import Agent, Runner
from llm import model

INSTRUCTIONS = 'You are a helpful assistant for [CLIENT].'

agent = Agent(
    name='Assistant',
    instructions=INSTRUCTIONS,
    model=model,
)

while True:
    user_input = input('Ask something (or type quit): ')
    if user_input == 'quit':
        break
    result = Runner.run_sync(agent, user_input)
    print(result.final_output)
