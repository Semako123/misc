def luhn(creditcard):
    rev_cred = str(creditcard)[::-1]
    checksum = int(rev_cred[0])

    for i in range(1, len(rev_cred)):
        if int(rev_cred[i]) % 2 == 0:
            checksum += int(rev_cred[i])
        else:
            num = int(rev_cred[i]) * 2
            if num > 9:
                num -= 9
            checksum += num
    
    return (checksum, checksum % 10 == 0)

print(luhn(79927398713))