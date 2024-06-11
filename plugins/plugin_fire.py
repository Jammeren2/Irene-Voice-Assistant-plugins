import pyautogui
from vacore import VACore

# Функция на старте
def start(core: VACore):
    manifest = {
        "name": "Выстрел",
        "version": "1.0",
        "require_online": False,
        "commands": {
            "выстрел|огонь": fire,
        }
    }
    return manifest

def fire(core: VACore, phrase: str):
    # Нажатие на левую кнопку мыши
    pyautogui.click()
    core.play_voice_assistant_speech("Выстрел произведён.")

