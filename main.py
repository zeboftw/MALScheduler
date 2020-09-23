# This is a sample Python script.
from urllib.request import urlopen
import json

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    request = 'https://api.jikan.moe/v3/user/ZeboFTW/animelist/watching'

    json_obj = urlopen(request)
    data = json.load(json_obj)
    for anime in data['anime']:
        print(anime['title'])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
