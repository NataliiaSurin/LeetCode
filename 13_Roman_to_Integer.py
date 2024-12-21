def romanToInt(s: str) -> int:
    romans = ['I', 'V', 'X', 'L', 'C', 'D', 'M', 'IV', 'IX', 'XL', 'XC', 'CD', 'CM']
    integers = [1, 5, 10, 50, 100, 500, 1000, 4, 9, 40, 90, 400, 900]
    integer = 0
    for i in range(0, len(romans)):
        if romans[i] in s:
            integer += integers[i]*s.count(romans[i])
    integer -= s.count('IV') + s.count('IX') + s.count('IV')*5 + s.count('IX')*10
    integer -= (s.count('XL') + s.count('XC')) * 10 + s.count('XL')*50 + s.count('XC')*100
    integer -= (s.count('CD') + s.count('CM')) * 100 + s.count('CD')*500 + s.count('CM')*1000
    return integer


print(romanToInt('MCMXIX'))
