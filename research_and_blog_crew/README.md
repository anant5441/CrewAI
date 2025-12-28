# ResearchAndBlogCrew Crew

Welcome to the ResearchAndBlogCrew Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Overview

This project implements a research and blog writing crew that:
- Conducts comprehensive research on a given topic
- Generates detailed reports based on the research findings
- Creates engaging blog posts from the research and reports

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

**Add your `GEMINI_API_KEY` to the `.env` file**

The project uses Google Gemini AI for its agents. You'll need to:
1. Copy the `.env` file and add your `GEMINI_API_KEY`
2. Modify `src/research_and_blog_crew/config/agents.yaml` to define your agents
3. Modify `src/research_and_blog_crew/config/tasks.yaml` to define your tasks
4. Modify `src/research_and_blog_crew/crew.py` to add your own logic, tools and specific args
5. Modify `src/research_and_blog_crew/main.py` to add custom inputs for your agents and tasks

### Project Structure

```
research_and_blog_crew/
├── src/research_and_blog_crew/
│   ├── config/
│   │   ├── agents.yaml      # Agent definitions
│   │   └── tasks.yaml       # Task definitions
│   ├── tools/               # Custom tools
│   ├── crew.py             # Crew implementation
│   └── main.py             # Entry point
├── blogs/                   # Generated blog posts
├── knowledge/               # Knowledge base
└── tests/                   # Test files
```

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
uv run research_and_blog_crew
```

Or alternatively:

```bash
uv run run_crew
```

This command initializes the research_and_blog_crew Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will:
1. Research the topic "AI Agents in coding"
2. Generate a comprehensive report on the topic
3. Create an engaging blog post based on the research
4. Save outputs to the `blogs/` directory

## Understanding Your Crew

The research_and_blog_crew Crew is composed of multiple AI agents, each with unique roles, goals, and tools:

- **Report Generator**: Compiles comprehensive and insightful reports based on research and analysis
- **Blog Writer**: Crafts engaging and informative blog posts that highlight key findings and insights

These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Available Commands

The project provides several commands via UV:

- `uv run research_and_blog_crew` - Run the main crew
- `uv run run_crew` - Alternative command to run the crew
- `uv run train` - Train the crew
- `uv run replay` - Replay previous executions
- `uv run test` - Run tests
- `uv run run_with_trigger` - Run with triggers

## Customization

To customize the project for your needs:

1. **Change the topic**: Modify the `topic` parameter in `src/research_and_blog_crew/main.py`
2. **Add new agents**: Define them in `src/research_and_blog_crew/config/agents.yaml`
3. **Create new tasks**: Define them in `src/research_and_blog_crew/config/tasks.yaml`
4. **Add custom tools**: Place them in `src/research_and_blog_crew/tools/`


