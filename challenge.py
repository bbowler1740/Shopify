import numpy as np
import pandas as pd

def calculate_avg__order_amount():
    data = pd.read_excel (r'C:\Users\Brayden\Desktop\Personal\Applications\Shopify\2019 Winter Data Science Intern Challenge Data Set.xlsx') #Use a relative path.
    df = pd.DataFrame(data, columns=['order_amount'])
    sumOrderAmount = df.sum()
    avgOrder = (sumOrderAmount / df.size) #Size calculates elements in the df object. Represents number of rows in the Excel sheet (or in the business case, total orders).
    return avgOrder

def calculate_avg_item_cost_per_order():
    data = pd.read_excel (r'C:\Users\Brayden\Desktop\Personal\Applications\Shopify\2019 Winter Data Science Intern Challenge Data Set.xlsx') #Use a relative path.
    dfTI = pd.DataFrame(data, columns=['total_items'])
    dfOA = pd.DataFrame(data, columns=['order_amount'])
    sumTotalItems = float(dfTI.sum())
    sumOrderAmount = float(dfOA.sum())
    avgCost = float(sumOrderAmount / sumTotalItems) #Represents the avg item cost per order
    return avgCost

print(calculate_avg__order_amount()) #We know from the case description this should be $3,145.13, use as a check.
print(calculate_avg_item_cost_per_order())

