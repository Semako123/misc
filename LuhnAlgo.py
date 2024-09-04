def luhn(creditcard):
    rev_cred = str(creditcard)[::-1]
    checksum = int(rev_cred[0])

    for i in range(1, len(rev_cred)):
        if i % 2 == 0:
            checksum += int(rev_cred[i])
            print(rev_cred[i], "here")
        else:
            num = int(rev_cred[i]) * 2
            print(num)
            if num > 9:
                num -= 9
            checksum += num
    
    return (checksum, checksum % 10 == 0)

print(luhn(1234567812345678))