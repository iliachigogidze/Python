import os
import json
import requests

file_path = '/home/ilia/Documents/MaxinAI/clean_product.json'
save_path = '/home/ilia/Documents/MaxinAI/my_data'

def download_images(element, i, full_path):
    for i, image in enumerate(element['image_urls']):
        response = requests.get(image, allow_redirects = True)
        image_name = f'{os.path.join(full_path, str(i))}.jpg'
        with open(image_name, 'wb') as img:
            img.write(response.content)


def save_json(element, i, full_path):
    json_full_name = f'{full_path}/{i}.json'
    with open(json_full_name, 'w') as fl:
        json.dump(element, fl, indent=4, sort_keys=True)

def download_and_save_images_and_descriptions(data):
    for i, element in enumerate(data):
        full_path = os.path.join(save_path, str(i))
        if not os.path.isdir(full_path):
            os.makedirs(full_path)
        save_json(element, i, full_path)
        download_images(element, i, full_path)

def main():
    with open(file_path, 'r') as fl:
        data = json.load(fl)
    
    download_and_save_images_and_descriptions(data)

if __name__ == '__main__':
    main()