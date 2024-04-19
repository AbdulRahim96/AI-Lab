daily_expenses = [80, 100, 90, 120, 110, 130, 70, 150, 140, 160, 200, 180, 190, 210, 220, 250, 240, 230, 270, 260, 280, 300, 320, 310, 340, 330, 350, 370, 360, 380]

# using negative indexing, and assuming after every -7th index is a weekend (sunday is a weekend only)
total = 0
for i in daily_expenses[ -1: :-7]:
 total += i

print("Total expenses:", total, "pkr")