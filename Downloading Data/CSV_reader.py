#CSV = data separated by commas
import csv
import matplotlib.pyplot as plt
from datetime import datetime

    
def num_columns(filename):
   
    with open(filename) as file_object:
        reader = csv.reader(file_object)
        header_row = next(reader)
        print('\n')
        print(header_row)
        print('\n')
        for index, column_heading in enumerate(header_row):
            print(index,column_heading)
        

def make_gragh(filename):

    

    with open(filename) as file_object:
        reader = csv.reader(file_object)
        header_row = next(reader)

        dates,highs,lows =[],[],[]
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[5])
            low = int(row[6])
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            
                


    plt.style.use('seaborn')
    fig,ax = plt.subplots()
    ax.plot(dates,highs,c='red',alpha=0.5)
    ax.plot(dates,lows,c='blue',alpha=0.5)
    ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
    fig.autofmt_xdate()
    ax.grid()
    # fig.savefig("matexpress.png")
    plt.show()


make_gragh('C:\Users\mitch\Desktop\coding\Python\Downloading Data\sitka_weather_2018_simple.csv')


# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.plot(highs)
# ax.set_title('Temp across july',fontsize=24)
# ax.set_xlabel('',fontsize=14)
# fig.autofmt_xdate()
# ax.set_ylabel('Temp',fontsize=14)
# ax.tick_params(axis='both',which='major',labelsize=16)
# ax.grid()


# fig.savefig("test.png")
# plt.show()