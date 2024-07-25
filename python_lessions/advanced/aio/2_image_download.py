import asyncio
import aiohttp
import aiofiles

img_urls = [
    'https://images.unsplash.com/photo-1655593805858-2054056d3ee6',
    'https://images.unsplash.com/photo-1655219435115-d9f0faccd7cd',
    # 'https://images.unsplash.com/photo-1655669357124-394d107b3aaf',
    # 'https://images.unsplash.com/photo-1653875096546-f776564b5548',
    # 'https://images.unsplash.com/photo-1654868739497-ee031a3d7088',
    # 'https://images.unsplash.com/photo-1654938900760-1419ee86bc1d',
    # 'https://images.unsplash.com/photo-1654986966034-8f06a66f280a',
    # 'https://images.unsplash.com/photo-1655019680534-0838d2870bfd',
    # 'https://images.unsplash.com/photo-1655033791689-523f86065166',
    # 'https://images.unsplash.com/photo-1654015969220-d1174cfa9719'
]


def get_tasks(session: aiohttp.ClientSession()):
    tasks = []
    for img_url in img_urls:
        tasks.append(session.get(img_url))
        print('downloading....{}'.format(img_url))

    return tasks


async def download_image():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        responses = await asyncio.gather(*tasks)
        i = 1
        for response in responses:
            f = await aiofiles.open('images/{}.jpg'.format(i), mode='wb')
            await f.write(await response.read())
            await f.close()
            i += 1

asyncio.run(download_image())

