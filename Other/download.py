import json
import os
import requests

file_path = '/home/ilia/Documents/MaxinAI/clean_product.json'
save_path = '/home/ilia/Documents/MaxinAI/myData'


def download_image(image_url, full_path, image_index):
    response = requests.get(image_url, allow_redirects=True)
    with open(f'{os.path.join(full_path, image_index)}.jpg', 'wb') as img:
        img.write(response.content)

def save_json(element, full_path, i):
    json_full_name = f'{full_path}/{i}.json'
    with open(json_full_name, 'w') as fl:
        json.dump(element, fl, indent=4, sort_keys=True)

def download_and_save_images_and_description(data):
    for i, element in enumerate(data):
        full_path = os.path.join(save_path, str(i))
        print(full_path)
        if not os.path.isdir(full_path):
            os.makedirs(full_path)
        save_json(element, full_path, i)
        for image_index, image_url in enumerate(element['image_urls']):
            download_image(image_url, full_path, str(image_index))

def main():
    with open(file_path, 'r') as fl:
        data = json.load(fl)

    download_and_save_images_and_description(data)

if __name__ == '__main__':
    main()
