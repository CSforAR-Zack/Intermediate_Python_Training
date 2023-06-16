import requests
import json

from datetime import datetime
from matplotlib.pyplot import subplots, show

def main():
    # Do not share your token with anyone or commit it to a public repository.
    # https://www.ncdc.noaa.gov/cdo-web/webservices/v2#data for the api guide
    # https://www.ncdc.noaa.gov/cdo-web/token to get your token.
    token = 'TOKEN GOES HERE'
    datatype_ids = 'TMAX,TMIN'
    units = 'standard'
    dataset_id = 'GHCND'
    station_id = 'GHCND:USW00003952'
    start_date = '2022-01-01'
    end_date = '2022-01-31'

    request_url = f'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid={dataset_id}&datatypeid={datatype_ids}&stationid={station_id}&startdate={start_date}&enddate={end_date}&limit=1000&units={units}'

    r = requests.get(request_url, headers={'token': token})

    data = json.loads(r.text)

    # with open('data.json', 'w') as f:
    #     json.dump(data, f, indent=4)

    # Iterate through the data and seperate out date, high, and low to we can display it in a graph
    dates = list()
    highs = list()
    lows = list()

    for item in data['results']:
        date = item['date']
        date = date.split('T')[0]
        date = datetime.strptime(date, '%Y-%m-%d')

        if date not in dates:
            dates.append(date)

        if item['datatype'] == 'TMAX':
            highs.append(item['value'])
        elif item['datatype'] == 'TMIN':
            lows.append(item['value'])

    # Setting up the graph and figure
    # subplots() returns a tuple containing a figure and a list of axes
    # so we can unpack the tuple into two variables.
    # One for the figure and one for the axes
    graph = subplots()
    graph_figure = graph[0]
    graph_parts = graph[1]

    # Will plot 2 lines
    # One for the highs and one for the lows
    graph_parts.plot(dates, highs, c="red")
    graph_parts.plot(dates, lows, c="blue")

    # Labeling Graph
    # The set_title() method is used to set the title of the graph
    # The set_xlabel() method is used to set the label for the x-axis
    # The set_ylabel() method is used to set the label for the y-axis
    # \u00b0 is the unicode character for the degree symbol
    graph_parts.set_title("Little Rock Daily Temps", fontsize=26)
    graph_parts.set_xlabel("Date", fontsize=18)
    graph_parts.set_ylabel("Temperature (\u00b0F)", fontsize=18)
    
    # Formatting the x-axis to show the dates as month/day
    graph_figure.autofmt_xdate()

    # Show the graph
    show()
    
    # Save file
    # graph_figure.savefig("graph.png")

        


if __name__ == '__main__':
    main()