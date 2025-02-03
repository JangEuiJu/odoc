import sys

def generate_pattern(n):
    sb = []
    sb.extend(("G" * n + "..." * n + "\n") * n)
    sb.extend(("." * n + "I" * n + "." * n + "T" * n + "\n") * n)
    sb.extend((".." * n + "S" * n + "." * n + "\n") * n)
    sys.stdout.write("".join(sb))

def main():
    n = int(sys.stdin.readline().strip())
    generate_pattern(n)

if __name__ == "__main__":
    main()