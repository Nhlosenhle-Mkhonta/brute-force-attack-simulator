import itertools
import time
import string
import matplotlib.pyplot as plt
import numpy as np

def brute_force_attack(target, charset, max_length=8, verbose=False):
    """
    Simulates a brute force attack on a password
    
    Args:
        target (str): The password to crack
        charset (str): Characters to use in guesses
        max_length (int): Maximum password length to attempt
        verbose (bool): Show attack progress
    
    Returns:
        tuple: (found_password, attempts, time_taken, results)
    """
    attempts = 0
    start_time = time.time()
    results = []
    
    # Try all lengths from 1 to max_length
    for length in range(1, max_length + 1):
        if verbose:
            print(f"Trying length {length}...")
        
        # Generate all possible combinations for current length
        for candidate in itertools.product(charset, repeat=length):
            attempts += 1
            candidate_str = ''.join(candidate)
            
            # Check for match every 1000 attempts
            if attempts % 1000 == 0:
                results.append((attempts, time.time() - start_time))
            
            # Found the password
            if candidate_str == target:
                time_taken = time.time() - start_time
                results.append((attempts, time_taken))
                return (candidate_str, attempts, time_taken, results)
    
    # Password not found
    time_taken = time.time() - start_time
    results.append((attempts, time_taken))
    return (None, attempts, time_taken, results)

def plot_results(results, target, charset_size):
    """Visualize attack progress"""
    attempts, times = zip(*results)
    plt.figure(figsize=(10, 6))
    plt.plot(attempts, times, 'b-')
    plt.title(f'Brute Force Attack Progress (Target: "{target}")')
    plt.xlabel('Attempts')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    
    # Add theoretical complexity line
    max_attempts = attempts[-1]
    x = np.linspace(0, max_attempts, 100)
    y = x * (times[-1] / max_attempts)  # Linear approximation
    plt.plot(x, y, 'r--', label='Theoretical Complexity')
    
    plt.legend()
    plt.show()

# Character sets for testing
charsets = {
    "digits": string.digits,
    "lowercase": string.ascii_lowercase,
    "alphanumeric": string.digits + string.ascii_lowercase,
    "full": string.digits + string.ascii_letters + string.punctuation
}

# Simulation parameters
TARGET_PASSWORD = "cat"  # Simple password for demonstration
CHARSET = charsets["lowercase"]  # Character set to use
MAX_LENGTH = 5  # Maximum password length to attempt

# Run simulation
result = brute_force_attack(TARGET_PASSWORD, CHARSET, MAX_LENGTH, verbose=True)

# Display results
password_found, attempts, time_taken, progress_data = result
if password_found:
    print(f"\nPassword cracked: '{password_found}'")
    print(f"Total attempts: {attempts}")
    print(f"Time taken: {time_taken:.6f} seconds")
    plot_results(progress_data, TARGET_PASSWORD, len(CHARSET))
else:
    print("Password not found within given constraints")
