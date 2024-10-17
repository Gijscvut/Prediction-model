import pandas as pd

import csv

import matplotlib.pyplot as plt

#Read data from the Excel document, nrows depends on latest value
df = pd.read_excel(r'Testing_prediction_model_data.xlsx', sheet_name='Sheet1', nrows = 693)

#choose column
df = df[['hot water consumption [liter]']]
#start from the bottom to the top because the lowest row is the row with the most recent value
df_reversed = df.iloc[::-1]

#starting points for 2 days ahead with measuring from 48 hours per measuring point
start_point = 49
max_point = 1

#empty list to append results to, used later on for .csv requirement
results = []
time = []

#opening csv file
with open('Predicted consumption day by day.csv', 'w', newline='') as csvfile:
    predictdoc = csv.writer(csvfile)
    field = ["Time (date, hour)", "Water flow L/h"] 
    predictdoc.writerow(field)
#for loop calculating per hour in range of 48 hrs
    for start_point in range(49, max_point, -1):
        #starting point 4-2 days back
        start_pointtwoday = start_point + 48
        #starting point 6-4 days back
        start_pointthreeday = start_point + 96
        #starting point 8-6 days back
        start_pointfourday = start_point + 144
        #obtain flow for timestamps
        point_weekone = df_reversed.iloc[start_point]['hot water consumption [liter]']
        point_weektwo = df_reversed.iloc[start_pointtwoday]['hot water consumption [liter]']
        point_weekthree = df_reversed.iloc[start_pointthreeday]['hot water consumption [liter]']
        point_weekfour = df_reversed.iloc[start_pointfourday]['hot water consumption [liter]']
       
        #calculate variables using the flow for each hour multiplied by the 'importance factor'
        flow_one = 0.5 * point_weekone
        flow_two= 0.25 * point_weektwo
        flow_three = 0.125 * point_weekthree
        flow_four = 0.125 * point_weekfour
        
        #new predicted flow
        Qnew = (flow_one + flow_two + flow_three + flow_four)
        print(Qnew)
        #setting variable to print number per hour
        
        Qnew_point = -start_point + 49
        
        #appending lists which will be printed in .csv file
        results.append(Qnew)
        time.append(Qnew_point)
        
    #write data in document for every step (out of the lists)
    predictdoc.writerows([time, results]) #need to figure out how to write in 2 rows
        #Qnew_point should be adjusted with some function with datetime, probably something like '%Y-%m-%d %H:00'
    #plotting results in a graph
    plt.plot(time, results, color = 'b', linestyle = 'solid', 
         marker = 'o',label = "Qnew") 
  
    plt.xticks(rotation = 0) 
    plt.xlabel('Time (Hour)') 
    plt.ylabel('Heated water flow (Liter/hour)') 
    plt.title('Predicted heated water flow', fontsize = 20) 
    plt.grid() 
    plt.legend() 
    #saving the graph as a figure before showing it in Spyder
    plt.savefig("Results graph day by day prediction" , dpi='figure' , format=None)
    plt.show() 