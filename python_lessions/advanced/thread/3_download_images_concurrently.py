from typing import List
import requests
import time
import os
import concurrent.futures


img_urls = [
    'https://images.unsplash.com/photo-1655593805858-2054056d3ee6',
    'https://images.unsplash.com/photo-1655219435115-d9f0faccd7cd',
    'https://images.unsplash.com/photo-1655669357124-394d107b3aaf',
    'https://images.unsplash.com/photo-1653875096546-f776564b5548',
    'https://images.unsplash.com/photo-1654868739497-ee031a3d7088',
    'https://images.unsplash.com/photo-1654938900760-1419ee86bc1d',
    'https://images.unsplash.com/photo-1654986966034-8f06a66f280a',
    'https://images.unsplash.com/photo-1655019680534-0838d2870bfd',
    'https://images.unsplash.com/photo-1655033791689-523f86065166',
    'https://images.unsplash.com/photo-1654015969220-d1174cfa9719'
]


def download_images_sync(urls: List[str]):
    for url in urls:
        img_bytes = None
        try:
            img_bytes = requests.get(url).content
        except Exception as e:
            print(f'Fail to download {url}')

        img_name = url.split('/')[3]
        img_name = f'{img_name}.jpg'
        img_source = f'images/{img_name}'

        try:
            with open(img_source, 'wb') as file:
                file.write(img_bytes)
                print(f'{img_name} download was completed.........')
        except Exception as e:
            print(f'Fail to store {img_name}')


def download_image_task(img_url: str):
    print(f'Starting download {img_url}')
    img_bytes = None
    try:
        img_bytes = requests.get(img_url).content
    except Exception as e:
        print(f'Fail to download {img_url}')

    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    img_source = f'images/{img_name}'

    # check whether image exists or not, if exists delete it
    if os.path.isfile(img_source):
        os.remove(img_source)

    # store image file
    try:
        with open(img_source, 'wb') as file:
            file.write(img_bytes)
            print(f'{img_name} download was completed.........')
    except Exception as e:
        print(f'Fail to store {img_name}')


def download_images_async():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image_task, img_urls)


start = time.perf_counter()

download_images_sync(img_urls)
# download_images_async()

end = time.perf_counter()

print(f'Total Time: {round(end - start)}')



