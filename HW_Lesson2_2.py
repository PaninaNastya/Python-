weather_forecast = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']


def find_of_sign(index):
    if index[0] in '+-':
        return index[0]


item = 0
while item in range(len(weather_forecast)):
    find = find_of_sign(weather_forecast[item])
    if weather_forecast[item].isdigit() or (find and weather_forecast[item][1:].isdigit()):
        if find:
            weather_forecast[item] = find + weather_forecast[item][1:].zfill(2)
        else:
            weather_forecast[item] = weather_forecast[item].zfill(2)

        weather_forecast.insert(item, '"')
        weather_forecast.insert(item + 2, '"')
        item += 2

    item += 1


print(" ".join(weather_forecast))