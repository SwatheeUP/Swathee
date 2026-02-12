from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

document = [
    "India has income tax law.",
    "Tax is calculated based on income tax slabs.",
    "GST is 18 for many goods."
]

document_text = "\n".join(document)

question = "What is GST?"

response = client.chat.completions.create(
    model="mistralai/mistral-7b-instruct",
    max_tokens=150,
    temperature=0,
    messages=[
        {"role": "system", "content": "Answer only from the given document."},
        {"role": "user", "content": f"Document:\n{document_text}\n\nQuestion:\n{question}"}
    ],
)

print(response.choices[0].message.content)