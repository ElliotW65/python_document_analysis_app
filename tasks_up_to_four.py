import numpy as np
import matplotlib.pyplot as plt
import httpagentparser  as http



def task_two_a(data, graph_function):
    '''
    Function to create a hisogram of the countries in the data passed
    in as a parameter. Calls get_unique_counts to create a dictionary
    of the count of the occurancrs of each country in the data and then
    creates a graph with the result by calling the graph function
    passed in as a parameter.

    Parameters:
        data (list): The list of countries for which to make the histogram.
        graph_function (function): Function to create the histogram of country
                                    counts.

    '''

    result = get_unique_counts(np.array(data))

    graph_function(result, 'Country', 'Histogram of visitor countries')


def process_browsers(browsers, graph_function, flag=None):
    '''
    Function to create a hisogram of the browsers in the data passed
    in as a parameter. If the task is 3b the data is transformed to 
    the short browser names e.g. 'Chrome' using the httpagentparser
    module. If not, the histogram is made using the verbose user agent
    string.

    Parameters:
        data (list): The list of visitor_useragent for which to make the histogram.
        graph_function (function): Function to create the histogram of country
                                    counts.
        flag (string): The task code specified by the user.

    '''

    if flag == '3b':
        browser_list = [http.detect(x) for x in browsers]

        browsers = [i['browser']['name'] if i.get('browser') else i.get('version')for i in browser_list]

    browser_arr = np.array(browsers)

    browser_arr = browser_arr[browser_arr != np.array(None)]

    result = get_unique_counts(browser_arr)

    graph_function(result, 'Browser', 'Histogram of broswers')



def task_four(data):
    '''
    Function to create a sorted dictionary of the total number of seconds each
    user spent reading in descending order and print the top 10.

    Parameters:
        data (list): The list of countries for which to make the histogram.

    '''

    read_time = {}

    for i in data:
        if read_time.get(i['visitor_uuid']) and i.get('event_readtime'):
            read_time[i['visitor_uuid']] += i['event_readtime']
        elif i.get('event_readtime'):
            read_time[i['visitor_uuid']] = i['event_readtime']

    sorted_dictionary = [(key,value) for key, value in dict(sorted(read_time.items(), key=lambda x: x[1], reverse=True)).items()]

    for i in sorted_dictionary[:10]:
        print(i[0], ' ', i[1])



def get_unique_counts(arr):
    '''
    Function to create dictionary of the number of occurances of each unique
    value in the numpy array passed in as a parameter.

    Parameters:
        arr (numpy array): An array of values for which to count the unique
                            occurances of each value.
    
    Returns:
        A dictionary where the key is each unique item in the arr parameter
        and the value is the count of the occurances of that value in the arr.

    '''

    values, counts = np.unique(arr, return_counts=True)

    return dict(zip(values, counts))

def show_histogram(data, xlabel, title):
    '''
    Function to create and show a bar chart/histogram of the values
    passed in as a parameter.

    Parameters:
        data (dict): A dictionary of keys and values to be plotted.
        xlabel (string): A label for the x axis of the graph
        title (string): A title for the graph.
    
    '''

    plt.bar(data.keys(), data.values())
    plt.title(title)
    plt.xlabel(xlabel)
    plt.xticks(rotation=90)
    plt.ylabel('Count')
    plt.show()
