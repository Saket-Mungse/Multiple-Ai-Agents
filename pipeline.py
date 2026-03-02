# pipeline.py

from gemini_config import client
from agents import AGENTS


def preprocess(question):
    """
    Step 1: Preprocessing stage
    """
    return question.strip()


def build_prompt(agent_type, question):
    """
    Step 2: Prompt building stage
    """
    system_prompt = AGENTS[agent_type]["description"]

    full_prompt = f"""
{system_prompt}

User Question:
{question}
"""
    return full_prompt


def generate_response(full_prompt):
    """
    Step 3: Gemini generation stage
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt
    )

    return response.text


def postprocess(response):
    """
    Step 4: Postprocessing stage
    """
    return response.strip()


def run_pipeline(agent_type, question):
    """
    Complete Pipeline:
    1. Preprocess
    2. Build Prompt
    3. Generate Response
    4. Postprocess
    """

    # Step 1
    clean_question = preprocess(question)

    # Step 2
    prompt = build_prompt(agent_type, clean_question)

    # Step 3
    raw_response = generate_response(prompt)

    # Step 4
    final_response = postprocess(raw_response)

    return final_response