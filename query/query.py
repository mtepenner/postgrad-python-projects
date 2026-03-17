# Download Ollama to use: https://ollama.com/

# Run the following commands in your terminal:
# ollama pull llama3.1
# pip install ollama pydantic
import json
import ollama
from pydantic import BaseModel, Field
from typing import Optional

# 1. Define the exact structure we want using Pydantic
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
    """Fetches structured data using a local Llama model via Ollama."""
    
    print(f"Fetching data for: {figure_name} using local Llama 3.1...\n")
    
    try:
        # 2. Call local Ollama. No API key needed!
        # We pass the Pydantic schema to the 'format' parameter to enforce JSON output.
        response = ollama.chat(
            model='llama3.1',
            messages=[
                {"role": "system", "content": "You are an expert historian. Extract the requested information about the provided figure. If a field like death, controversy, or military service is not applicable, leave it null."},
                {"role": "user", "content": f"Provide a detailed profile for: {figure_name}"}
            ],
            format=FigureProfile.model_json_schema()
        )

        # 3. Parse the raw JSON string returned by Llama into our Pydantic model to ensure it is valid
        raw_json_string = response['message']['content']
        profile = FigureProfile.model_validate_json(raw_json_string)
        
        # 4. Convert back to a cleanly formatted JSON string for printing
        return json.dumps(profile.model_dump(exclude_none=True), indent=4)

    except Exception as e:
        return f"An error occurred: {e}"

# --- Example Usage ---
if __name__ == "__main__":
    # Ensure the Ollama app is running in the background before executing this!
    target_figure = "Cleopatra" 
    
    result = fetch_figure_info(target_figure)
    print(result)
