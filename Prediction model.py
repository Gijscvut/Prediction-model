import pandas as pd

import csv

import matplotlib.pyplot as plt

#Read data from the Excel document, nrows depends on latest value
df = pd.read_excel(r'SERENE water consumption behavior copy.xlsx', sheet_name='weekend', nrows = 6608)

#choose column
df = df[['Water Flow Rate']]
#start from the bottom to the top because the lowest row is the row with the most recent value
df_reversed = df.iloc[::-1]

#starting points for 2 days ahead with 168 hours being 1 week back, is 169 because it equals to values manually found
#max_point is 48 hours ahead
start_point = 169
max_point = 121

#empty list to append results to, used later on for .csv requirement
results = []
time = []

#opening csv file
with open('Predicted consumption.csv', 'w', newline='') as csvfile:
    predictdoc = csv.writer(csvfile)
    field = ["Time (date, hour)", "Water flow L/h"] 
    predictdoc.writerow(field)
#for loop calculating per hour in range of 48 hrs
    for start_point in range(169, max_point, -1):
        #starting point 2 weeks back
        start_pointtwo = start_point + 168
        #starting point 3 weeks back
        start_pointthree = start_point + 336
        #starting point 4 weeks back
        start_pointfour = start_point + 504
        #obtain flow for timestamps
        point_weekone = df_reversed.iloc[start_point]['Water Flow Rate']
        point_weektwo = df_reversed.iloc[start_pointtwo]['Water Flow Rate']
        point_weekthree = df_reversed.iloc[start_pointthree]['Water Flow Rate']
        point_weekfour = df_reversed.iloc[start_pointfour]['Water Flow Rate']
        #print(point_weekon * 60)
        #print(point_weektwo * 60)
        #print(point_weekthree * 60)
        #print(point_weekfour * 60)
        #test, commented because not necessary now
        #print(f"Week 1: {point_weekone:2f}, Week 2: {point_weektwo:2f}, Week 3: {point_weekthree:2f}, Week 4: {point_weekfour:2f}")
        
        #calculate variables using the flow for each hour multiplied by the 'importance factor'
        flow_one = 0.5 * point_weekone
        flow_two= 0.25 * point_weektwo
        flow_three = 0.125 * point_weekthree
        flow_four = 0.125 * point_weekfour
        
        #new predicted flow
        Qnew = (flow_one + flow_two + flow_three + flow_four) * 60
        print(Qnew)
        #setting variable to print number per hour
        
        Qnew_point = -start_point + 169
        #print results, commented because it's only for testing
        #print(f"Qnew {Qnew_point} hours ahead: {Qnew:2f}")
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
    plt.show() 