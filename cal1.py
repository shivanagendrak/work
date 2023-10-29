def cal(number):
    if number %2==0:
        return "Even"
    else:
        return "Odd"
for number in range(10):
    print("Number",number,"is",cal(number))
