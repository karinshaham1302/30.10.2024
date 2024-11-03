# start

for number in range(2, 200 + 1):
    if number > 1:
        is_prime: bool = True
        for divider in range(2, number ** 0.5 + 1):
            if number % divider == 0:
                is_prime = False
                break
        if is_prime:
            print(number, end=' ')

# stop

# נותן לי שגיאה עקב float ב- range, איך אפשר שזה לא יקרוס?
