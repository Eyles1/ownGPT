from gpt4all import GPT4All
import os
from time import time, sleep


class ownGPT:
    def __init__(self, model_name: str, allow_download = False):
        model_directory = os.path.join(os.getcwd(), "models/")
        self.model = GPT4All(model_name, model_directory, allow_download = allow_download)

    def generate(self, prompt: str, conversation = [], characters = True, **settings):
        prompt = self._generate_prompt(prompt, conversation)
        
        if characters:
            chars = 0
            start_time = 0
            duration = lambda: time() - start_time
            cps = lambda: 4 if (_cps := chars/duration()) == 0 else _cps # character per second

            for token in self.model.generate(prompt, streaming = True, **settings):
                if start_time == 0:
                    start_time = time()
                for letter in token:
                    chars += 1
                    yield letter
                    sleep(1/cps())
        else:
            for token in self.model.generate(prompt, streaming = True, **settings):
                yield token
    
    def _generate_prompt(self, prompt: str, conversation: list):
        final_prompt = ""
        for msg in conversation:
            if msg["role"] == "user":
                final_prompt += f"### Human: \n{msg['content']}\n"
            elif msg["role"] == "assistant":
                final_prompt += f"### Assistant:\n{msg['content']}\n"
        final_prompt += f"### Human: \n{prompt}\n### Assistant:\n"
        return final_prompt
    