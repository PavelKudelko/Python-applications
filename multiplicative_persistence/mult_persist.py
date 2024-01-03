print("Program starting.")
print("\nCheck multiplicative persistence.")
number = (input("Insert integer: "))
result = 1
cnt = 0
while len(str(number)) != 1:
    number = str(number)
    for i in range(len(number)):
        result *= int(number[i])
        if i != len(number) - 1:
            print(number[i], end=" * ")
        else:
            print(number[i], "=", result)
            number = result
            result = 1
            cnt += 1
print(f"This program took {cnt} step(s)")
print("\nProgram ending.")
