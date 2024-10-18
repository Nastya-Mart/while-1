my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0

while index < len(my_list) and my_list[index] >= 0:
    elem = my_list[index]
    if elem < 0:
        break
    if elem > 0:
        print(elem)
    index += 1













