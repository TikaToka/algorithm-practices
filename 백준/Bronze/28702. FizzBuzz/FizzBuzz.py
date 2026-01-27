order = [0, 0, 1, 0, 2, 1, 0, 0, 1, 2, 0, 1, 0, 0, 12]

a = input()
b = input()
c = input()
if a.isdigit():
    target = int(a)
    move = 3
elif b.isdigit():
    target = int(b)
    move = 2
else:
    target = int(c)
    move = 1
idx = (int(target) - 1) % 15
nxt = (idx + move) % 15
if order[nxt] == 0:
    print(target + move)
elif order[nxt] == 1:
    print('Fizz')
elif order[nxt] == 2:
    print('Buzz')
else:
    print('FizzBuzz')
    