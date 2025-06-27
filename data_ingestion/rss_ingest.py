import feedparser
import json
from pathlib import Path
from datetime import datetime

# RSS Feed URL (you can change to CNN/NYT later)
RSS_URL = "http://feeds.bbci.co.uk/news/world/rss.xml"

# Output path
output_file = Path("data/raw/news_rss.jsonl")
output_file.parent.mkdir(parents=True, exist_ok=True)

def fetch_and_save_rss():
    feed = feedparser.parse(RSS_URL)

    if not feed.entries:
        print("[!] No entries found.")
        return

    with output_file.open("a") as f:
        for entry in feed.entries:
            news = {
                "title": entry.get("title", ""),
                "summary": entry.get("summary", ""),
                "published": entry.get("published", str(datetime.utcnow())),
                "link": entry.get("link", ""),
                "source": "BBC"
            }
            f.write(json.dumps(news) + "\n")
            print(f"[✔] Saved: {news['title']}")

if __name__ == "__main__":
    fetch_and_save_rss()

