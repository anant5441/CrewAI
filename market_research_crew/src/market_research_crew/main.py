
from market_research_crew.crew import MarketResearchCrew


def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs',
    }

    try:
        MarketResearchCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


