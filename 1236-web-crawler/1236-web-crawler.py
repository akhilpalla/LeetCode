class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = self.getHostName(startUrl)
        return self.dfs(startUrl, htmlParser, hostname, {})
    def dfs(self, url: str, htmlParser: 'HtmlParser', hostname: str, visited: Dict[str, None]) -> List[str]:
        if hostname not in url or url in visited:
            return visited
        visited[url] = None
        neighbors = htmlParser.getUrls(url)
        merged = visited
        for n in neighbors:
            v = self.dfs(n, htmlParser, hostname, visited)
            if v is not None:
                merged = v | visited
        return merged
    def merge(self, v: Dict[str, None], visited: Dict[str, None]) -> Dict[str, None]:
        m = {}
        for (key, value) in v:
            m[key] = value
        for (key, value) in visited:
            m[key] = value
        return m
    def bfs(self, url: str, htmlParser: 'HtmlParser', hostname: str, visited: Dict[str, None]) -> List[str]:
        q = [url]
        while len(q) > 0:
            url = q.pop(0)
            visited[url] = None
            neighbors = htmlParser.getUrls(url)
            for n in neighbors:
                if hostname in n and n not in visited:
                    q.append(n)
        return visited
    def getHostName(self, startUrl) -> str:
        forwardSlashCount = 0
        lastKnownForwardSlashIndex = -1
        i = 0
        while i < len(startUrl) and forwardSlashCount < 3:
            if startUrl[i] == "/":
                forwardSlashCount += 1
                lastKnownForwardSlashIndex = i
            i += 1 
        if lastKnownForwardSlashIndex == 6:
            return startUrl
        else:
            return startUrl[0:lastKnownForwardSlashIndex]