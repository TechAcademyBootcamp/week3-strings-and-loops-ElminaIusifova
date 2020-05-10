def calc_tax(sal):
    if sal > 3000:
        return sal*30/100
    return sal*20/100

salary = [1000, 2000, 3000, 4000]

for s in salary:
    tax = calc_tax(s)
    print(tax)