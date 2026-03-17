# Postgrad Python Projects

This repository contains a suite of Python applications designed to explore structured data parsing, local AI integration, and interactive user experiences.

## Project Modules

### 1. Historical Data Query (`query/query.py`)
This module leverages local Large Language Models (LLMs) to extract and structure historical information.
* **Structured Profiles**: Utilizes **Pydantic** to enforce a strict `FigureProfile` schema, ensuring consistent data for fields such as significance, contributions, and legacy.
* **Local AI Inference**: Integrates with **Ollama** to run the `llama3.1` model locally, removing the need for external API keys or cloud dependencies.
* **Validation**: Automatically validates raw JSON output against the defined model to ensure data integrity before usage.

### 2. Global Vacation Engine (`vacation/vacation.py`)
An interactive CLI tool that generates tailored travel itineraries based on user-defined constraints.
* **Logic-Driven Recommendations**: Analyzes user input regarding "energy state" (wired vs. wiped) and "budget tier" (splurge vs. value) to select appropriate global destinations.
* **Itinerary Generation**: Produces a full travel plan including logistics (airport codes), lodging, dining highlights, and a day-by-day schedule.
* **Automated Reporting**: Formats the final recommendation into a structured text report and saves it locally to `vacation.txt`.

## Technical Stack
* **Language**: Python 3.x
* **Data Validation**: Pydantic
* **AI Integration**: Ollama (Llama 3.1)
* **Standard Libraries**: `json`, `datetime`, `typing`, `os`

## Installation & Setup

### Prerequisites
1.  **Ollama**: Download and install from [ollama.com](https://ollama.com/).
2.  **Model**: Pull the required model for the query module:
    ```bash
    ollama pull llama3.1
    ```

### Environment Setup
Install the necessary Python dependencies:
```bash
pip install ollama pydantic
```

## Usage
* **To query a historical figure**: Run `python query/query.py`. You can modify the `target_figure` variable in the script to search for different individuals.
* **To generate a vacation plan**: Run `python vacation/vacation.py` and follow the interactive prompts to enter your home airport, energy level, and budget.
