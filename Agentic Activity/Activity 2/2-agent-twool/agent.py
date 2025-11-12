from datetime import datetime
from google.adk.agents import Agent
from google.adk.tools import google_search  # , VertexAI



root_agent = Agent(
    name="2-agent-twool",
    model="gemini-2.0-flash",
    description="Tool agent",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - current time
    """,
     tools=[google_search],
    # tools=[get_current_time],
    # tools=[google_search, get_current_time], # <--- Doesn't work cant combine
    # function with adk built in
)
