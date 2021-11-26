price = [57.8, 46.51, 97, 88.14, 33, 13, 22.5, 56.25, 60, 99.99]
price_val = []
print(id(price_val))


for i in price:
    val = (str(i).split('.'))
    if len(val) == 1:
        price_val.append(val[0] + ' руб ' + '00 коп')
    elif len(val) == 2:
        price_val.append(val[0] + ' руб ' + val[1].zfill(2) + ' коп')

price_val.sort()

print(id(price_val))
print(", ".join(price_val))

price_new = sorted(price_val, reverse=True)
print(', '.join(price_new))
print(id(price_new))

print(', '.join(sorted(price_new[:5])))