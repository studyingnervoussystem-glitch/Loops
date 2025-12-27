'''def main():
    meaw(3)

def meaw(n):
    for _ in range(n):
        print("meaw")

main()'''


def main():
    number = get_number()
    meaw(number)

def get_number():
    while True:
        n = int(input("What's n?: "))
        if n > 0:
            break
    return n

def meaw(n):
    for _ in range(n):
        print("meaw")
        
main()