from crewai import Agent
from tools.example_tool import ExampleTool

class ResearcherAgent:
    """A research agent that can gather and analyze information."""
    
    @staticmethod
    def create():
        """Create and return a configured researcher agent."""
        return Agent(
            name="Researcher",
            role="Research Specialist",
            goal="Gather comprehensive information and data from various sources to support analysis and decision-making",
            backstory="""You are an expert researcher with years of experience in gathering, 
            analyzing, and synthesizing information from multiple sources. You have a keen 
            eye for detail and can quickly identify relevant information from large datasets.""",
            verbose=True,
            allow_delegation=False,
            tools=[ExampleTool()]
        ) 