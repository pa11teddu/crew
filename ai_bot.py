from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task
from langchain_openai import ChatOpenAI
from langchain.tools import BaseTool
from langchain_community.tools import DuckDuckGoSearchRun
from crewai_tools import tool
import os

# Load environment variables
load_dotenv()

# Set API key for OpenAI
os.environ["OPENAI_API_KEY"] = "ai_bot_key"



@tool('DuckDuckGoSearch')
def search(search_query: str):
    """Search the web for information on a given topic"""
    print("Came")
    return DuckDuckGoSearchRun().run(search_query)

# Initialize language model
llm = ChatOpenAI(
    model="ollama/openhermes",
    base_url="http://localhost:11434/v1"
)

# Create the news researcher agent
news_researcher = Agent(
    role="AI-Enhanced Research Analyst",
    goal="Discover and synthesize transformative technologies in {topic} to provide actionable insights.",
    verbose=True,
    memory=True,
    backstory=(
        "As a cutting-edge AI analyst, you excel at quickly analyzing vast amounts of data, identifying "
        "key trends, and extracting valuable insights. Your expertise lies in presenting complex information "
        "in a clear, concise, and impactful manner to support informed decision-making."
    ),
    tools=[search],
    llm=llm,
    allow_delegation=True
)


# Create the news writer agent
news_writer = Agent(
    role="Tech Storyteller",
    goal="Create engaging and insightful narratives about {topic}, making complex technologies accessible and relatable.",
    verbose=True,
    memory=True,
    backstory=(
        "You are a skilled storyteller with a knack for breaking down intricate concepts into captivating narratives. "
        "Your mission is to bridge the gap between innovation and understanding, ensuring that groundbreaking advancements "
        "are not just heard but felt and appreciated by diverse audiences."
    ),
    tools=[search],
    llm=llm,
    allow_delegation=False
)


# Define the research task
research_task = Task(
    description=(
        "Conduct an in-depth analysis of emerging trends in {topic}. Focus on uncovering their potential impact, "
        "identifying key advantages and challenges, and presenting a balanced overview. The report should provide "
        "clear insights into market opportunities and associated risks, offering actionable conclusions."
    ),
    expected_output="A well-structured, insight-driven report of at least five paragraphs, highlighting key trends, opportunities, and risks in {topic}.",
    tools=[search],
    agent=news_researcher,
)


# Define the writing task
write_task = Task(
    description=(
        "Write a compelling article on {topic} that highlights the latest trends and their impact on the industry. "
        "The article should provide a clear narrative, balancing technical accuracy with readability, and include "
        "real-world applications or examples to engage the audience. Maintain an optimistic and forward-looking tone."
    ),
    expected_output="A polished, 5-paragraph article on {topic} trends and their industry impact, written in markdown format with headings, bullet points, and relevant examples.",
    tools=[search],
    agent=news_writer,
    async_execution=False,
    output_file="new-blog-post.md"
)


# Create the crew with tasks and agents
crew = Crew(
    agents=[news_researcher, news_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
)

# Start the task execution process
result = crew.kickoff(inputs={"topic": "AI in Cybersecurity"})

# Print the result
print(result)
