# Exploring the My Drama List Website
This is the final project for my BYU Stat 386 course. It has 3 parts: collecting the data, exploratory data analysis, and building a dashboard. 

## Collecting the Data
* **bsoup_scrape.py** This contains the function that scrapes the mdl website for title,year,episodes,country,viewer_score, and rank 
* **combined_soup.csv** Contains the data scraped through beautiful soup
* **selenium_notes.ipynb** Contains code for scraping the title pages with selenium
* **selenium_scrape.py** As of yet is an unsuccessful attempt to create a separate function I could incorporate in the cleaning notebook
* **combined_selenium.csv** Contains data scraped through selenium
* **data_cleaning.ipynb** This contains the code for running the bsoup_scrape function, combining csv files, and cleaning the data
* **combined_mdl.csv** Contaings the merged data collected with soup and selenium
* **mdl_final.csv** This is the cleaned and final version of the data used for EDA

## Exploratory Data Analysis
* **eda.ipynb** This notebook has code to explore the data and create graphics

## Building a Dashboard 
* **dashboard.py** Contains code to make streamlit dashboard
* **requirements.txt** Lists the packages required for the dashboard

## Feedback Folder
* various text files to document the feedback process for my class assignment
