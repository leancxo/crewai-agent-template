# CrewAI Agent Template

A reusable template for creating agentic AI projects using [CrewAI](https://github.com/crewAIInc/crewAI). This template provides a structured approach to building multi-agent systems with configurable agents, tasks, and tools.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-0.130.0+-green.svg)](https://github.com/crewAIInc/crewAI)

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- OpenAI API key (or other LLM provider)

### Installation

1. **Clone this template:**
```bash
git clone https://github.com/yourusername/crewai-agent-template.git
cd crewai-agent-template
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables:**
```bash
cp .env.template .env
# Edit .env with your API keys
```

4. **Run the template:**
```bash
python main.py
```

## 🧪 Testing the Template

**No API keys required!** Test the template functionality immediately:

### Quick Demo
```bash
python demo.py
```
Shows a simple demonstration of agent creation and workflow simulation.

### Comprehensive Testing
```bash
python test/test_agents.py
```
Runs a full test suite that verifies:
- ✅ Agent instantiation
- ✅ Tool functionality
- ✅ Configuration loading
- ✅ Mock crew execution

### Test Results
The test suite will show you exactly what's working:
```
🎯 CrewAI Agent Template - Test Suite
============================================================
🧪 Testing Individual Agents...
✅ Researcher Agent created successfully!
✅ Analyst Agent created successfully!

🔧 Testing Tools...
✅ Example Tool executed successfully!

📋 Testing Configuration Loader...
✅ Configuration loaded successfully!
✅ 2 agents created from configuration!
✅ 2 tasks created from configuration!

🚀 Testing Mock Crew Execution...
✅ Mock crew execution completed successfully!

📋 Test Summary
============================================================
✅ PASS - Individual Agents
✅ PASS - Tools
✅ PASS - Configuration Loader
✅ PASS - Mock Crew Execution

Results: 4/4 tests passed

🎉 All tests passed! Your CrewAI template is working correctly.
```

## 📁 Project Structure

```
crewai-agent-template/
├── agents/                 # Agent definitions
│   ├── researcher_agent.py
│   └── analyst_agent.py
├── config/                 # YAML configuration files
│   ├── default_agent_setup.yaml
│   └── test_setup.yaml
├── tools/                  # Custom tools for agents
│   └── example_tool.py
├── utils/                  # Utility functions
│   └── loader.py
├── test/                   # Test suite
│   └── test_agents.py
├── main.py                 # Entry point
├── demo.py                 # Demo script
├── README.md              # This file
├── requirements.txt       # Dependencies
├── .env.template          # Environment variables template
├── .gitignore            # Git ignore rules
├── cursor.rules           # Cursor IDE rules
└── LICENSE               # MIT License
```

## 🔧 How to Use

### Running the Template

The template comes with a default configuration that includes:
- **Researcher Agent**: Gathers information and data
- **Analyst Agent**: Analyzes data and provides insights

To run with the default configuration:
```bash
python main.py
```

To run with a custom configuration:
```bash
python main.py config/your_config.yaml
```

### Adding New Agents

1. Create a new agent file in `agents/`:
```python
from crewai import Agent
from tools.example_tool import ExampleTool

class YourAgent:
    @staticmethod
    def create():
        return Agent(
            name="Your Agent",
            role="Your Role",
            goal="Your goal description",
            backstory="Your agent's backstory",
            verbose=True,
            allow_delegation=False,
            tools=[ExampleTool()]
        )
```

2. Add the agent to your configuration file:
```yaml
crew:
  agents:
    - name: "your_agent"
      class: "YourAgent"
      module: "agents.your_agent"
      enabled: true
      order: 3
```

### Adding Custom Tools

1. Create a new tool in `tools/`:
```python
from langchain.tools import BaseTool

class YourTool(BaseTool):
    name: str = "your_tool"
    description: str = "Description of what your tool does"
    
    def _run(self, query: str) -> str:
        # Your tool logic here
        return "Tool result"
```

2. Import and use the tool in your agents.

### Configuration Files

Configuration files use YAML format and define:
- **Crew**: Name, description, and agent list
- **Tasks**: Task descriptions, assigned agents, and expected outputs
- **Settings**: Global settings like verbosity and memory

Example configuration structure:
```yaml
crew:
  name: "My Crew"
  description: "Description of what this crew does"
  agents:
    - name: "agent1"
      class: "AgentClass"
      module: "agents.agent_file"
      enabled: true
      order: 1

tasks:
  - name: "Task 1"
    description: "What this task does"
    agent: "agent1"
    expected_output: "Expected result"

settings:
  verbose: true
  max_iterations: 3
  memory: true
```

## 🛠️ Customization

### Environment Variables

Copy `.env.template` to `.env` and configure:
- `OPENAI_API_KEY`: Your OpenAI API key
- `ANTHROPIC_API_KEY`: Your Anthropic API key (optional)
- Other LLM provider keys as needed

### Adding New Configurations

1. Create new YAML files in `config/`
2. Define your agent setup, tasks, and settings
3. Run with: `python main.py config/your_config.yaml`

### Extending the Template

- **New Agent Types**: Add specialized agents for different domains
- **Custom Tools**: Integrate with external APIs, databases, or services
- **Task Templates**: Create reusable task patterns
- **Monitoring**: Add logging and performance tracking

## 📚 Examples

### Basic Research Crew
```yaml
crew:
  name: "Research Crew"
  agents:
    - name: "researcher"
      class: "ResearcherAgent"
      module: "agents.researcher_agent"
    - name: "analyst"
      class: "AnalystAgent"
      module: "agents.analyst_agent"

tasks:
  - name: "Research Topic"
    description: "Research the given topic thoroughly"
    agent: "researcher"
  - name: "Analyze Findings"
    description: "Analyze research findings and provide insights"
    agent: "analyst"
```

## 🤝 Contributing

We welcome contributions! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For issues and questions:
1. Check the [CrewAI documentation](https://docs.crewai.com/)
2. Review the configuration examples in this repository
3. Open an issue in this repository

## 🙏 Acknowledgments

- Built with [CrewAI](https://github.com/crewAIInc/crewAI) - Framework for orchestrating role-playing, autonomous AI agents
- Inspired by the need for reusable, production-ready agent templates

---

**Happy building with CrewAI! 🚀**

---

## 📦 Publishing Information

This template is designed to be:
- **Forkable**: Clone and adapt for your specific use cases
- **Extensible**: Easy to add new agents, tools, and configurations
- **Production-Ready**: Includes error handling, logging, and security best practices
- **Well-Documented**: Comprehensive examples and documentation
- **Testable**: Complete test suite that works without API keys

### For Template Users

1. **Fork this repository** to your GitHub account
2. **Clone your fork** locally
3. **Test the template** with `python test/test_agents.py`
4. **Customize** the agents, tools, and configurations for your needs
5. **Deploy** your agentic AI solution

### For Contributors

We welcome contributions to make this template even better:
- New agent types
- Additional tools and integrations
- Configuration examples
- Documentation improvements
- Bug fixes and performance optimizations

---

**Star this repository if you find it helpful! ⭐** 