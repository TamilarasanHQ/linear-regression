#GENERATE THE DAILY SALES ARRAY
import numpy as np
import matplotlib.pylab as plt
day = np.arange(365)
trend = 200 + 0.5*day
seasonality = np.linspace(0, 2*np.pi*52, 365)
season = 20*np.sin(seasonality)
noise = np.random.normal(loc=0, scale=15, size=365)
sales = trend + season + noise
#BASIC BUSINESS QUESTIONS
total_daily_sales = np.sum(sales)
avg_daily_sales = np.mean(sales)
best_i = np.argmax(sales)
worst_i = np.argmin(sales)
best_sales = sales[best_i]
worst_sales = sales[worst_i]
month_list = [31,28,31,30,31,30,31,31,30,31,30,31]
cum_month = np.cumsum(month_list)
# i can make this to a function later
m = 0
sum = 0
monthly_totals = []
for i in cum_month:
    n = i
    for j in range(m,n):
        sum += sales[j]
    m = n
    monthly_totals.append(round(float(sum),3))
    sum = 0
kernel = np.ones(7)/7
moving_avg = np.convolve(sales, kernel, mode='valid')
print(moving_avg)