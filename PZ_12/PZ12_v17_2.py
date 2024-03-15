#Составить генератор (yield), который переведёт символы строки из верхнего регистра в нижний.

line = "ПриВет, чЕреЗ тРи мЕСяца я сЪеду нА квАрТиРУ!"

def lower_generator(str):
    for char in str:
        if char.isupper():
            yield char.lower()
        else:
            yield char

result = ''.join(lower_generator(line))
print(result)
