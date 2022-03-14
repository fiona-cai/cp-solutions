my_input = input()

while True:
    if my_input == "99999":
        break

    my_sum = int(my_input[0]) + int(my_input[1])

    if my_sum != 0:
        direction = ""
        if my_sum % 2 == 0:
            direction = "right"
        else:
            direction = "left"
    
    print(direction, my_input[2:])
    my_input = input()
