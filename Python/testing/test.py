sales_data = [1200, 1500, 1400, 1600, 1800, 1900, 2000, 2200, 2100, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100, 4200, 4300]

# Identify weekend days based on higher sales figures
weekend_start_index = sales_data.index(max(sales_data))
weekend_end_index = sales_data.index(max(sales_data)) + 1
print("weekend_start_index:", weekend_start_index)

# Slice the list to extract weekend sales using negative indexing
weekend_sales = sales_data[weekend_start_index:weekend_end_index]

print(sales_data[weekend_start_index])

# Calculate the total sales for the weekends
total_weekend_sales = sum(weekend_sales)

print("Weekend sales figures:", weekend_sales)
