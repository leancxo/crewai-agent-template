#!/usr/bin/env python3
"""
CrewAI Agent Template - Demo Script

This script demonstrates the template functionality with a simple example.
Perfect for showing how the template works without requiring API keys.
"""

import sys
from pathlib import Path

# Add the current directory to Python path for imports
sys.path.append(str(Path(__file__).parent))

from test.mock_agents import MockResearcherAgent, MockAnalystAgent
from tools.example_tool import ExampleTool

def run_demo():
    """Run a simple demo of the template functionality."""
    
    print("🎯 CrewAI Agent Template - Demo")
    print("=" * 50)
    print("This demo shows how the template works with mock data.")
    print("No API keys required!\n")
    
    # Create agents
    print("🤖 Creating Agents...")
    researcher = MockResearcherAgent.create()
    analyst = MockAnalystAgent.create()
    
    print(f"✅ Created {researcher.name} - {researcher.role}")
    print(f"✅ Created {analyst.name} - {analyst.role}")
    print()
    
    # Demonstrate tool usage
    print("🔧 Testing Tools...")
    tool = ExampleTool()
    tool_result = tool._run("demo query")
    print(f"✅ Tool result: {tool_result}")
    print()
    
    # Simulate a simple workflow
    print("🚀 Simulating Agent Workflow...")
    print("-" * 30)
    
    # Mock research phase
    print("📊 Research Phase:")
    research_result = researcher.execute_task("Research AI agent development trends")
    print(f"   {research_result}")
    print()
    
    # Mock analysis phase
    print("📈 Analysis Phase:")
    analysis_result = analyst.execute_task("Analyze research findings and provide recommendations")
    print(f"   {analysis_result}")
    print()
    
    # Final output
    print("🎉 Demo Completed Successfully!")
    print("=" * 50)
    print("The template is working correctly!")
    print()
    print("Next steps:")
    print("1. Run 'python test/test_agents.py' for comprehensive testing")
    print("2. Set up API keys in .env file for real agent execution")
    print("3. Run 'python main.py' to execute the full crew")
    print("4. Customize agents and tools for your specific needs")
    print()
    print("Happy building with CrewAI! 🚀")

if __name__ == "__main__":
    run_demo() 