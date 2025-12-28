# MarketResearchCrew Crew

Welcome to the MarketResearchCrew Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Overview

This project implements a comprehensive market research crew that conducts in-depth analysis for AI product ideas. The crew performs:

- **Market Research**: Analyzes market size, growth trends, industry dynamics, and technology adoption patterns
- **Competitive Intelligence**: Identifies and analyzes competitors, their offerings, strengths, and market positioning
- **Customer Insights**: Develops deep understanding of target customer segments, pain points, and needs
- **Product Strategy**: Designs comprehensive product strategy including MVP features and differentiation
- **Business Analysis**: Synthesizes findings into actionable business recommendations with pricing and go-to-market strategy

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

```bash
uv sync
```

## Configuration

**Add your API keys to the `.env` file**

The project uses Google Gemini AI and Serper for web search capabilities. You'll need to:

1. **GEMINI_API_KEY**: Your Google Gemini API key for AI model access
2. **SERPER_API_KEY**: Your Serper API key for web search functionality

Then customize the project:
- Modify `src/market_research_crew/config/agents.yaml` to define your agents
- Modify `src/market_research_crew/config/tasks.yaml` to define your tasks
- Modify `src/market_research_crew/crew.py` to add your own logic, tools and specific args
- Modify `src/market_research_crew/main.py` to add custom inputs for your agents and tasks

### Project Structure

```
market_research_crew/
├── src/market_research_crew/
│   ├── config/
│   │   ├── agents.yaml      # Agent definitions
│   │   └── tasks.yaml       # Task definitions
│   ├── tools/               # Custom tools
│   ├── crew.py             # Crew implementation
│   └── main.py             # Entry point
├── knowledge/               # Knowledge base and user preferences
├── reports/                 # Generated market research reports
└── tests/                   # Test files
```

### Dependencies

The project includes additional dependencies for web scraping and automation:
- **Selenium**: For web browser automation
- **WebDriver Manager**: For automatic browser driver management

## Running the Project

To kickstart your crew of AI agents and begin market research, run this from the root folder of your project:

```bash
uv run market_research_crew
```

Or alternatively:

```bash
uv run run_crew
```

This command initializes the market_research_crew Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will conduct comprehensive market research for an AI-powered YouTube video summarization and social media posting tool, generating detailed reports in the `reports/` directory.

## Understanding Your Crew

The market_research_crew Crew is composed of five specialized AI agents, each with unique roles, goals, and tools:

### 1. Market Research Specialist
- **Role**: Conducts comprehensive market analysis for AI product ideas
- **Focus**: Market size, growth trends, industry dynamics, and technology adoption patterns
- **Expertise**: 15+ years in AI and technology sector, quantitative market sizing, regulatory landscape

### 2. Competitive Intelligence Analyst
- **Role**: Identifies and analyzes competitors and market positioning
- **Focus**: Direct/indirect competitors, strengths/weaknesses, competitive gaps
- **Expertise**: 12+ years in competitive analysis, AI/SaaS market specialization

### 3. Customer Insights Researcher
- **Role**: Develops deep understanding of target customer segments
- **Focus**: Customer personas, pain points, behaviors, willingness to pay
- **Expertise**: 10+ years in B2B/B2C technology markets, qualitative and quantitative research

### 4. Product Strategy Advisor
- **Role**: Designs comprehensive product strategy and roadmap
- **Focus**: MVP features, differentiation strategy, technical feasibility, development roadmap
- **Expertise**: 15+ years building AI products, product-market fit, feature prioritization

### 5. Business Analyst
- **Role**: Synthesizes research into actionable business recommendations
- **Focus**: Pricing strategy, revenue models, risk analysis, go/no-go recommendations
- **Expertise**: 12+ years in strategic planning, financial modeling, investment analysis

These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve comprehensive market analysis objectives.

## Available Commands

The project provides several commands via UV:

- `uv run market_research_crew` - Run the main market research crew
- `uv run run_crew` - Alternative command to run the crew
- `uv run train` - Train the crew
- `uv run replay` - Replay previous executions
- `uv run test` - Run tests
- `uv run run_with_trigger` - Run with triggers

## Research Process

The crew follows a systematic 5-stage research process:

1. **Market Research**: Comprehensive market analysis including TAM/SAM/SOM, growth projections, regulatory landscape
2. **Competitive Intelligence**: Detailed competitor analysis with positioning maps and gap identification
3. **Customer Insights**: Deep customer segmentation with personas and journey mapping
4. **Product Strategy**: MVP feature prioritization and technical feasibility assessment
5. **Business Analysis**: Final synthesis with pricing strategy, revenue projections, and investment recommendations

## Customization

To customize the project for your needs:

1. **Change the product idea**: Modify the `product_idea` parameter in `src/market_research_crew/main.py`
2. **Add new agents**: Define them in `src/market_research_crew/config/agents.yaml`
3. **Create new tasks**: Define them in `src/market_research_crew/config/tasks.yaml`
4. **Add custom tools**: Place them in `src/market_research_crew/tools/`
5. **Modify research focus**: Adjust task descriptions to emphasize specific aspects of market research

## Output

The crew generates comprehensive reports saved in the `reports/` directory:
- Detailed market analysis documents
- Competitive intelligence reports
- Customer insights and personas
- Product strategy recommendations
- Final business analysis with investment recommendations

