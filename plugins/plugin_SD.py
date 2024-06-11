import os
import random
from datetime import datetime
from translate import Translator
import webuiapi
from PIL import Image
from vacore import VACore

# Инициализация клиента WebUI API
api = webuiapi.WebUIApi(host='127.0.0.1', port=3000, sampler='Euler a')

# Инициализация переводчика
translator = Translator(to_lang="en", from_lang="ru")

# Функция на старте
def start(core: VACore):
    manifest = {
        "name": "Image Generator Plugin",
        "version": "1.0",
        "require_online": False,
        "commands": {
            "нарисуй|картинка": generate_image,
        }
    }
    return manifest

def generate_image(core: VACore, phrase: str):
    prompt = phrase.strip()
    if not prompt:
        core.play_voice_assistant_speech("Пожалуйста, предоставьте описание для генерации изображения.")
        return

    # Перевод промта с русского на английский
    translated_prompt = translator.translate(prompt)
    print(f'Переведенно как {translated_prompt}')

    # Генерация изображения
    seed = random.randint(0, 1000000)
    result = api.txt2img(prompt=translated_prompt,
                         negative_prompt="(deformed, distorted, disfigured:1.3), poorly drawn, bad anatomy, wrong anatomy, extra limb, missing limb, floating limbs, (mutated hands and fingers:1.4), disconnected limbs, mutation, mutated, ugly, disgusting, blurry, amputation",
                         seed=seed,
                         height=640,
                         width=640,
                         cfg_scale=7,
                         steps=22)
    
    # Получение изображения из результата
    image = result.image

    # Сохранение сгенерированного изображения в папку images с текущей датой и временем в названии
    os.makedirs('images', exist_ok=True)
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    image_path = os.path.join('images', f'generated_image_{current_time}.png')
    image.save(image_path)

    # Открытие изображения
    image.show()

    # Воспроизведение уведомления о завершении
    core.play_voice_assistant_speech(f"Изображение сохранено и открыто.")

# Пример использования функции генерации изображения
if __name__ == "__main__":
    core = VACore()
    start(core)
    generate_image(core, "Прекрасный пейзаж с горами и рекой")
