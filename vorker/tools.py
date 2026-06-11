"""
Tool definitions for [PRODUCT NAME] agent.
Each function is wrapped automatically by ADK as a FunctionTool.
Keep docstrings accurate — the model reads them to decide when to call each tool.
"""

from google.adk.tools import FunctionTool


def tool_one(input_data: str) -> dict:
    """
    [TOOL ONE DESCRIPTION — what it does, when the agent should use it].

    Args:
        input_data: [describe what input this tool expects]

    Returns:
        A dict with keys: 'status', 'result', 'message'
    """
    # TODO: replace with real logic on problem reveal
    return {
        "status": "success",
        "result": f"Processed: {input_data}",
        "message": "Tool one executed successfully.",
    }


def tool_two(query: str) -> dict:
    """
    [TOOL TWO DESCRIPTION — what it does, when the agent should use it].

    Args:
        query: [describe what query/input this tool expects]

    Returns:
        A dict with keys: 'status', 'data', 'message'
    """
    # TODO: replace with real logic on problem reveal
    return {
        "status": "success",
        "data": {"query": query, "response": "Placeholder response"},
        "message": "Tool two executed successfully.",
    }


# Export as ADK FunctionTools
tool_one = FunctionTool(tool_one)
tool_two = FunctionTool(tool_two)
