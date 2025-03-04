import feedparser

d = feedparser.parse('https://feedparser.readthedocs.io/en/latest/examples/rss20.xml')
print(d.feed.title)
print(d.feed.link)
print(d.feed.subtitle)
print(d.feed.generator)
