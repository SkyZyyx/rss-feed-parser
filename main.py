import feedparser

def inp():
    url = input("Enter the URL of the RSS feed: ")
    return url

def parse(url):
    d = feedparser.parse(url)
    title = d.feed.title
    link = d.feed.link
    subtitle = d.feed.subtitle
    generator = d.feed.generator
    return title,link,subtitle,generator


url = inp()
title,link,subtitle,generator = parse(url)

print(f"Title est : {title}")
print(f"Link is : {link}")
print(f"Subtitle is : {subtitle}")
print(f"Generator is : {generator}")


