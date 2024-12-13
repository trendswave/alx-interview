def isWinner(x, nums):
    if x <= 0 or not nums:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_game(n, primes):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False

    primes = [i for i in range(n + 1) if is_prime[i]]
    return primes

def play_game(n, primes):
    numbers = set(range(1, n + 1))
    turn = 0  # 0 for Maria, 1 for Ben

    while True:
        prime_found = False
        for prime in primes:
            if prime in numbers:
                prime_found = True
                multiples = set(range(prime, n + 1, prime))
                numbers -= multiples
                break

        if not prime_found:
            return turn == 1

        turn = 1 - turn

# Example usage
x = 3
nums = [4, 5, 1]
print(isWinner(x, nums))  # Output: "Ben"
