"""
Mock Agent Classes for Testing

These classes provide mock implementations of agents that don't require API keys.
Perfect for testing the template functionality without external dependencies.
"""

try:
    from tools.example_tool import ExampleTool
except ImportError:
    import sys
    import os
    from pathlib import Path
    sys.path.append(str(Path(__file__).parent.parent))
    from tools.example_tool import ExampleTool

class MockAgent:
    """A mock agent class that simulates CrewAI Agent behavior without API calls."""
    
    def __init__(self, name, role, goal, backstory, tools=None, verbose=True, allow_delegation=False):
        self.name = name
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.tools = tools or []
        self.verbose = verbose
        self.allow_delegation = allow_delegation
    
    def execute_task(self, task_description):
        """Mock task execution that returns a simulated result."""
        if self.verbose:
            print(f"🤖 {self.name} ({self.role}) executing task...")
        
        # Simulate different responses based on agent type
        if "research" in self.name.lower():
            return f"Research completed by {self.name}: Found comprehensive data on the topic."
        elif "analyst" in self.name.lower():
            return f"Analysis completed by {self.name}: Generated insights and recommendations."
        else:
            return f"Task completed by {self.name}: Processed the request successfully."

class MockResearcherAgent:
    """Mock researcher agent for testing."""
    
    @staticmethod
    def create():
        """Create and return a mock researcher agent."""
        return MockAgent(
            name="Researcher",
            role="Research Specialist",
            goal="Gather comprehensive information and data from various sources to support analysis and decision-making",
            backstory="You are an expert researcher with years of experience in gathering, analyzing, and synthesizing information from multiple sources.",
            tools=[ExampleTool()],
            verbose=True,
            allow_delegation=False
        )

class MockAnalystAgent:
    """Mock analyst agent for testing."""
    
    @staticmethod
    def create():
        """Create and return a mock analyst agent."""
        return MockAgent(
            name="Analyst",
            role="Data Analyst",
            goal="Analyze data and information to provide insights, trends, and actionable recommendations",
            backstory="You are a skilled data analyst with expertise in statistical analysis, trend identification, and data visualization.",
            tools=[ExampleTool()],
            verbose=True,
            allow_delegation=False
        ) 