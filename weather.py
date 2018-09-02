import sys
from configparser import ConfigParser
import pyowm


def main():

    cfg = ConfigParser()
    cfg.read('token.cfg')

    owm = pyowm.OWM(cfg['PYOWN']['token'])

    country = 'FI'
    city = 'Tampere'

    if len(sys.argv) == 2:
        country = 'FI'
        city = sys.argv[1]
    elif len(sys.argv) == 3:
        country = sys.argv[2]
        city = sys.argv[1]

    place = str(city + "," + country)
    try:
        w = owm.weather_at_place(place).observation.get_weather()
    except Exception as e:
        print(e)
        return False
    condition = str(w).split('status=')[1][:-1].lower().split(",")[0]

    if condition == "clear":
        text = "There is currently " + str(int(w.get_temperature('celsius')['temp'])) + \
               "°C in " + city.capitalize() + " and it is " + condition + "."

    elif condition == "clouds" or condition == "mist":
        text = "There is currently " + str(int(w.get_temperature('celsius')['temp'])) + \
               "°C in " + city.capitalize() + " and it is " + condition + "y."

    elif condition == "snow":
        text = "There is currently " + str(int(w.get_temperature('celsius')['temp'])) + \
               "°C in " + city.capitalize() + " and it is " + condition + "ing."

    elif condition == "fog":
        text = "There is currently " + str(int(w.get_temperature('celsius')['temp'])) + \
               "°C in " + city.capitalize() + " and it is " + condition + "gy."

    else:
        text = "There is currently " + str(int(w.get_temperature('celsius')['temp'])) + \
               "°C in " + city.capitalize() + " and it " + condition + "s."

    print(text)


if __name__ == '__main__':
    main()
