import sys
input = sys.stdin.readline

def main():
    N = int(input());
    if N % 2 != 0: print("SK");
    else: print("CY");

if __name__ == "__main__":
    main()