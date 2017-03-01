import functools
import re
from lxml import etree

import aiohttp
import asyncio

AVAILABLE_LANGUAGES = {
    "en": "english",
    "de": "german",
    "fr": "french",
    "sv": "swedish",
    "es": "spanish",
    "bg": "bulgarian",
    "ro": "romanian",
    "it": "italian",
    "pt": "portuguese",
    "ru": "russian"
}

BASE_URL = "http://{subdomain}.dict.cc/?s={search}"


class UnavailableLanguageError(Exception):
    pass


class Translate:
    @staticmethod
    def filter(content: str):
        def sanitize(word):
            return re.sub("[\\\\\"]", "", word)

        in_list = []
        out_list = []
        javascript_list_pattern = "\"[^,]+\""
        print(content)
        for line in content.split("\n"):
            if "var c1Arr" in line:
                in_list = list(map(sanitize, re.findall(javascript_list_pattern, line)))
            elif "var c2Arr" in line:
                out_list = list(map(sanitize, re.findall(javascript_list_pattern, line)))
        return in_list, out_list

    @classmethod
    async def _make_request(cls, request_url):
        session = aiohttp.ClientSession(
            headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.3;'
                                   ' WOW64; rv:30.0) Gecko/20100101 Firefox/30.0'}
        )

        async with session.get(request_url) as req:
            assert isinstance(req, aiohttp.ClientResponse)

            return (await req.read()).decode()

    @staticmethod
    def _parse_page(content):
        """
        Internal function to parse a page by matching the xpath.
        """
        if content:
            data = etree.HTML(content)
            # Let's hope this doesn't break.
            _root = data.xpath('//*[@id="maincontent"]/script[2]/text()')
            return _root

    @classmethod
    async def get_translation(cls, word, from_lang, to_lang, url=BASE_URL):

        subdomain = from_lang.lower() + to_lang.lower()

        req_url = url.format(subdomain=subdomain, search=word)
        response = await cls._make_request(request_url=req_url)

        parse_part = functools.partial(cls._parse_page, response)
        event = asyncio.get_event_loop()
        parsed = await event.run_in_executor(None, parse_part)

        return cls.filter(str(parsed))


loop = asyncio.get_event_loop()
print(loop.run_until_complete(Translate.get_translation("car", "en", "de")))
