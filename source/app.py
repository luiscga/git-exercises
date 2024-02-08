import sys

def main(argv):
    if len(argv) > 1:
        print(f"Hello {argv[1]}")
    else:
        print("Usage: python hello.py")

if __name__ == "__main__":
    main(sys.argv[1:])
