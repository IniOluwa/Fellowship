# prime number generator

def prime_range(n):
   the_list = range(2, n*20)

   for i in the_list:
       the_list = filter(lambda x: x == i or x % i , the_list)
   
   return the_list

def nth_prime(n):
    if n <= 0:
        return False
    else:
        return prime_range(n)[n - 1]

print nth_prime(1000)