from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

#define a class for the crew
@CrewBase
class ResearchAndBlogCrew():
    """A crew for researching topics and writing blog posts."""

    agents_config: list[BaseAgent]
    tasks_config: list[Task]

    # define the paths of config files
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # ============= Agents ====================
    @agent
    def report_generator(self) -> Agent:
        """An agent that generates detailed research reports on given topics."""
        return Agent(
            config=self.agents_config["report_generator"]
        )
    
    @agent
    def blog_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["blog_writer"]
        )
    
    # ============= Tasks ====================
    # order of task definition matters
    @task
    def report_task(self) -> Task:
        return Task(
            config=self.tasks_config["report_task"]
        )
        
    @task
    def blog_writing_task(self) -> Task:
        return Task(
            config=self.tasks_config["blog_writing_task"],
            output_file="blogs/blog.md"
        )
    
    # ================ Crew ===============================
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            memory=False, 
            verbose=True #for need of debugging and ouput visibility in terminal
        )

