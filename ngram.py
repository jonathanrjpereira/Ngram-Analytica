
import requests
import re
import matplotlib.pyplot as plt

ngram = "farrago" #Example Word: farrago

def graph(word):

    #page = requests.get("https://books.google.com/ngrams/graph?content=farrago&year_start=1800&year_end=2008&corpus=15&smoothing=8&share=&direct_url=t1%3B%2Cfarrago%3B%2Cc0")


    url1 = "https://books.google.com/ngrams/graph?content="
    url2 = "&year_start=1800&year_end=2008&corpus=15&smoothing=8&share=&direct_url=t1%3B%2C"
    url3 = "%3B%2Cc0"
    url = url1 + str(word) + url2 + str(word) + url3
    #print (url)

    page = requests.get(url)
    #print (page.status_code)

    #print (page.content)

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page.content, 'html.parser')

    data = []
    for paragraph in soup.find_all('script'):
        data.append(paragraph.string)

    graph = data[7] #data[7] contains all the graph's plotted points in percentages.

    try:
        found = re.search('"timeseries": (.+?)], "pare', graph).group(1)    #Start & End of graph data
    except AttributeError:
        found = 'Error' # apply your error handling
    #print (found)

    list = found.split (', ')   #Convert graph's data points into list
    list = [s.replace('[', '') for s in list]   #Removes any garbage values from data.
    #print (len(list))


    list = [float(s) for s in list]
    #list = [float(s)*10000000 for s in list]    #Coverts data points from floating exponential values to float
    # 10,000,000 is used such that numbers with value 10e-5 are less than 1

    #print (len(list))
    print (list)
    return list


graph_plot = graph(ngram)

year = list(range(1800, 2009))  # X-axis Co-ordinates
#print (year)

plt.plot(year, graph_plot)  #Plot X=Year , Y=Frequency(%)
plt.axis([1800, 2008, min(graph_plot), max(graph_plot)])    # X & Y axis Range
plt.xlabel('Year')
plt.ylabel('Frequency(%)')
plt.show()
