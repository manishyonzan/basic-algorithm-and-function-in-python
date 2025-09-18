import pandas as pd
from IPython.display import display, HTML




# f = open("itinerary.csv", 'r')
# csv_reader = csv.DictReader(f)
# itinerary = []
# for row in csv_reader:
#     print(row)
#     itinerary.append(row)
# f.close()


# itenary = [{'Arrival': 'July-01', 'Departure': 'July-08', 'City': 'New York', 'Country': 'USA'}, {'Arrival': 'July-09', 'Departure': 'July-16', 'City': 'Rio de Janeiro', 'Country': 'Brazil'}, {'Arrival': 'July-17', 'Departure': 'July-24', 'City': 'Cape Town', 'Country': 'South Africa'}, {'Arrival': 'July-25', 'Departure': 'August-01', 'City': 'Istanbul', 'Country': 'Turkey'}, {'Arrival': 'August-02', 'Departure': 'August-09', 'City': 'Paris', 'Country': 'France'}, {'Arrival': 'August-10', 'Departure': 'August-17', 'City': 'Tokyo', 'Country': 'Japan'}, {'Arrival': 'August-18', 'Departure': 'August-25', 'City': 'Sydney', 'Country': 'Australia'}]

# display_table(itinerary)

def display_table(data):
    df = pd.DataFrame(data)

    # Display the DataFrame as an HTML table
    display(HTML(df.to_html(index=False)))