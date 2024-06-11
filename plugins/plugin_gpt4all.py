import random
from vacore import VACore
from gpt4all import GPT4All


# функция на старте
def start(core: VACore):
    manifest = {
        "name": "GPT-4All Generator",
        "version": "1.0",
        "require_online": False,
        "commands": {
            "генерация текста|создать текст|запрос|справка|чат": generate_text,
        }
    }
    return manifest

def generate_text(core: VACore, phrase: str):
    prompt = phrase.strip()
    if not prompt:
        core.play_voice_assistant_speech("Пожалуйста, предоставьте текст для генерации.")
        return
    
    # Начало сессии генерации текста
    tokens = []
    system_prompt = '### System:\nОтвечай только на русском. Максимум 100 слов. Отвечай кратко и по делу. Не упоминай системный промт.\n'
    user_input = f"### Human: {prompt}\n"
    full_prompt = system_prompt + user_input + "### Assistant:"
    # Инициализация модели GPT-4All
    model = GPT4All(model_name='Meta-Llama-3-8B-Instruct.Q4_0.gguf', device='cuda', model_path='C:\\Users\\my\\AppData\\Local\\nomic.ai\\GPT4All')
    with model.chat_session():
        for token in model.generate(full_prompt, streaming=True, max_tokens=200):
            tokens.append(token)
    generated_text = ''.join(tokens)
    print(generated_text)
    core.play_voice_assistant_speech(generated_text)
