#!/usr/bin/env python3
"""
CrewAI Agent Template - Main Entry Point

This script loads agent configurations from YAML files and runs the crew.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from utils.loader import ConfigLoader

def main():
    """Main function to load configuration and run the crew."""
    
    # Load environment variables
    load_dotenv()
    
    # Add the current directory to Python path for imports
    sys.path.append(str(Path(__file__).parent))
    
    # Default configuration file
    config_path = "config/default_agent_setup.yaml"
    
    # Allow command line override of config file
    if len(sys.argv) > 1:
        config_path = sys.argv[1]
    
    try:
        # Load configuration
        print(f"Loading configuration from: {config_path}")
        config = ConfigLoader.load_config(config_path)
        
        # Create crew from configuration
        print("Creating crew from configuration...")
        crew = ConfigLoader.create_crew_from_config(config)
        
        # Run the crew
        print(f"Running crew: {config['crew']['name']}")
        print(f"Description: {config['crew']['description']}")
        print("-" * 50)
        
        result = crew.kickoff()
        
        print("-" * 50)
        print("Crew execution completed!")
        print(f"Result: {result}")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please ensure the configuration file exists and is accessible.")
        sys.exit(1)
    except ValueError as e:
        print(f"Configuration error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 