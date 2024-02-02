def number_to_words_till_1000(num: int, is_money: bool = False):
    if num > 1000:
        return ''
    last = ["", "нэг", "хоёр", "гурав", "дөрөв", "тав", "зургаа", "долоо", "найм", "ес"] \
        if not is_money else ["", "нэг", "хоёр", "гурван", "дөрвөн", "таван", "зургаан", "долоон", "найман", "есөн"]
    second2last = ["", "арван", "хорин", "гучин", "дөчин", "тавин", "жаран", "далан", "наян", "ерэн"] \
        if is_money or num % 10 != 0 else ["", "арав", "хорь", "гуч", "дөч", "тавь", "жар", "дал", "ная", "ер"]
    third2last = [" ", "нэг зуун", "хоёр зуун", "гурван зуун", "дөрвөн зуун",
                  "таван зуун", "зургаан зуун", "долоон зуун", "найман зуун", "есөн зуун"]
    if num % 100 == 0 and not is_money:
        third2last = list(map(lambda x: x[0:-1], third2last))
    names = [last, second2last, third2last]
    res = ''
    digit_count = 0
    while num > 0:
        res = ' ' + names[digit_count][num % 10] + res
        num = num // 10
        digit_count = (digit_count + 1) % 3
    return ' '.join(res.split())


def number_to_words(num, is_money: bool = False):
    if num == 0:
        return "тэг"
    scales = ["", "мянга", "сая", "тэрбум", "их наяд"]
    digit_count = 0
    res = ''
    while num > 0:
        scale = scales[digit_count] if num % 1000 > 0 else ''
        res = number_to_words_till_1000(num % 1000, digit_count > 0 or is_money) + ' ' + scale + ' ' + res
        digit_count += 1
        num = num // 1000
    res = ' '.join(res.split())
    if res.endswith('мянга') and is_money:
        res = res + 'н'
    return ' '.join(res.split())


if __name__ == '__main__':
    print(number_to_words(97001))
    print(number_to_words(123467545300))
    print(number_to_words(7493849304301))
    print(number_to_words(300, True), 'төгрөг')
    print(number_to_words(300, False))
    print(number_to_words(1000, True), 'төгрөг')
    print(number_to_words(1000, False))
    print(number_to_words(1234, True), 'төгрөг')
    print(number_to_words(1234, False))
