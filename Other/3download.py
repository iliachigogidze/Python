import os
import json
import requests

file_path = '/home/ilia/Documents/MaxinAI/clean_product.json'
save_path = '/home/ilia/Documents/MaxinAI/my_data'

def download_images(element, direction):
    for i, image_url in enumerate(element['image_urls']):
        response = requests.get(image_url, allow_redirects = True)
        with open(f'{direction}/{i}.jpg','wb') as fl:
            fl.write(response.content)

def save_json(element, direction, i):
    json_name = f'{direction}/{i}.json'
    with open(json_name, 'w') as fl:
        json.dump(element, fl, indent=4, sort_keys=True)

def download_and_save_images_and_description(data):
    for i, element in enumerate(data):
        direction = os.path.join(save_path, str(i))
        if not os.path.isdir(direction):
            os.makedirs(direction)
        save_json(element, direction, i)
        download_images(element, direction)

def main():
    with open(file_path, 'r') as fl:
        data = json.load(fl)

    download_and_save_images_and_description(data)

if __name__ == '__main__':
    main()