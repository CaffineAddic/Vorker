"""
[PRODUCT NAME] — AI Agent
Built with Google ADK for Vorker Intern Tryouts, Phase 1.
"""

from google.adk.agents import Agent
from .tools import tool_one, tool_two

root_agent = Agent(
    name="[product_name]_agent",
    model="gemini-2.0-flash",
    description=(
        "An AI agent that helps [target user] with [specific task], "
        "saving them time and reducing manual effort."
    ),
    instruction=(
        "You are a helpful AI coworker for [target user type]. "
        "Your job is to [core job description]. "
        "Always be concise, professional, and action-oriented. "
        "When you need more information, ask one clarifying question at a time. "
        "Confirm before taking any irreversible action."
    ),
    tools=[tool_one, tool_two],
)
