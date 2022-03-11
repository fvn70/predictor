import random
import re


def compare(s1, s2):
    global sum
    cnt = 0
    num = len(s1)
    for i in range(num):
        if s1[i] == s2[i]:
            cnt += 1
            sum -= 1
        else:
            sum += 1
    p = round(cnt / num * 100, 2)
    print(f'Computer guessed right {cnt} out of {num} symbols ({p} %)')
    print(f'Your balance is now ${sum}\n')


def predict(ss_in):
    res = triads[random.randint(0, 7)]
    res = '110'
    for i in range(len(ss_in) - 3):
        s3 = ss_in[i:i + 3]
        d = dic[s3]
        res += '0' if d[0] > d[1] else '1'
    return res


def make_dic():
    global dic
    s = []
    max = 100
    while True:
        print('Print a random string containing 0 or 1:\n')
        s += [c for c in input() if c in '01']
        ln = len(s)
        if ln < max:
            print(f'The current data length is {ln}, {max - ln} symbols left')
        else:
            break
    ss = "".join(s)

    print(f'\nFinal data string:\n{ss}\n')
    quads = [ss[i:i+4] for i in range(len(ss))][:-3]
    dic = {t: (quads.count(t + '0'), quads.count(t + '1')) for t in triads}


triads = ["000", "001", "010", "011", "100", "101", "110", "111"]
dic = {}
sum = 1000


def main():
    print('''
    Please give AI some data to learn...
    The current data length is 0, 100 symbols left''')
    make_dic()
    print('''
    You have $1000. Every time the system successfully predicts your next press, you lose $1.
    Otherwise, you earn $1. Print "enough" to leave the game. Let's go!
    ''')

    while True:
        ss_in = input('Print a random string containing 0 or 1:\n')
        if ss_in == 'enough':
            break
        if not re.match('[01]+', ss_in):
            continue
        ss_out = predict(ss_in)
        print(f'prediction:\n{ss_out}\n')
        compare(ss_in[3:], ss_out[3:])

    print('Game over!')


if __name__ == '__main__':
    main()
