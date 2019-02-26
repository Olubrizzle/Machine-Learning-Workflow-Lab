#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 15:24:52 2019

@author: oluwolealowolodu
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import seaborn as sns

order = pd.read_csv('Orders.csv')
returns = pd.read_csv('Returns.csv')

# 1
order['Profit'] = order['Profit'].str.replace('[^\d\.]', '')
order['Profit'] = pd.to_numeric(order['Profit'])

order['Sales'] = order['Sales'].str.replace('[^\d\.]', '')
order['Sales'] = pd.to_numeric(order['Sales'])

# 2
order['Order.Date'] = pd.to_datetime(order['Order.Date'])
order['Month'] = order['Order.Date'].dt.month
month_quantity = order.groupby(['Month'])['Quantity'].sum()
month_quantity.plot()
# =============================================================================
# month_category = order.groupby(['Category'])['Month']
# month_category.hist()
# plt.hist([month_category, month_quantity], color=['orange', 'green'])
# plt.hist(month_category, bins=20, alpha=0.5, label='x')
# plt.hist(month_quantity, bins=20, alpha=0.5, label='y')
# plt.legend(loc='upper right')
# plt.show()
# month_category.plot()
# type(month_category)
# type(order['Category'])
# =============================================================================
month_category = order.groupby(['Month','Category'])['Quantity'].sum()
month_category.plot(kind='bar')
order.groupby(['Month','Category'])['Quantity'].sum().unstack().plot(kind='line',stacked=True)
order.groupby(['Month','Category'])['Quantity'].sum().unstack().plot(kind='bar',stacked=True)



# 3 a
returns.rename(columns={'Order ID': 'Order_ID'}, inplace=True)
order.rename(columns={'Order.ID': 'Order_ID'}, inplace=True)

merged_df = pd.merge(returns, order, on = 'Order_ID')
profit_loss = merged_df['Profit'].sum()
#profit_loss
# 135035.95

# 3 b
count = list(merged_df['Order_ID'].value_counts())
(merged_df['Order_ID'].value_counts()>1).sum()
#count above 1 = 551
(merged_df['Order_ID'].value_counts()>5).sum()
#count above 5 = 41

# 3 c
regions = (returns['Region'].value_counts())
regions.max()
#highest return region Western Europe       121
subcategory = (merged_df['Sub.Category'].value_counts())
#subcategory = Binders        269
category = (merged_df['Category'].value_counts())
# category Office Supplies    1348


#4

    
    