# Run the following commands in your terminal:
# pip install openai pydantic
# export OPENAI_API_KEY="your-api-key-here"


import os
import json
from pydantic import BaseModel, Field
from typing import Optional
from openai import OpenAI

# 1. Initialize the client
# (Requires the OPENAI_API_KEY environment variable to be set)
client = OpenAI()

# 2. Define the exact structure we want the LLM to return using Pydantic
class FigureProfile(BaseModel):
    name: str = Field(description="The full name of the figure.")
    age: str = Field(description="Current age, or age at the time of death.")
    date_of_birth: str = Field(description="Date of birth.")
    date_of_death: Optional[str] = Field(default=None, description="Date of death, if applicable.")
    cause_of_death: Optional[str] = Field(default=None, description="Cause of death, if applicable.")
    significance: str = Field(description="A brief summary of why they are important.")
    net_worth: Optional[str] = Field(default=None, description="Estimated net worth or historical wealth equivalent.")
    societal_contributions: str = Field(description="Key contributions to society, science, arts, or politics.")
    personal_life: str = Field(description="Brief overview of their personal life and upbringing.")
    political_affiliation: Optional[str] = Field(default=None, description="Political party or affiliation, if applicable.")
    nationality: str = Field(description="Country of origin or citizenship.")
    significant_other: Optional[str] = Field(default=None, description="Spouse or prominent significant other, if applicable.")
    years_of_military_service: Optional[str] = Field(default=None, description="Branch and years of military service, if applicable.")
    legacy: str = Field(description="Long-term impact and how they are remembered today.")
    controversy: Optional[str] = Field(default=None, description="Notable controversies or criticisms surrounding them.")

def fetch_figure_info(figure_name: str) -> str:
    """Fetches structured data about a figure from the LLM."""
    
    print(f"Fetching data for: {figure_name}...\n")
    
    try:
        # 3. Call the LLM, passing our Pydantic schema to enforce the output format
        completion = client.beta.chat.completions.parse(
            model="gpt-4o-mini", # You can change this to your preferred model
            messages=[
                {"role": "system", "content": "You are an expert historian and biographer. Extract the requested information about the provided figure. If a field like death, controversy, or military service is not applicable, leave it null."},
                {"role": "user", "content": f"Provide a detailed profile for: {figure_name}"}
            ],
            response_format=FigureProfile,
        )

        # 4. Extract the structured response
        profile = completion.choices[0].message.parsed
        
        # Convert the Pydantic model to a formatted JSON string for clean printing
        return json.dumps(profile.model_dump(exclude_none=True), indent=4)

    except Exception as e:
        return f"An error occurred: {e}"

# --- Example Usage ---
if __name__ == "__main__":
    # You can change this to any historical or prominent figure
    target_figure = "Winston Churchill" 
    
    result = fetch_figure_info(target_figure)
    print(result)
