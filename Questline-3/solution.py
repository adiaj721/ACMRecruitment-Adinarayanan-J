Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
... #if we list all the natural numbers below  10 that are multiples of  3 or 5,we get 3,5,6,9 . The sum of these multiples is 23  
... #Find the sum of all the multiples of 3 or 5 below 1000
... 
... total_sum = 0
... for number in range(1000):
...     if number % 3 == 0 or number % 5 == 0:
...         total_sum += number
... print("The sum of all multiples of 3 or 5 below 1000 is:", total_sum)
... 
... 
... # 2520 is the smallest number that can be divided by each of the numbers from   1 to  10 without any remainder. 
... #What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?
... 
... import math
... def lcm(a, b):
...     return abs(a * b) // math.gcd(a, b)
... result = 1
... for i in range(1, 21):
...     result = lcm(result, i)
... 
... print("The smallest positive number evenly divisible by all the numbers from 1 to 20 is:", result)
