# AI Multi-Agent Crew Projects

This repository contains two powerful multi-agent AI systems built with [crewAI](https://crewai.com), designed to automate complex workflows through intelligent agent collaboration.

## 📋 Table of Contents

- [Projects Overview](#projects-overview)
- [Market Research Crew](#market-research-crew)
- [Research and Blog Crew](#research-and-blog-crew)
- [Technology Stack](#technology-stack)
- [Customization Guide](#customization-guide)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

---

## 🎯 Projects Overview

### 1. Market Research Crew
A comprehensive market research system that conducts in-depth analysis for AI product ideas through five specialized agents working sequentially.

### 2. Research and Blog Crew
A streamlined content creation system that researches topics and generates engaging blog posts through collaborative AI agents.

---

## 📊 Market Research Crew

### Overview
The Market Research Crew performs end-to-end market analysis for AI product ideas, delivering professional-grade reports ready for investor or executive presentations.

### ✨ Key Features
- **Comprehensive Market Analysis**: TAM/SAM/SOM sizing, growth projections, and regulatory landscape
- **Competitive Intelligence**: Detailed competitor analysis with positioning maps
- **Customer Insights**: Deep segmentation with detailed personas and journey mapping
- **Product Strategy**: MVP feature prioritization and technical feasibility assessment
- **Business Analysis**: Pricing strategy, financial projections, and go-to-market recommendations

### 🤖 Specialized Agents

#### 1. Market Research Specialist (15+ years experience)
- Market sizing and growth trend analysis
- Industry dynamics and technology adoption patterns
- Regulatory landscape assessment

#### 2. Competitive Intelligence Analyst (12+ years experience)
- Competitor identification and analysis
- Market positioning and gap analysis
- Competitive threat assessment

#### 3. Customer Insights Researcher (10+ years experience)
- Customer segmentation and persona development
- Pain point analysis and needs assessment
- Customer journey mapping

#### 4. Product Strategy Advisor (15+ years experience)
- MVP feature prioritization
- Differentiation strategy design
- Technical feasibility assessment
- Development roadmap creation

#### 5. Business Analyst (12+ years experience)
- Pricing and revenue model design
- Financial projections and risk analysis
- Investment thesis development
- Go/No-Go recommendations

### 📁 Project Structure
```
market_research_crew/
├── src/market_research_crew/
│   ├── config/
│   │   ├── agents.yaml          # Agent definitions
│   │   └── tasks.yaml           # Task definitions
│   ├── tools/
│   │   ├── __init__.py
│   │   └── custom_tool.py       # Custom tool templates
│   ├── __init__.py
│   ├── crew.py                  # Crew implementation
│   └── main.py                  # Entry point
├── knowledge/
│   └── user_preference.txt      # User preferences
├── reports/                     # Generated reports
├── pyproject.toml              # Project configuration
└── README.md
```

### 🚀 Installation & Setup

#### Prerequisites
- Python >=3.10 <3.14
- UV package manager

#### Install UV
```bash
pip install uv
```

#### Install Dependencies
```bash
cd market_research_crew
uv sync
```

#### Configuration
Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_gemini_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

### 💻 Usage

#### Run Market Research
```bash
uv run market_research_crew
```
or
```bash
uv run run_crew
```

#### Customize Product Idea
Edit `src/market_research_crew/main.py`:
```python
inputs = {
    "product_idea": "Your AI product idea here"
}
```

**Default Example**: The project is pre-configured to analyze an AI-powered YouTube video summarization and social media posting tool.

### 📝 Available Commands
```bash
uv run market_research_crew    # Run the market research crew
uv run run_crew                # Alternative command to run the crew
uv run train                   # Train the crew
uv run replay                  # Replay previous executions
uv run test                    # Run tests
uv run run_with_trigger        # Run with triggers
```

### 📄 Output
Reports are saved in the `reports/` directory with comprehensive analysis:

| Report Type | Word Count | Content |
|------------|-----------|---------|
| Market Research | 1500-2000 | Market sizing, growth trends, regulatory landscape |
| Competitive Intelligence | 2000-2500 | Competitor profiles, positioning maps, gap analysis |
| Customer Insights | 2000-2500 | Personas, pain points, customer journey |
| Product Strategy | 2500-3000 | MVP features, technical feasibility, roadmap |
| Business Analysis | 3000-4000 | Pricing, financials, investment recommendations |

---

## 📝 Research and Blog Crew

### Overview
The Research and Blog Crew automates the content creation process by researching topics and generating engaging, SEO-friendly blog posts.

### ✨ Key Features
- Automated topic research
- Comprehensive report generation (~2000 words)
- Engaging blog post creation (~500 words)
- Markdown-formatted output

### 🤖 Specialized Agents

#### 1. Report Generator
- Synthesizes information from multiple sources
- Creates detailed, structured reports
- Provides actionable insights

#### 2. Blog Writer
- Crafts engaging, accessible content
- Highlights key findings
- Optimizes for readability and engagement

### 📁 Project Structure
```
research_and_blog_crew/
├── src/research_and_blog_crew/
│   ├── config/
│   │   ├── agents.yaml          # Agent definitions
│   │   └── tasks.yaml           # Task definitions
│   ├── tools/
│   │   ├── __init__.py
│   │   └── custom_tool.py       # Custom tool templates
│   ├── __init__.py
│   ├── crew.py                  # Crew implementation
│   └── main.py                  # Entry point
├── blogs/                       # Generated blog posts
├── knowledge/
│   └── user_preference.txt      # User preferences
├── pyproject.toml              # Project configuration
└── README.md
```

### 🚀 Installation & Setup

#### Install Dependencies
```bash
cd research_and_blog_crew
uv sync
```

#### Configuration
Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 💻 Usage

#### Run Blog Generation
```bash
uv run research_and_blog_crew
```
or
```bash
uv run run_crew
```

#### Customize Topic
Edit `src/research_and_blog_crew/main.py`:
```python
inputs = {
    'topic': 'Your topic here'
}
```

**Default Example**: The project is pre-configured to research and write about "AI Agents in coding".

### 📝 Available Commands
```bash
uv run research_and_blog_crew    # Run the crew
uv run run_crew                  # Alternative command to run the crew
uv run train                     # Train the crew
uv run replay                    # Replay previous executions
uv run test                      # Run tests
uv run run_with_trigger          # Run with triggers
```

### 📄 Output
Blog posts are saved in the `blogs/` directory:
- **Research Report**: Comprehensive analysis (~2000 words)
- **Blog Post**: Engaging content in markdown format (~500 words)
- No code blocks, ready for publishing

---

## 🛠️ Technology Stack

### Core Framework
- **crewAI**: Multi-agent orchestration framework (v1.7.2)

### AI Models
- **Google Gemini AI**: Advanced language model for agent intelligence

### Tools & Integrations

#### Market Research Crew
- **Serper**: Web search capabilities
- **Selenium**: Web scraping automation
- **WebDriver Manager**: Browser driver management

### Development
- **UV**: Modern Python package manager
- **Python**: >=3.10 <3.14

---

## 🎨 Customization Guide

### Adding New Agents

**Step 1**: Define in `config/agents.yaml`
```yaml
new_agent:
  role: >
    Agent Role Description
  goal: >
    Agent Goal
  backstory: >
    Agent Background and Expertise
```

**Step 2**: Implement in `crew.py`
```python
@agent
def new_agent(self) -> Agent:
    return Agent(
        config=self.agents_config["new_agent"],
        tools=toolkit  # Optional
    )
```

### Adding New Tasks

**Step 1**: Define in `config/tasks.yaml`
```yaml
new_task:
  description: >
    Detailed task description with {variable} placeholders
  expected_output: >
    Description of expected output format and content
  agent: agent_name
```

**Step 2**: Implement in `crew.py`
```python
@task
def new_task(self) -> Task:
    return Task(
        config=self.tasks_config["new_task"],
        context=[self.prerequisite_task()],  # Optional
        output_file="path/to/output.md"      # Optional
    )
```

### Creating Custom Tools

Create in `tools/custom_tool.py`:
```python
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class CustomToolInput(BaseModel):
    """Input schema for CustomTool."""
    argument: str = Field(..., description="Argument description")

class CustomTool(BaseTool):
    name: str = "Tool Name"
    description: str = "Tool description for agent understanding"
    args_schema: Type[BaseModel] = CustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "result"
```

---

## 🔄 Process Flows

### Market Research Crew Flow
```
Market Research → Competitive Intelligence → Customer Insights → Product Strategy → Business Analysis
```
Each stage builds upon previous findings, creating a comprehensive analysis chain.

### Research and Blog Crew Flow
```
Report Generation → Blog Writing
```
Sequential process ensures blog content is based on thorough research.

---

## 💡 Best Practices

### For Market Research Crew
- ✅ Provide specific, detailed product ideas
- ✅ Review agent configurations for domain-specific needs
- ✅ Customize task descriptions for industry focus
- ✅ Validate API keys for web search functionality
- ✅ Allow sufficient time for comprehensive research (can take 15-30 minutes)

### For Research and Blog Crew
- ✅ Choose topics with sufficient online resources
- ✅ Adjust word counts in task configurations as needed
- ✅ Review knowledge base for personalization
- ✅ Customize agent backstories for tone preferences
- ✅ Test with narrow topics before broad ones

### General Tips
- 🔧 Enable verbose mode for debugging: `verbose=True`
- 🧠 Use memory for complex, context-dependent tasks: `memory=True`
- ⚡ Adjust `max_rpm` in crew configuration for API rate limits
- 🧪 Test with smaller scopes before full production runs
- 📊 Monitor token usage to optimize costs

---

## 🐛 Troubleshooting

### Common Issues

#### Import Errors
```bash
uv sync  # Reinstall dependencies
```

#### API Key Errors
- ✓ Verify `.env` file exists in project root
- ✓ Check API key validity
- ✓ Ensure proper environment variable loading
- ✓ Restart terminal after adding `.env` file

#### Agent Performance Issues
- ✓ Review agent backstories and goals for clarity
- ✓ Check task descriptions for specificity
- ✓ Validate tool configurations
- ✓ Monitor API rate limits

#### Installation Issues
```bash
# Check Python version
python --version  # Should be >=3.10 <3.14

# Reinstall UV
pip install --upgrade uv

# Clean install
rm -rf .venv
uv sync
```

---

## 🎯 Example Use Cases

### Market Research Crew
- 💼 Validating startup ideas
- 🚀 Competitive analysis for product launches
- 💰 Investment opportunity assessment
- 🌍 Market entry strategy development
- 🎯 Product-market fit validation
- 📈 Due diligence for acquisitions

### Research and Blog Crew
- 📱 Content marketing automation
- 📚 Technical documentation
- 📊 Industry trend analysis
- 🎓 Educational content creation
- 💭 Thought leadership pieces
- 🔍 SEO-optimized blog posts

---

## 🔧 Advanced Configuration

### Customizing Crew Behavior

#### Adjust Process Type
```python
@crew
def crew(self) -> Crew:
    return Crew(
        agents=self.agents,
        tasks=self.tasks,
        process=Process.sequential,  # or Process.hierarchical
        verbose=True,
        memory=True,                 # Enable for context retention
        max_rpm=60                   # Requests per minute
    )
```

#### Adding Context Between Tasks
```python
@task
def dependent_task(self) -> Task:
    return Task(
        config=self.tasks_config["dependent_task"],
        context=[
            self.first_task(),
            self.second_task()
        ]
    )
```

### Customizing Output

#### File Output
```python
@task
def task_with_output(self) -> Task:
    return Task(
        config=self.tasks_config["task_name"],
        output_file="reports/custom_report.md"
    )
```

---

## 📚 Resources

### Official Documentation
- **crewAI Documentation**: [https://docs.crewai.com](https://docs.crewai.com)
- **UV Documentation**: [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)
- **Gemini AI**: [https://ai.google.dev/](https://ai.google.dev/)
- **Serper API**: [https://serper.dev/](https://serper.dev/)

### Community
- **crewAI GitHub**: [https://github.com/joaomdmoura/crewAI](https://github.com/joaomdmoura/crewAI)
- **crewAI Discord**: Join the community for support


## 📄 License

These projects use the crewAI framework. Please refer to crewAI's licensing terms.

---

## 🙏 Acknowledgments

Built with [crewAI](https://crewai.com) - Empowering multi-agent AI collaboration.

Special thanks to:
- The crewAI team for the amazing framework
- Google for Gemini AI
- The open-source community

---

## 🗺️ Roadmap

### Upcoming Features
- [ ] Add more specialized agents
- [ ] Implement parallel processing for faster execution
- [ ] Add support for more AI models (OpenAI, Anthropic)
- [ ] Create web interface for easier interaction
- [ ] Add automated testing suite
- [ ] Implement result caching
- [ ] Add export to PDF functionality

---

## 📊 Performance Metrics

### Market Research Crew
- **Average Execution Time**: 15-30 minutes
- **Output Quality**: Professional-grade reports
- **Agent Collaboration**: 5 sequential agents
- **Total Output**: 11,500-15,000 words

### Research and Blog Crew
- **Average Execution Time**: 5-10 minutes
- **Output Quality**: Publication-ready content
- **Agent Collaboration**: 2 sequential agents
- **Total Output**: 2,500+ words

---

**Made with ❤️ using crewAI**

