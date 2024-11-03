# start

while True:
    try:
        number = int(input('Enter a number [10-99]:'))
        if 10 > number < 99:
            break
        else:
            print('the number is NOT valid')
    except ValueError:
        print('invalid number')

asarot = number // 10
ahadot = number % 10
if ahadot > asarot:
    new_num: int = ahadot * 10 + asarot * 1
else:
    new_num = number

print(f'the number is: {new_num}')

# stop
