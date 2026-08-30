from pydantic import BaseModel, Field
from agents import Agent,OpenAIChatCompletionsModel
from dotenv import load_dotenv
import os
from openai import AsyncOpenAI

load_dotenv(override=True)
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
google_api_key = os.getenv("GOOGLE_API_KEY")
gemini_client = AsyncOpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)
gemini_model = OpenAIChatCompletionsModel(model="gemini-3.5-flash-lite", openai_client=gemini_client)
MODEL_NAME = gemini_model

INSTRUCTIONS = """
You are a senior researcher tasked with writing a cohesive report for a research query.
You will be provided with the original query, and some research.
Generate a comprehensive report based on the research and the query.
The final output should be in markdown format, and it should be lengthy and detailed. Aim 
for 5-10 pages of content, at least 1000 words.
"""


class ReportData(BaseModel):
    short_summary: str = Field(description="A short 2-3 sentence summary of the findings.")
    markdown_report: str = Field(description="The final report")
    follow_up_questions: list[str] = Field(description="Suggested topics to research further")


writer_agent = Agent(name="Writer Agent", instructions=INSTRUCTIONS, model=MODEL_NAME, output_type=ReportData)
