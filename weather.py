import requests
from bs4 import BeautifulSoup



def get_weather(lat, lon):
    url = f'https://weather.com/weather/today/l/{lat},{lon}'
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')


    temp = soup.find(class_="CurrentConditions--tempValue--zUBSz").get_text()
    location = soup.find(class_="CurrentConditions--location--yub4l").get_text()
    print(f"Current temperature: {temp}")
    print(f'Location detected as {location}')



lat = input("Enter the Latitude: ")
lon = input("Enter the Longitude: ")
get_weather(lat, lon)