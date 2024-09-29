def linear(n, lst):
    if len(lst) == 0:
        return
    elif n == lst[0]:
        return 1
    else:
        lst.pop(0)
        try:
            return linear(n, lst) + 1
        except TypeError:
            return

def main():
    while True:
        try:
            n = int(input("Number: "))
            break
        except ValueError:
            print("Type a valid number")

    lst = [5, 9, 10, 23, 0, -6, -46, 15, -2]
    position = linear(n, lst)
    if position == None:
        print("Not found.")
    else:
        print("Number's position in the list:", position)

if __name__=="__main__":
    main()
