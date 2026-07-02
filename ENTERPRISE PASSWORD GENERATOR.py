

import math
import string
import secrets  

print("=== DECODELABS RANDOM ENTROPY ENGINE ACTIVATED ===")
print("Aligned with NIST 2024 security standards.\n")

# --- PHASE 1: INPUT AND VALIDATION ---
while True:
    try:
        
        length_input = input("Enter desired password length (Recommended minimum 15): ").strip()
        password_length = int(length_input)
        
        
        if password_length < 1:
            print("[WARNING] Password length must be at least 1 character.")
            continue
        break
    except ValueError:
        print("[ERROR] Input configuration failure. Please enter a valid integer.")


character_pool = string.ascii_letters + string.digits + string.punctuation
pool_size = len(character_pool)


password_list = [secrets.choice(character_pool) for _ in range(password_length)]


final_password = "".join(password_list)


entropy_bits = password_length * math.log2(pool_size)


if entropy_bits < 64:
    strength_tier = "WEAK (Vulnerable to brute force)"
elif entropy_bits < 80:
    strength_tier = "MEDIUM (Standard account security)"
else:
    strength_tier = "EXCELLENT (Enterprise high-security context)"


print("\n" + "=" * 44)
print("             SECURE LEDGER STATEMENT            ")
print("=" * 44)
print(f"GENERATED CREDENTIAL : {final_password}")
print(f"CHARACTER POOL SIZE  : {pool_size}")
print(f"CALCULATED ENTROPY   : {entropy_bits:.2f} bits")
print(f"SECURITY PROFILE     : {strength_tier}")
print("=" * 44)
print("System successfully synchronized. Ready for Project 4 API architecture.")