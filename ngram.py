import sys
import requests
import re
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

def graph(content, start, end, smoothing):
    url = "https://books.google.com/ngrams/graph"

    querystring = {"content":content,
                   "case_insensitive":"on",
                   "year_start":start,
                   "year_end":end,
                   "corpus":"15",
                   "smoothing":smoothing}

    page = requests.get(url, params=querystring)

    soup = BeautifulSoup(page.content, 'html.parser')

    data = []
    for paragraph in soup.find_all('script'):
        data.append(paragraph.string)

    graph = data[7] #data[7] contains all the graph's plotted points in percentages.

    try:
        found = re.search('"timeseries": (.+?)], "pare', graph).group(1)    #Start & End of graph data
    except AttributeError:
        print("Encountered an error! Here's the response from the page\n Response: {}".format(page.content)) # apply your error handling
        sys.exit(1) # Exit gracefully

    # Convert graph's data points into list and
    # remove any garbage values from data
    tokens = found.replace('[', '').split(', ')
    datapoints = [float(datapoint) for datapoint in tokens]
    #list = [float(s)*10000000 for s in list]    #Coverts data points from floating exponential values to float
    # 10,000,000 is used such that numbers with value 10e-5 are less than 1

    return datapoints

def ngram_viewer(content, start, end, smoothing):
    graph_plot = graph(content, start, end, smoothing)
    year = list(range(start, end))  # X-axis Co-ordinates

    plt.plot(year, graph_plot)  #Plot X=Year , Y=Frequency(%)
    plt.axis([start, end, min(graph_plot), max(graph_plot)])    # X & Y axis Range
    plt.xlabel('Year')
    plt.ylabel('Frequency(%)')
    plt.show()

if __name__ == '__main__':
    ngram_viewer("Farrago", 1800, 2009, smoothing=3)
