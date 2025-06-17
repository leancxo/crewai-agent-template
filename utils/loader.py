import yaml
import importlib
from typing import Dict, List, Any
from crewai import Agent, Task, Crew

class ConfigLoader:
    """Utility class for loading and instantiating agents from YAML configuration."""
    
    @staticmethod
    def load_config(config_path: str) -> Dict[str, Any]:
        """Load configuration from a YAML file."""
        try:
            with open(config_path, 'r') as file:
                config = yaml.safe_load(file)
            return config
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found: {config_path}")
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing YAML configuration: {e}")
    
    @staticmethod
    def instantiate_agent(agent_config: Dict[str, Any]) -> Agent:
        """Dynamically instantiate an agent from configuration."""
        try:
            # Import the module dynamically
            module = importlib.import_module(agent_config['module'])
            
            # Get the agent class
            agent_class = getattr(module, agent_config['class'])
            
            # Create the agent instance
            agent = agent_class.create()
            
            return agent
        except (ImportError, AttributeError) as e:
            raise ValueError(f"Error instantiating agent {agent_config['name']}: {e}")
    
    @staticmethod
    def create_agents_from_config(config: Dict[str, Any]) -> List[Agent]:
        """Create a list of agents from configuration."""
        agents = []
        
        for agent_config in config['crew']['agents']:
            if agent_config.get('enabled', True):
                agent = ConfigLoader.instantiate_agent(agent_config)
                agents.append(agent)
        
        return agents
    
    @staticmethod
    def create_tasks_from_config(config: Dict[str, Any], agents: List[Agent]) -> List[Task]:
        """Create a list of tasks from configuration."""
        tasks = []
        agent_map = {agent.name: agent for agent in agents}
        
        for task_config in config.get('tasks', []):
            agent_name = task_config['agent']
            if agent_name in agent_map:
                task = Task(
                    description=task_config['description'],
                    agent=agent_map[agent_name],
                    expected_output=task_config.get('expected_output', ''),
                    context=task_config.get('context', '')
                )
                tasks.append(task)
        
        return tasks
    
    @staticmethod
    def create_crew_from_config(config: Dict[str, Any]) -> Crew:
        """Create a complete crew from configuration."""
        agents = ConfigLoader.create_agents_from_config(config)
        tasks = ConfigLoader.create_tasks_from_config(config, agents)
        
        crew = Crew(
            agents=agents,
            tasks=tasks,
            verbose=config.get('settings', {}).get('verbose', True),
            memory=config.get('settings', {}).get('memory', False)
        )
        
        return crew 