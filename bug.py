# bug.py
def divide(a, b):
    return a / b

def main():
    x = 10
    y = 0  # bug: zero division error hobe ekhane
    print("Result:", divide(x, y))

if __name__ == "__main__":
    main()
