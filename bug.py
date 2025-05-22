# bug.py
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def main():
    x = 10
    y = 0
    print("Result:", divide(x, y))

if __name__ == "__main__":
    main()
