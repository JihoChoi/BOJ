# Quotient & Remainder

# Reference
# https://doorbw.tistory.com/60

N = int(input())

count = 0

while True:
    if N % 5 == 0:
        count = count + (N // 5)
        print(count)
        break;
    else:
        N = N - 3
        count += 1
        if N < 0:
            print("-1")
            break;