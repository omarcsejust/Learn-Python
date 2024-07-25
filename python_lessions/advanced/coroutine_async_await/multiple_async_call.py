import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import time
import random


class ScrapData:

    REQUEST_URL = 'https://regfollower.com/feed'

    def __init__(self):
        agent_li = ['fav', 'news', 'new', '']
        rand_val = random.choice(agent_li)
        self.header = {'user-agent': 'my-{}-app'.format(rand_val)}

    def scrap_news(self):
        news_xml_data = self.get_reg_follower_xml_data(ScrapData.REQUEST_URL)

        news_data = self.parse_news_data(xml_data=news_xml_data)

        start_time = time.time()

        html_desc = asyncio.run(self.read_news_description(news_data))
        for indx, desc in enumerate(html_desc):
            desc_text, p_tag = ScrapData.parse_html_description(desc)
            print(desc_text, p_tag)
        # print(news_data)
        # return desc
        print((time.time() - start_time))

    def get_reg_follower_xml_data(self, reg_follower_url: str):
        req = Request(url=reg_follower_url, headers=self.header)
        response = urlopen(req)
        xml_data = BeautifulSoup(response, 'lxml-xml')  # lxml, lxml-xml, html.parser
        return xml_data

    def parse_news_data(self, xml_data) -> list:
        items = xml_data.find_all('item')
        news_data = []
        for item in items[0:20]:
            title = item.title.text
            desc_url = item.link.text
            summary = item.description.text
            pub_date = item.pubDate.text
            guid = int(item.guid.text.split('=')[1])

            news_data.append(
                {'title': title, 'desc_url': desc_url, 'summary': summary, 'pub_date': pub_date, 'guid': guid})

            # print(title, desc_url, summary, pub_date, guid)
            # break
        return news_data

    def aio_http_tasks(self, session, news_data: []):
        tasks = []
        for data in news_data:
            tasks.append(session.get(data['desc_url'], headers=self.header, ssl=False))
        return tasks

    async def read_news_description(self, news_data: []):
        result = []
        try:
            async with aiohttp.ClientSession(trust_env=True, headers=self.header) as session:
                tasks = self.aio_http_tasks(session, news_data)
                responses = await asyncio.gather(*tasks)
                for response in responses:
                    result.append(await response.text())
                # await session.close()
        except Exception as e:
            print(e)
            return None

        return result

    @staticmethod
    def parse_html_description(desc_res):
        description = ''
        tag_desc = ''
        try:
            desc_html = BeautifulSoup(desc_res, 'html')
            content_html = desc_html.find_all("div", class_="entry-content")
            p_tags = content_html[0].findAll('p')
        except Exception as e:
            print(e)
            return None, None

        for tag in p_tags:
            description = description + ' ' + tag.text
            tag_desc = tag_desc + ' ' + str(tag)

        return description, tag_desc


if __name__ == '__main__':
    scrap_obj = ScrapData()
    scrap_obj.scrap_news()



