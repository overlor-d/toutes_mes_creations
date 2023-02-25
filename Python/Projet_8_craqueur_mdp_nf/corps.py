import itertools
import string
import time

CHARSET = string.ascii_lowercase + string.ascii_uppercase + string.digits

def crack_password(password, max_length=4, timeout=60):
    start_time = time.time()
    for length in range(1, max_length+1):
        for guess in itertools.product(CHARSET, repeat=length):
            guess = "".join(guess)
            if guess == password:
                elapsed_time = time.time() - start_time
                return guess, elapsed_time
            if time.time() - start_time > timeout:
                return None, None

password = "5689"
guess, elapsed_time = crack_password(password, max_length=len(password), timeout=60)

if guess:
    print(f"Password found: {guess}")
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
else:
    print("Password not found within timeout period.")
