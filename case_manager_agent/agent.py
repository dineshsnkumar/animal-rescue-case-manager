from google.adk.agents.llm_agent import Agent
from google.genai import types
from prompts import case_manager_agent_prompt

root_agent = Agent(
    model="gemini-3.5-flash",
    name="case_manager_agent",
    description="Handles animal rescue management operations",
    instruction=case_manager_agent_prompt,
)
