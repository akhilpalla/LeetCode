# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
import asyncio

async def get_url(htmlParser, url):
    return await asyncio.to_thread(htmlParser.getUrls, url)

class Solution:

    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        return asyncio.run(self.async_crawl(startUrl, htmlParser))

    async def async_crawl(self, startUrl, htmlParser):
        seen = set()
        result = set()
        domain = "http://" + startUrl[len("http://"):].split("/")[0]

        async def dfs(start_url):
            if start_url in seen:
                return 
            seen.add(start_url)
            result.add(start_url)
            children = []
            for c in await get_url(htmlParser, start_url):
                if c.startswith(domain):
                    children.append(c)
            await asyncio.gather(*list(dfs(c) for c in children))

        await dfs(startUrl)
        return list(result)