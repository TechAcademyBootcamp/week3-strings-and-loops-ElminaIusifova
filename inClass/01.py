
def report():
    sales_wl = []
    print('Welcome to counting program!')
    day = 0
    while day < 7:
        day += 1
        profit = int(input(f"{day} days how much did you sell: "))
        sales_wl.append(profit)
    print(sales_wl)

    max_profit = max(sales_wl)
    min_profit = min(sales_wl)

    print(f"max profit= {max_profit}")
    print(f"min profit= {min_profit}")

    index_of_max_profit = sales_wl.index(max_profit)
    index_of_min_profit = sales_wl.index(min_profit)
    print(f"max profit was on {index_of_max_profit + 1} day")
    print(f"min profit was on {index_of_min_profit + 1} day")

    summary = 0
    # sum = sum(sales_wl)
    # print(sum)

    for i in sales_wl:
        summary = summary + i
    print(f"all money is {summary}")

    avg = summary / len(sales_wl)
    # print(f"Average is {avg}")
    print('Average is {:.2f}'.format(avg))
    return summary


##################### FIRST WEEK
w1_summary = report()

    ##################### SECOND WEEK
w2_summary = report()

if w1_summary > w2_summary:
    print("Week 1 has more profit")
else:
    print("Week 2 has more money")


