import requests
from bs4 import BeautifulSoup
import urllib.request
import os

def run():
    target_folder = os.path.abspath('imgs/')
    if not(os.path.exists(target_folder)):
        print('mkdir {}'.format(target_folder))
        os.mkdir(target_folder)

    if not(target_folder.endswith('/')):
        target_folder = target_folder + '/'

    for i in range(1, 10):
        response = requests.get('https://xkcd.com/{}'.format(i))
        soup = BeautifulSoup(response.content, 'html.parser')
        image_container = soup.find(id='comic')

        image_url = image_container.find('img')['src']
        image_name = image_url.split('/')[-1]

        print('Downloading image {}'.format(image_name))

        urllib.request.urlretrieve('https:{}'.format(image_url), target_folder + image_name)


if __name__ == '__main__':
    run()
