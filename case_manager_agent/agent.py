from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from google.adk.planners import PlanReActPlanner
from mcp import StdioServerParameters
from .prompts import case_manager_agent_prompt
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

os.environ["LITELLM_LOG"] = "DEBUG"


root_agent = LlmAgent(
    model=LiteLlm(model="groq/qwen/qwen3.6-27b"),
    planner=PlanReActPlanner(),
    name="case_manager_agent",
    description="Handles animal rescue management operations",
    instruction=case_manager_agent_prompt,
    tools=[
        McpToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="uv",
                    args=[
                        "run",
                        "python",
                        "mcp/server.py",
                    ],
                )
            )
        )
    ],
)
