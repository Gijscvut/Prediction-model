import pandas as pd

#Read data from the Excel document
df = pd.read_excel(r'SERENE water consumption behavior copy.xlsx', sheet_name='weekend', nrows = 6834)

df = df[['Water Flow Rate']]

df_reversed = df.iloc[::-1]

#starting points for 2 days ahead with 168 hours being 1 week back
#max_point is 48 hours ahead
start_point = 168
max_point = 216

#empty list to append results, used later on for .csv requirement
'''results = []'''

#for loop calculating per hour in range of 48 hrs
for start_point in range(168, max_point):
    #set starting points per week back
    start_pointtwo = start_point + 168
    start_pointthree = start_point + 336
    start_pointfour = start_point + 504
    #obtain flow for timestamps
    point_weekone = df_reversed.iloc[start_point]['Water Flow Rate']
    point_weektwo = df_reversed.iloc[start_pointtwo]['Water Flow Rate']
    point_weekthree = df_reversed.iloc[start_pointthree]['Water Flow Rate']
    point_weekfour = df_reversed.iloc[start_pointfour]['Water Flow Rate']
    
    #print(f"Week 1: {point_weekone:2f}, Week 2: {point_weektwo:2f}, Week 3: {point_weekthree:2f}, Week 4: {point_weekfour:2f}")
    
    #calculate variables for new flow per week
    flow_one = 0.5 * point_weekone
    flow_two= 0.25 * point_weektwo
    flow_three = 0.125 * point_weekthree
    flow_four = 0.125 * point_weekfour
    
    #new predicted flow
    Qnew = flow_one + flow_two + flow_three + flow_four
    #setting variable to print number per hour
    Qnew_point = start_point - 168
    #print results
    print(f"Qnew {Qnew_point} hours ahead: {Qnew:2f}")
    