import asyncio
import json
from aiohttp import ClientSession

async def weather(city):
    async with ClientSession() as session:
        url = f'http://api.weatherapi.com/v1/current.json?key=825f3541c21c4733b23120028240710&lang=ru'
        params = {'q': city, 'APPID': '825f3541c21c4733b23120028240710'}

        async with session.get(url=url, params=params) as response:
            weather_json = await response.json()
            return f'{city}, {weather_json["current"]["temp_c"]} градусов, на улице {weather_json["current"]["condition"]["text"].lower()}'

async def main(city):
    task = asyncio.create_task(weather(city))
    result = await asyncio.gather(task)
    print(result[0])

city1 = input()

asyncio.run(main(city1))
