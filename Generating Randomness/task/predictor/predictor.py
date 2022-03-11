import random


def compare(s1, s2):
    cnt = 0
    num = len(s1)
    for i in range(num):
        if s1[i] == s2[i]:
            cnt += 1
    p = round(cnt / num * 100, 2)
    print(f'Computer guessed right {cnt} out of {num} symbols ({p} %)')


def predict(ss_in):
    res = triads[random.randint(0, 7)]
    res = '110'
    for i in range(len(ss_in) - 3):
        s3 = ss_in[i:i + 3]
        d = dic[s3]
        res += '0' if d[0] > d[1] else '1'
    return res


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

# ss = '010100101001010101111110001001011000010101010101010010101010101001010010101010001111001010010101010010101010101'

print(f'\nFinal data string:\n{ss}\n')
quads = [ss[i:i+4] for i in range(len(ss))][:-3]
dic = {t: (quads.count(t + '0'), quads.count(t + '1')) for t in triads}
# for k, v in dic.items():
#     print(f'{k}: {v[0]},{v[1]}')

ss_in = input('Please enter a test string containing 0 or 1:\n')
ss_out = predict(ss_in)
print(f'prediction:\n{ss_out}\n')
compare(ss_in[3:], ss_out[3:])
