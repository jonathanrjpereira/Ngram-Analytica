# Ngram Analytica
Web-Scrapes &amp; Re-Plots the Google Ngram Viewer Graph for any N-gram in Python.
The Google Books Ngram Viewer is an online search engine that charts the frequencies of any set of comma-delimited search strings using a yearly count of n-grams found in sources printed between 1500 and 2008 in Google's text corpora in English.

## Features
 - Works for any N-gram without numbers or special characters. 
 - Scrapes & organizes all the individual data-points of the Google Ngram Viewer Graph using BeautifulSoup.
 - Re-Plots the graph using Matplotlib in Python.

## Working
![Google Ngram - Farrago](https://github.com/jonathanrjpereira/Ngram-Analytica/blob/master/img/Google%20Ngram%20farrago.png)

In the above image, we can see Google's Ngram for the word "farrago" that charts the frequencies of the word usage from the years 1800-2009. The data can be downloaded from Google's Ngram website itself. Alternatively, we can use web-scraping techniques to gather individual N-gram data. This is beneficial since it doesn't require the dataset of every possible N-gram.

![Page Source - Farrago](https://github.com/jonathanrjpereira/Ngram-Analytica/blob/master/img/HTML%20Source.JPG)

In order to this, we need to scrape through the HTML source of the particular N-gram wherein we will find the data points(Frequency vs Year) for a particular N-gram. The page source containing the frequency of the word "farrago" can be seen in the above image.
We use BeautifulSoup to obtain the page source. After this, we perform various operations to remove garbage data which leaves us only with the Frequency data of the graph. We then use Matplotlib to plot the Frequency data vs the 209 years as shown in the image below.

![Matplotlib - Farrago](https://github.com/jonathanrjpereira/Ngram-Analytica/blob/master/img/Matplotlib%20Ngram%20farrago.png)

Unlike the Google Ngram graph which does provide headway in the Y-axis, our method sets the maximum & minimum Y-axis graph limits to the maximum & minimum frequency(%) values within the graph. Hence the scale may vary between the two versions of the graph but the values will be the same.

## Dependencies
You will need to install the following dependencies:
 1. Python 3
 2. Web Scraping Library: [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
 3. Graph Plotting Library: [Matplotlib 3.0](https://matplotlib.org/)


## Contributing
Are you a programmer, engineer, first-time-contributor or hobbyist who has a great idea for a new feature in Ngram Analytica? Maybe you have a good idea for a bug fix? Feel free to grab the code and tinker with it. Don't forget to smash those Star & Pull Request buttons.
[Contributor List](https://github.com/jonathanrjpereira/Ngram-Analytica/graphs/contributors)

## Note
We are not affiliated with Google Ngram. This repository was created as a proof of concept & is not meant for large-scale use. Web-Scraping is a temporary solution to gathering such data. Please be mindful & limit the number of requests made to the website using such a method. If your requirement involves performing a large-scale analysis of the underlying data, you might prefer to download a portion of the corpora yourself. Or all of it, if you have the bandwidth and space. You can find more information & datasets [Here.](http://storage.googleapis.com/books/ngrams/books/datasetsv2.html)  
