# Homework 3
# Author: Nestor Carvallo
# Date: 10/19/2026

number = int(input("Enter a highway number: "))

if number >= 1 and number <= 99:
    if number % 2 == 0:
        print(f"Interstate {number} runs east/west.")
    else:
        print(f"Interstate {number} runs north/south.")
elif number >= 100 and number <= 999 and number % 100 == 0:
    # 200, 300, ... would "serve I-0", which does not exist
    print("Invalid highway number.")
elif number >= 100 and number <= 999:
    primary = number % 100
    direction = "east/west" if primary % 2 == 0 else "north/south"
    print(f"Interstate {number} is an auxiliary highway serving I-{primary}, which runs {direction}.")
else:
    print("Invalid highway number.")
