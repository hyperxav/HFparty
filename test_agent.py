from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

# Create a simple agent with DuckDuckGo search capability
agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()], 
    model=HfApiModel(model="Qwen/Qwen2.5-Coder-32B-Instruct")
)

# Test the agent with a simple query
result = agent.run("Search for the best music recommendations for a party at the Wayne's mansion.") 