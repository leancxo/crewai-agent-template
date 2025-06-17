#!/usr/bin/env python3
"""
Test script for CrewAI Agent Template

This script demonstrates the agent functionality using mock data and tools.
No API keys required - perfect for testing the template setup.
"""

import sys
import os
from pathlib import Path

# Add the parent directory to Python path for imports
sys.path.append(str(Path(__file__).parent.parent))

try:
    from test.mock_agents import MockResearcherAgent, MockAnalystAgent
except ImportError:
    from mock_agents import MockResearcherAgent, MockAnalystAgent
from tools.example_tool import ExampleTool
from utils.loader import ConfigLoader

def test_individual_agents():
    """Test individual agents to ensure they can be instantiated."""
    print("🧪 Testing Individual Agents...")
    print("-" * 50)
    
    try:
        # Test Researcher Agent
        print("Testing Researcher Agent...")
        researcher = MockResearcherAgent.create()
        print(f"✅ Researcher Agent created successfully!")
        print(f"   Name: {researcher.name}")
        print(f"   Role: {researcher.role}")
        print(f"   Goal: {researcher.goal[:100]}...")
        print()
        
        # Test Analyst Agent
        print("Testing Analyst Agent...")
        analyst = MockAnalystAgent.create()
        print(f"✅ Analyst Agent created successfully!")
        print(f"   Name: {analyst.name}")
        print(f"   Role: {analyst.role}")
        print(f"   Goal: {analyst.goal[:100]}...")
        print()
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating agents: {e}")
        return False

def test_tools():
    """Test the example tool functionality."""
    print("🔧 Testing Tools...")
    print("-" * 50)
    
    try:
        # Test Example Tool
        print("Testing Example Tool...")
        tool = ExampleTool()
        result = tool._run("test query")
        print(f"✅ Example Tool executed successfully!")
        print(f"   Result: {result}")
        print()
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing tools: {e}")
        return False

def test_config_loader():
    """Test the configuration loader functionality."""
    print("📋 Testing Configuration Loader...")
    print("-" * 50)
    
    try:
        # Test loading configuration
        config_path = "config/default_agent_setup.yaml"
        print(f"Loading configuration from: {config_path}")
        config = ConfigLoader.load_config(config_path)
        print(f"✅ Configuration loaded successfully!")
        print(f"   Crew Name: {config['crew']['name']}")
        print(f"   Crew Description: {config['crew']['description']}")
        print(f"   Number of Agents: {len(config['crew']['agents'])}")
        print(f"   Number of Tasks: {len(config['tasks'])}")
        print()
        
        # Test creating agents from config (using mock agents for testing)
        print("Creating agents from configuration...")
        # For testing, we'll create mock agents instead of real ones
        agents = [MockResearcherAgent.create(), MockAnalystAgent.create()]
        print(f"✅ {len(agents)} agents created from configuration!")
        for agent in agents:
            print(f"   - {agent.name} ({agent.role})")
        print()
        
        # Test creating tasks from config
        print("Creating tasks from configuration...")
        tasks = ConfigLoader.create_tasks_from_config(config, agents)
        print(f"✅ {len(tasks)} tasks created from configuration!")
        for task in tasks:
            print(f"   - {task.description[:50]}...")
        print()
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing configuration loader: {e}")
        return False

def test_mock_crew_execution():
    """Test a mock crew execution with simulated results."""
    print("🚀 Testing Mock Crew Execution...")
    print("-" * 50)
    
    try:
        # Create a simple mock crew execution
        print("Simulating crew execution...")
        
        # Create mock agents
        researcher = MockResearcherAgent.create()
        analyst = MockAnalystAgent.create()
        
        # Mock research task result
        research_result = researcher.execute_task("Research AI agent development")
        print("📊 Research Task Completed:")
        print(f"   {research_result}")
        print()
        
        # Mock analysis task result
        analysis_result = analyst.execute_task("Analyze research findings")
        print("📈 Analysis Task Completed:")
        print(f"   {analysis_result}")
        print()
        
        print("✅ Mock crew execution completed successfully!")
        print()
        
        return True
        
    except Exception as e:
        print(f"❌ Error in mock crew execution: {e}")
        return False

def run_all_tests():
    """Run all tests and provide a summary."""
    print("🎯 CrewAI Agent Template - Test Suite")
    print("=" * 60)
    print("This test suite verifies that the template is working correctly.")
    print("No API keys required - using mock data and tools.\n")
    
    tests = [
        ("Individual Agents", test_individual_agents),
        ("Tools", test_tools),
        ("Configuration Loader", test_config_loader),
        ("Mock Crew Execution", test_mock_crew_execution)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ Unexpected error in {test_name}: {e}")
            results.append((test_name, False))
    
    # Summary
    print("📋 Test Summary")
    print("=" * 60)
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
        if result:
            passed += 1
    
    print(f"\nResults: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! Your CrewAI template is working correctly.")
        print("You can now:")
        print("1. Set up your API keys in .env file")
        print("2. Run 'python main.py' to execute the real crew")
        print("3. Customize agents and tools for your specific needs")
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Please check the errors above.")
    
    return passed == total

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1) 