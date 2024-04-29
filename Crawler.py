import requests 

from bs4 import BeautifulSoup
from dataclasses import dataclass

# 1. Définir des fonctions
# 2. Utiliser dataclass

@dataclass
class PostThing:
    title: str
    author_id: int
    # whatever
    pass

my_post = PostThing(title="patate",author_id=420)

# from parser import ParserError

# Set the path to the desktop
desktop_path = './'
file_name = 'sitemap.xml'
file_path = desktop_path + file_name

sitemap_url = 'https://www.galaxyrpg.net/sitemap.php'

# Send a GET request to the sitemap URL
response = requests.get(sitemap_url)
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Save the response content as a file
    with open(file_path, 'w') as f:
        f.write(response.content.decode('utf-8'))
    soup = BeautifulSoup(response.content, 'xml')
    loc_tags = soup.find_all('loc')
    for loc_tag in loc_tags:
        print(loc_tag.text)
else:
    print(f'Failed to crawl or load: {sitemap_url}')