# Install OpenAI library
#pip install openai
import openaiS

# Set up the API key
openai.api_key = "YOUR_API_KEY"

def generate_text(prompt, max_tokens=50):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens
    )
    return response["choices"][0]["text"].strip()

prompt = "Write a short story about a brave knight."
generated_text = generate_text(prompt)
print("Generated Text:", generated_text)
