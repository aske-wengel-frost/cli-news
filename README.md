# News Scraper

This Python script is designed to scrape the latest news titles and links from a specified website. It utilizes the `requests`, `BeautifulSoup`, and `tabulate` libraries to extract data and display it in a tabulated format.

![Example Usage](Screenshot%202023-12-03%20at%2012.16.14.png)

## Requirements
- Python 3.x
- Required Python packages: `requests`, `BeautifulSoup`, `tabulate`

## Usage
1. Ensure you have Python installed.
2. Install necessary packages using pip:
3. Run the script by executing the code.
4. Specify the desired news webpage URL by setting the `url` variable to the desired website.

## Code Explanation
- The `scrape_news` function takes a website address as input and retrieves the latest news titles and links from the specified webpage.
- The `display_data_tabulated` function displays the extracted data in a tabulated format.
- The main section of the code specifies the URL of the news webpage, scrapes the data using `scrape_news`, and displays it using `display_data_tabulated`.

## Functionality
1. The `scrape_news` function:
 - Takes the URL of a webpage as input.
 - Retrieves the webpage content using `requests`.
 - Parses the HTML content using `BeautifulSoup`.
 - Extracts news items based on specified class names and retrieves their titles and links.
 - Returns a list containing titles and corresponding links.

2. The `display_data_tabulated` function:
 - Checks if data is available.
 - Displays the extracted news data in a tabulated format using the `tabulate` library.

## Example Usage
```python
url: str = "https://www.dr.dk/nyheder"  # Set the desired news webpage URL
news_data = scrape_news(url)
display_data_tabulated(news_data)
