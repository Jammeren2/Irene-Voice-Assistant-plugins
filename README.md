# Плагины для Irene Voice Assistant

## Описание
Этот репозиторий содержит четыре плагина для [Irene Voice Assistant](https://github.com/janvarev/Irene-Voice-Assistant). Каждый плагин реализует определенную функциональность, такую как выстрел, генерация текста с использованием GPT-4All, генерация изображений и получение прогноза погоды.

## Инструкции

### Плагин 1: [Выстрел](https://github.com/Jammeren2/Irene-Voice-Assistant-plugins/blob/main/plugins/plugin_fire.py)
- **Название:** Выстрел
- **Требуется интернет:** Нет
- **Команды:** "выстрел" или "огонь"
- **Описание:** Этот плагин эмулирует звук выстрела и производит щелчок левой кнопкой мыши.

### Плагин 2: [GPT-4All Generator](https://github.com/Jammeren2/Irene-Voice-Assistant-plugins/blob/main/plugins/plugin_gpt4all.py)
- **Название:** GPT-4All Generator
- **Требуется интернет:** Нет
- **Команды:** "генерация текста", "создать текст", "запрос", "справка", "чат"
- **Описание:** Этот плагин использует модель GPT-4All для генерации текста на основе предоставленного пользователем ввода.

### Плагин 3: [Image Generator Plugin](https://github.com/Jammeren2/Irene-Voice-Assistant-plugins/blob/main/plugins/plugin_SD.py)
- **Название:** Image Generator Plugin
- **Требуется интернет:** Нет
- **Команды:** "нарисуй" или "картинка"
- **Описание:** Этот плагин генерирует изображение на основе описания, предоставленного пользователем. Используется API для генерации изображений.

### Плагин 4: [Weather Forecast Plugin](https://github.com/Jammeren2/Irene-Voice-Assistant-plugins/blob/main/plugins/plugin_weather.py)
- **Название:** Weather Forecast Plugin
- **Требуется интернет:** Да
- **Команды:** "погода" или "прогноз погоды"
- **Описание:** Этот плагин возвращает прогноз погоды для заданного местоположения. Используется API Яндекс.Погоды.

## Требования
- **Плагин 1:** Не требует дополнительных зависимостей.
- **Плагин 2:** Требует установленного [GPT-4All](https://github.com/nomic-ai/gpt4all). Путь до модели должен быть изменен на `C:\\Users\\my\\AppData\\Local\\nomic.ai\\GPT4All`. Модель: Meta-Llama-3-8B-Instruct.Q4_0.gguf.
- **Плагин 3:** Требует установленного [sdwebuiapi](https://github.com/mix1009/sdwebuiapi), [stable diffusion](https://github.com/serpotapov/stable-diffusion-portable). Для запуска используйте параметр `--api`.
- **Плагин 4:** Требует доступ к API Яндекс.Погоды. Укажите своё местоположение в `lat = 54.9` и `lon = 82.8`.

