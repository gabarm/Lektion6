def smallest_number(x1,x2,x3):
    return min([x1,x2,x3])

def main():
    numbers = [float(input("nr1: ")),float(input("nr2: ")),float(input("nr3: "))]
    print((smallest_number(*numbers)))
    

if __name__ == "__main__":
    main()