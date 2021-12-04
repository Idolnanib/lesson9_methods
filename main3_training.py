



def get_index(guests, name):
    if name in guests:
        indx = guests.index(name)
        return indx

    return None

# def test():
#     for i in range(5):
#         if i == 2:
#             return
#         print(i)
#
# test()

guests = ["ivan", "semen", "sonya", "petr"]

name = input("Enter name: ")
print(get_index(guests, name))