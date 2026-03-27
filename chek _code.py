# my_listt = [11,33,35,34 ,68,80,50]
# print("before any operation", my_listt)
# my_listt.sort()  # it sorts the list in ascending order.
# print("after operation", my_listt)

# my_list = input("enter the number")
# print("before any operation", my_list)
# my_list = sorted(my_list)  # it sorts the list in ascending order.
# print("after operation", my_list)

# for i in range (50):
#     print("hello world",i)


# def inter_name():
rows = 5

for i in range(1, rows + 1):       # Outer loop → row control
    for j in range(1, i + 1):       # Inner loop → stars
        print("*", end="")
    print()                         # नई लाइन

# inter_name()