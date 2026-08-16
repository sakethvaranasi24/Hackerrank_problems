from collections import Counter

n = int(input())
shoe = list(map(int, input().split()))
n_cust = int(input())

total = 0
shoe_count = Counter(shoe)

for i in range(n_cust):
    size, price = map(int, input().split())
    if shoe_count[size] > 0:
        shoe_count[size] -= 1
        total += price

print(total)
