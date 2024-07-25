import requests
from bs4 import BeautifulSoup
import pandas as pd

# Read the input file
df = pd.read_excel('Input.xlsx')

def extract_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract title
    title = soup.find('title').text if soup.find('title') else 'No Title'

    # Extract article text
    article = soup.find('article')
    if not article:
        article = soup.find('div', {'class': 'post-content'})
    text = ' '.join([p.text for p in article.find_all('p')]) if article else 'No Content'

    return title, text

for index, row in df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']
    title, text = extract_text(url)
    
    with open(f'{url_id}.txt', 'w', encoding='utf-8') as file:
        file.write(title + "\n" + text)