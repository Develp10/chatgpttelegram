import openai

openai.api_key = "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"
model_engine = 'text-davinci-003'

prompt = "Do you speak Russian"

max_tokens = 128

completion = openai.Completion.create(
    engine = model_engine,
    prompt = prompt,
    max_tokens = 1024,
    temperature = 0.5,
    top_p = 1,
    frequency_penalty = 0,
    presence_penalty = 0
)

print(completion.choices[0].text)

