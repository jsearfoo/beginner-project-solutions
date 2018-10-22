'''
Whats My Number..?
Only one number available from 1 - 1000 that satisfies below rules,
find it.
RULES:
  - The number has two or more digits.
  - The number is prime.
  - The number does NOT contain a 1 or 7 in it.
  - The sum of all of the digits is less than or equal to 10.
  - The first two digits add up to be odd.
  - The second to last digit is even and greater than 1.
  - The last digit is equal to how many digits are in the number.
'''

def primenum(num):
    for i in range(2,num):
        if num % i ==0: continue
        else:
            return num

for num in range(10,1001):                                              #The number has two or more digits.
    digits = [int(j) for j in str(num)]

    if  1 not in digits and 7 not in digits:                          #The number does NOT contain a 1 or 7 in it.
        if sum(digits) <=10:
            if int((digits[0]+digits[1]))%2 !=0:                       #The first two digits add up to be odd.
                if digits[-2]%2 ==0 and digits[-2]>1:                 #The second to last digit is even and greater than 1.
                    if int(digits[-1])==len(digits):                              #The last digit is equal to how many digits are in the number.
                        print(primenum(num))                            #The number is prime.
