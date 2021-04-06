N = int(input(''))
cycle = 0
new = N
while True:
    a = new//10
    b = new % 10
    c = (a+b) % 10
    new = 10 * b + c
    cycle += 1
    if new == N:
        break
print(cycle)



