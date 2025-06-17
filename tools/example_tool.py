from langchain.tools import BaseTool
from typing import Optional

class ExampleTool(BaseTool):
    """An example tool that returns a static response."""
    
    name: str = "example_tool"
    description: str = "A placeholder tool that returns a static response for demonstration purposes"
    
    def _run(self, query: Optional[str] = None) -> str:
        """Execute the tool and return a static response."""
        return "Tool result here. This is a placeholder response from the example tool."
    
    def _arun(self, query: Optional[str] = None) -> str:
        """Async version of the tool execution."""
        return self._run(query) 