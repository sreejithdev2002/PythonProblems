my_num = int(input("Enter a number: "))

power_of_my_num = len(str(my_num))

total = 0
i = my_num

while i > 0:
    remainder = i%10
    total += remainder**power_of_my_num
    i = i // 10

if total == my_num:
     print(f"{my_num} is Armstrong number")
else:
    print(f"{my_num} is not Armstrong number")