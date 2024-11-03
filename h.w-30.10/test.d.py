#start

signal_a = 0
signal_b = 0
signal_c = 0
signal_d = 0

while True:
    answer = input('Enter your answer a, b, c, d:')
    if answer == 'x':
        break
    if answer == 'a':
            signal_a += 1
    elif answer == 'b':
            signal_b += 1
    elif answer == 'c':
            signal_c += 1
    elif answer == 'd':
            signal_d += 1
    else:
        print('Enter another signal')

anser_singal: list[int] = [signal_a, signal_b, signal_c, signal_d]
print('max answer singal', max(anser_singal))
print('min answer singal', min(anser_singal))
