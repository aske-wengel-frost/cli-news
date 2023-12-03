import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


def scrape_news(content_address: str) -> [str]:
    """
    :param content_address: string-type address of website
    :return: list of strings ->  titles and links respectively
    """

    response = requests.get(content_address)

    if response.status_code != 200:
        print("Failed to fetch the page.")

    else:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Get elements with specified class-name. Thank god dr knows how to name classes :-P
        news_items = soup.find_all('li', class_='hydra-latest-news-page__index-list-item')
        data = []
        for item in news_items:
            # Extract the title
            title_element = item.find('a', class_='hydra-card-title')
            title = title_element.get_text() if title_element else "No Title Found"

            # Extract the link
            link = title_element['href'] if title_element else "No Link Found"

            data.append([title, 'dr.dk' + link])
        return data


def display_data_tabulated(data):
    if not data:
        print("No data retrieved :-(")
    else:
        # print(f"Title: {title}", f"Link: dr.dk{link}\n")
        print(tabulate(data, headers=["Title", "Reference"], tablefmt='heavy_grid'))


# Specify desired news-webpage
url: str = "https://www.dr.dk/nyheder"

news_data = scrape_news(url)
display_data_tabulated(news_data)
