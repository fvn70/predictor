s = []
max = 100
while True:
    print('Print a random string containing 0 or 1:\n')
    s += [c for c in input() if c in '01']
    ln = len(s)
    if ln < max:
        print(f'Current data length is {ln}, {max - ln} symbols left')
    else:
        break
print(f'\nFinal data string:\n{"".join(s)}')
