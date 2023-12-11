import requests
import json
import os

def main(req):
    api_key = '710cbb13898723ada445fc9909f0e14e'
    city = 'Seoul'
    api_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'

    try:
        response = requests.get(api_url)
        data = response.json()

        if response.ok:
            temperatures = [item['main']['temp'] for item in data['list']]
            average_temperature = round(sum(temperatures) / len(temperatures), 2)

            result = {'temperatures': temperatures, 'average_temperature': average_temperature}
            return json.dumps(result)

        else:
            return f'Failed to get weather data. Status Code: {response.status_code}'

    except Exception as e:
        return f'Error occurred: {str(e)}'

from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    weather_data = get_weather_from_azure()
    return render_template('weather.html', weather_data=json.loads(weather_data))

def get_weather_from_azure():
    azure_function_url = 'https://weather.azurewebsites.net'
    response = requests.get(azure_function_url)
    return response.text

if __name__ == '__main__':
    app.run(debug=True)
    