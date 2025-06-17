from crewai import Agent
from tools.example_tool import ExampleTool

class AnalystAgent:
    """An analyst agent that can process and interpret data."""
    
    @staticmethod
    def create():
        """Create and return a configured analyst agent."""
        return Agent(
            name="Analyst",
            role="Data Analyst",
            goal="Analyze data and information to provide insights, trends, and actionable recommendations",
            backstory="""You are a skilled data analyst with expertise in statistical analysis, 
            trend identification, and data visualization. You excel at turning raw data into 
            meaningful insights that drive decision-making.""",
            verbose=True,
            allow_delegation=False,
            tools=[ExampleTool()]
        ) 