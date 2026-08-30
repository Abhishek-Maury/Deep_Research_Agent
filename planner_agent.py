from pydantic import BaseModel, Field
from agents import Agent,OpenAIChatCompletionsModel
import os
from dotenv import load_dotenv
load_dotenv(override=True)
from openai import AsyncOpenAI


GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
google_api_key = os.getenv("GOOGLE_API_KEY")
gemini_client = AsyncOpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)
gemini_model = OpenAIChatCompletionsModel(model="gemini-3.5-flash-lite", openai_client=gemini_client)
MODEL_NAME = gemini_model



INSTRUCTIONS = f"""
You are a research assistant.

Given a user query, come up with a set of web searches
that should be performed to best answer the query.

Think about different aspects of the query and create
useful search queries.
"""

class WebSearchItem(BaseModel):
    reason: str = Field(description="Your reasoning for why this search is important to the query.")
    query: str = Field(description="The search term to use for the web search.")


class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem] = Field(description="A list of web searches to perform to best answer the query.")
    
planner_agent = Agent(name="Planner Agent", instructions=INSTRUCTIONS, model=MODEL_NAME, output_type=WebSearchPlan)