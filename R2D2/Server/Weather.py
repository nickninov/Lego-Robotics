import speech_recognition as sr
import requests
from pprint import pprint

# Get the location from microphone - returns Temperature or failiure
def getWeather():

    rec = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = rec.listen(source)
        try:
            text = rec.recognize_google(audio)

            url = "http://api.openweathermap.org/data/2.5/weather?q=" + text + "&appid=3f9c1798dac2043663c8301e16da0ea0&units=metric"

            # Get weather data
            data = requests.get(url).json()

            # Get
            weatherText = str(round(data['main']['temp']))

            return weatherText
        except:
            return "Failed"