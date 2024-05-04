'''This module contains the RawData class which is used to scrape the raw html data from a provided URL. 
   It also contains the InputOutput class which is used to read and write data to and from files.''' 

'''Single Responsibility Principle'''

import requests
from bs4 import BeautifulSoup

## Class to get the raw html data from a provided URL
class RawData:
    def scrape(url):
        
        ## Scrape the page source from the URL
        response = requests.get(url)
        lookUp = BeautifulSoup(response.text, 'html.parser')

        ## return html as BeautifulSoup object
        return lookUp

## Class to read and write data to and from files
class InputOutput:
    def read_urls(filename):
        ## Read URLs from a .txt file
        with open(filename, 'r') as file:
            urls = file.readlines()
        urls = [url.strip() for url in urls]
        return urls
    
    def write_to_file(article, filename):
        ##Write the article to a .txt file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(article)

    def clear_contents(filename):
        ## Clear the contents of a file
        with open(filename, 'w') as file:
            file.write('')
    
    def append_article_to_file(article, filename):
        ## Append the article to a .txt file
        with open(filename, 'a') as file:
            file.write(article + '\n\n')

    def append_title_to_file(title, filename):
        ## Append the title to a .txt file
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(title)