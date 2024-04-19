sales_data = [1200, 1500, 1400, 1600, 1800, 1900, 2000, 2200, 2100, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100, 4200, 4300]
print("total days of sales: ",len(sales_data))

# using negative indexing, and assuming after every -7th index is a weekend (sunday is a weekend only)
total = 0
for i in sales_data[ -1: :-7]:
 total += i

print("Total weekand sales:", total, "pkr")