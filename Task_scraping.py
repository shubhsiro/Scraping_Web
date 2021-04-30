import schedule
import time
import datetime

import requests 
import bs4 
import pandas as pd 

def check_data():
    ## print("done")
    # Make requests from webpage
    url = 'https://www.worldometers.info/coronavirus/country/india/'
    result = requests.get(url)
    # Creating soap object
    soup = bs4.BeautifulSoup(result.text,'lxml')
    # Searching div tags having maincounter-number class
    cases = soup.find_all('div' ,class_= 'maincounter-number')
    # List to store number of cases
    data = []
    # Find the span and get data from it
    for i in cases:
        span = i.find('span')
        data.append(span.string)
    # Display number of cases
    print(data)
    # Creating dataframe
    df = pd.DataFrame({"CoronaData": data})
    # Naming the coloumns
    df.index = ['TotalCases', ' Deaths', 'Recovered']
    # Saving csv file name with time stamp
    filename = datetime.datetime.now().strftime('test-%Y-%m-%d-%H-%M.csv')
    # Saving the data in csv file
    df.to_csv(filename)
    # print
    print("done")

schedule.every(4).hours.do(check_data)
while 1:
    #check if any task is pending
    schedule.run_pending()
    time.sleep(1)
