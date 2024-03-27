def fast_power(base, power):
    if power == 0:
        return 1
    elif power % 2 == 0:
        half_power = fast_power(base, power // 2)
        return half_power * half_power
    else:
        half_power = fast_power(base, (power - 1) // 2)
        return base * half_power * half_power

result = fast_power(2, 5)  
print(result)
