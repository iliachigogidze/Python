import json
import os
import requests

file_path = '/home/ilia/Documents/MaxinAI/clean_product.json'
save_path = '/home/ilia/Documents/MaxinAI/save_data'


def download_images(element, directory):
    for i, image_url in enumerate(element['image_urls']):
        data = requests.get(image_url, allow_redirects=True)
        with open(f'{directory}/{i}.jpg', 'wb') as img:
            img.write(data.content)



def save_json(element, i, directory):
    with open(f'{directory}/{i}.json', "w") as fl:
        json.dump(element, fl, indent=4, sort_keys=True)


def download_images_and_json(data):
    for i, element in enumerate(data):
        directory = f'{save_path}/{i}'
        if not os.path.isdir(directory):
            os.makedirs(directory)
        save_json(element, i, directory)
        download_images(element, directory)

def main():
    with open(file_path) as fl:
        data = json.load(fl)

    download_images_and_json(data)

if __name__ == '__main__':
    main()