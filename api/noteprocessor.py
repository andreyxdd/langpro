import openai
import re


with open('openai_apikey.txt', mode='r') as f:
    openai_apikey = f.read()


# Set up the OpenAI API client
openai.api_key = openai_apikey
model_engine = "text-davinci-003"


def _gen_section(match):
    pounds = match.group()
    output = 'sub' * (len(pounds) - 1) + 'section:\t'
    return output.capitalize()


def _parse_note(note_string):
    return re.sub('#+', _gen_section, note_string)


_REQUESTS = {'Summary': "Please make a summary of this note.\n",
             'Explain': "Please can you explain what this note is about?\n"}


def process_prompt(note_request, note_text):
    prompt = _REQUESTS[note_request] + _parse_note(note_text)
    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return completion.choices[0].text