triads = ["000", "001", "010", "011", "100", "101", "110", "111"]
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
ss = "".join(s)
print(f'\nFinal data string:\n{ss}\n')

quads = [ss[i:i+4] for i in range(len(ss))][:-3]
dic = {t: (quads.count(t + '0'), quads.count(t + '1')) for t in triads}
for k, v in dic.items():
    print(f'{k}: {v[0]},{v[1]}')
