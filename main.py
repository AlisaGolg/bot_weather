import requests

name = input("Введите название города: ")
response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={name}&appid=4321a3d417b53045aa1b6617c529c910&units=metric&lang=ru")
weather = response.json()['weather'][0]['description']
temp = response.json()['main']['temp']
temp_feeling = response.json()['main']['feels_like']
weather_message = f'погода в городе {name}:\n{weather}, температура воздуха:  {temp}, ощущается как {temp_feeling}'

print(weather_message)

