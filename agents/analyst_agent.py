from crewai import Agent
from tools.pest_control_research_tool import PestControlResearchTool

class AnalystAgent:
    """A specialized sales opportunity analyst for pest control training solutions."""
    
    @staticmethod
    def create():
        """Create and return a configured sales opportunity analyst agent."""
        return Agent(
            name="Sales Opportunity Analyst",
            role="Training Needs Assessment Specialist",
            goal="Analyze pest control companies to identify specific training gaps, compliance needs, and create targeted value propositions for Pest Pro University solutions",
            backstory="""You are a skilled sales analyst with deep expertise in the pest control industry 
            and training sector. You understand regulatory requirements across different states, 
            can assess company training needs based on their size and operations, and excel at 
            identifying specific pain points that Pest Pro University can solve. You can calculate 
            ROI for training investments, understand the value of CEU credits, and know how to 
            position different training tracks (Service Tech, Sales/Office, Business Management) 
            based on company profiles.""",
            verbose=True,
            allow_delegation=False,
            tools=[PestControlResearchTool()]
        ) 