__Web Scraping Project__  
This project contains a Python script main.py that scrapes information from a list of sports news articles and writes the content of each article to a separate text file.


__Getting Started:__  
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


__Prerequisites:__  
The project requires Python and Conda to be installed on your machine.


__Installing:__  
Follow these steps to set up a new Conda environment and run the program:

1. Open your terminal.

2. Navigate to the project directory:  
    *cd path/to/your/project* (please replace "path/to/your/project" with your path to the file)

3. Create a new Conda environment and install the required packages using the requirements.yml file:  
    *conda create -n myenv --file requirements.yml* (please replace "myenv" with your desired environment name)

4. Activate the new environment:  
    *conda activate myenv* (please replace "myenv" with environment name created in previous step)


__Running the Program:__  
After setting up the environment, you can run the program using the following command:  
*python3 main.py*


__File Description:__  
main.py: This is the main Python script that performs the web scraping task. It reads a list of URLs from a text file, scrapes the content of each URL using requests and beautifulsoup4, formats the content by adding a newline every 20 words, and writes the formatted content to a separate text file for each URL.


urls.txt: This file contains the five URLs that will be scraped in main.py


ariticle1-5.txt: These five .txt files contain the information scraped from the five URLs in main.py

------------------------------------------------------------------------------------------------------------

Please replace the placeholders "myenv" and "path/to/your/project" with the name of your Conda environment and the actual path to your project.

Italicized text indicates commands directly used in your terminal.

