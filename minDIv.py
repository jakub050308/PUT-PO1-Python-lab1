dzielna = int(input())

for i in range(1, dzielna+1):
    if dzielna % i == 0:
        print(i)
        break
