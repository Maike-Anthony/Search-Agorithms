def binary(n, lst):
    l = len(lst)
    if l == 1 and n != lst[0]:
        return "Not found."
    elif n == lst[l // 2]:
        return "Found."
    elif n < lst[l // 2]:
        return binary(n, lst[:(l // 2)])
    else:
        return binary(n, lst[(l // 2):])

def main():
    lst = [1, 3, 5, 7, 9]
    while True:
        try:
            n = int(input("Number: "))
            break
        except ValueError:
            print("Type an integer.")
    print(binary(n, lst))


if __name__=="__main__":
    main()

