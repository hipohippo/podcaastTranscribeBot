import re
from typing import Tuple

import requests
from bs4 import BeautifulSoup

episode_id = "63f48cc10d7e8eaa721fe7ed"  ## 测试sample
series_id = {"忽左忽右": "5e4ee557418a84a0466737b7", "不合时宜": "5e280fb8418a84a0461fd076"}
series_prefix = rf"https://www.xiaoyuzhoufm.com/podcast/"


def extract_audio_link_episodeid(episode_id: str) -> Tuple[str, str]:
    sample_link = f"https://www.xiaoyuzhoufm.com/episode/{episode_id}"
    page = requests.get(sample_link)
    if page.status_code != 200:
        return "", ""
    soup = BeautifulSoup(page.content, "html.parser")
    audio_link = soup.find("meta", property="og:audio").get("content", "")
    audio_title = soup.find("title").text
    audio_title = re.search("([^|]*)|.*", audio_title)[1]
    return audio_link, audio_title


def fetch_episode_list(series_id: str):
    pass


def fetch_series_id():
    pass


def search_for_episode_id():
    pass
