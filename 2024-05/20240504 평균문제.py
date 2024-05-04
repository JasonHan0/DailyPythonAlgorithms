def main():
    N = int(input())
    grades = list(map(int, input().split()))
    print(sum([g / max(grades) * 100 for g in grades]) / N)