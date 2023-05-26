# <ASSIGNMENT 1.5: Document the sieve method>
def sieve(upper_limit):
    primes = [True]*(upper_limit + 1)
    primes[0] = primes[1] = False # Cannot find postive integrate number smaller than 1

    for (i, isprime) in enumerate(primes): #Judge if it is a prime number. If ture, test if it is the largest prime number. If false, turn to next number.
        if isprime:
            last_prime = i # Record the largest prime number.
            for n in range(i**2, upper_limit + 1, i): #If n is a prime, all of the numbers(n * prime number) are not a prime.
                primes[n] = False # Record the result, the loop will end when false show in column.
    
    return last_prime #output result
# <\ASSIGNMENT 1.5>


if __name__ == "__main__":
    upper_limit = input("Upper limit: ")
    print(f"Highest prime up to (and including) limit: {sieve(int(upper_limit))}")