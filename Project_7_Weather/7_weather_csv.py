from datetime import datetime
from csv import reader

# Pip install matplotlib (not if using replit.com)
from matplotlib.pyplot import subplots, show


def main():
    # Getting Static Data
    filename = "Little_Rock_Weather_2019.csv"

    with open(filename) as f:
        # Create a reader object for the CSV file to make it easier to work with
        # the data in the file
        r = reader(f)

        # Grab (pop) the header row and remove it from the reader
        header_row = next(r)

        # Create empty lists to store the data we want to plot
        highs = []
        lows = []
        dates = []
        
        # Loop through the rows in the reader object
        for row in r:
            # Getting a specific station: USW00003952
            if row[0] == "USW00003952":
                # Highs are in column 5
                high = int(row[5])
                highs.append(high)

                # Lows are in column 6
                low = int(row[6])
                lows.append(low)

                # Matplotlib.pyplot needs dates in a specific format
                # so we need to convert the date string to a datetime object
                # before we can plot it. The format of the date string is
                # YYYY-MM-DD so we can use strptime() to convert it to a
                # datetime object by using the format string "%Y-%m-%d"
                date = datetime.strptime(row[2], "%Y-%m-%d")
                dates.append(date)

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
    graph_parts.set_title("Little Rock Daily Temps, 2019", fontsize=26)
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