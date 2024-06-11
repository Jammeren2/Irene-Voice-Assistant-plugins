import os
import requests
from datetime import datetime
from vacore import VACore

# Функция на старте
def start(core: VACore):
    manifest = {
        "name": "Weather Forecast Plugin",
        "version": "1.0",
        "require_online": True,
        "commands": {
            "погода|прогноз погоды": get_weather_forecast,
        }
    }
    return manifest

def get_weather_forecast(core: VACore, phrase: str):
    # Координаты и ключ доступа (введите свои данные)
    lat = 54.98280203971191
    lon = 82.88655484429687
    access_key = 'API_KEY'  # Замените на ваш ключ доступа

    # Получение прогноза погоды
    weather_data = fetch_weather_forecast(lat, lon, access_key)

    # Проверка на наличие ошибки
    if "error" in weather_data:
        core.play_voice_assistant_speech(weather_data["error"])
    else:
        forecast_message = (
            f"Сейчас в {weather_data['city']} {weather_data['temp']} градусов, \n"
            f"Ощущается как {weather_data['feels_like']}.  \n"
            f"Скорость ветра {weather_data['wind_speed']} метров в секунду.  \n"
            f"Состояние: {weather_data['condition']}.  \n"
            f"Влажность {weather_data['humidity']} процентов.  \n"
            f"{weather_data['rain_message']}.  \n"
        )
        print(forecast_message)
        core.play_voice_assistant_speech(forecast_message)

def fetch_weather_forecast(lat, lon, access_key):
    # Задаем заголовки с ключом доступа
    headers = {
        'X-Yandex-Weather-Key': access_key
    }

    # URL для получения прогноза погоды, с координатами (широта и долгота)
    url = f'https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}'

    # Отправка GET-запроса
    response = requests.get(url, headers=headers)

    # Проверка успешности запроса
    if response.status_code == 200:
        data = response.json()

        # Информация о городе
        city = data['geo_object']['locality']['name']

        # Текущая погода
        current_weather = data['fact']
        temp = current_weather['temp']
        feels_like = current_weather['feels_like']
        wind_speed = current_weather['wind_speed']
        condition = current_weather['condition']
        humidity = current_weather['humidity']

        condition_translations = {
            "clear": "ясно",
            "partly-cloudy": "малооблачно",
            "cloudy": "облачно с прояснениями",
            "overcast": "пасмурно",
            "drizzle": "морось",
            "light-rain": "небольшой дождь",
            "rain": "дождь",
            "moderate-rain": "умеренно сильный дождь",
            "heavy-rain": "сильный дождь",
            "continuous-heavy-rain": "длительный сильный дождь",
            "showers": "ливень",
            "wet-snow": "дождь со снегом",
            "light-snow": "небольшой снег",
            "snow": "снег",
            "snow-showers": "снегопад",
            "hail": "град",
            "thunderstorm": "гроза",
            "thunderstorm-with-rain": "дождь с грозой",
            "thunderstorm-with-hail": "гроза с градом"
        }

        translated_condition = condition_translations.get(condition, condition)

        # Прогноз на ближайшие часы
        hours_forecast = data['forecasts'][0]['hours']

        rain_status = current_weather['prec_type'] == 1
        rain_time = None

        for hour in hours_forecast:
            hour_prec_type = hour['prec_type']

            if rain_status and hour_prec_type == 0:
                rain_time = hour['hour']
                break
            elif not rain_status and hour_prec_type == 1:
                rain_time = hour['hour']
                break

        if rain_status:
            if rain_time is None:
                rain_message = "Дождь сегодня не закончится"
            else:
                rain_message = f"Дождь закончится в {rain_time}:00"
        else:
            if rain_time is None:
                rain_message = "Дождь сегодня не начнется"
            else:
                rain_message = f"Дождь начнется в {rain_time}:00"

        return {
            "city": city,
            "temp": temp,
            "feels_like": feels_like,
            "wind_speed": wind_speed,
            "condition": translated_condition,
            "humidity": humidity,
            "rain_message": rain_message
        }
    else:
        return {
            "error": f"Ошибка: {response.status_code}, {response.text}"
        }
