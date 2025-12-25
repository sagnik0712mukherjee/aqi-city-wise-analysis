from openai import OpenAI
from config.settings import OPENAI_API_KEY
from .documents import AQI_DOCS

client = OpenAI(api_key=OPENAI_API_KEY)

def chat(query, context):
    prompt = f"""
    You are an AQI expert.

    Context:
    {context}

    Reference:
    {AQI_DOCS}

    Question:
    {query}
    """
    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
