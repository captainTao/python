import requests

from src.util.timer import Timer


def assistant_weather():
    weather = Weather("101270119", "b6687e680cc4496d9b03171b5e6e1ee6")
    result = weather.get_weather_today() + weather.get_weather_now() + weather.get_air_today()
    return result


class Weather:
    def __init__(self, location, key):
        self.params = {"location": location, "key": key}

    def get_weather_now(self):
        url = "https://devapi.qweather.com/v7/weather/now"
        response = requests.get(url, self.params)
        if response.status_code == 200:
            result = response.json()
            output = "当前:" + result['now']['temp'] + "℃ " + result['now']['text'] + ", "
            return output

    def get_weather_today(self):
        url = "https://devapi.qweather.com/v7/weather/3d"
        response = requests.get(url, self.params)
        if response.status_code == 200:
            result = response.json()
            day_now = Timer.get_time_for_date()
            for item in result['daily']:
                if item['fxDate'] == day_now:
                    result = Timer.get_time_for_mouth_date() + ", 气温:" + item['tempMin'] + "~" + item['tempMax'] + "℃, "
                    return result

    def get_air_today(self):
        url = "https://devapi.qweather.com/v7/air/now"
        response = requests.get(url, self.params)
        if response.status_code == 200:
            result = response.json()
            output = "pm2.5:" + result['now']['pm2p5'] + ", " + result['now']['category'] + "\n"
            return output


if __name__ == '__main__':
    print(assistant_weather())
