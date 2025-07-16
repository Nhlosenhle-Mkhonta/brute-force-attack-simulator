# Brute Force Attack Simulator  
*A Python tool to demonstrate password cracking techniques and security principles*  

---

##  Overview  
This simulator demonstrates how **brute force attacks** work by systematically guessing passwords. It highlights:  
✅ How attackers exploit weak passwords  
✅ Why password length/complexity matters  
✅ Defensive strategies (2FA, account lockouts, etc.)  

**Use Case**: Educational tool for cybersecurity awareness.  

---

##  How It Works  

###  Core Algorithm  
1. **Generates Combinations**  
   - Uses `itertools.product()` to create all possible character combinations  
   - Progressively tests lengths (e.g., 1-char → 2-char → ... → max_length)  

2. **Attack Simulation**  
   - Tracks attempts and time taken  
   - Checks for password match every 1,000 attempts  

3. **Visualization**  
   - Plots attempts vs. time using `matplotlib`  
   - Compares actual progress vs. theoretical complexity  

###  Security Principles Demonstrated  
| Factor               | Weak Example (`cat`) | Strong Example (`Tr0ub4dour&3v3`) |
|----------------------|----------------------|-----------------------------------|
| **Time to Crack**    | 0.005 seconds        | ~445,000 years*                   |
| **Attempts Needed**  | 1,379                | 1.4 × 10²²                        |
| **Character Pool**   | 26 (lowercase)       | 70+ (mixed case + symbols)        |

> *Assumes 1 billion attempts/second  

---

## How to Use  

### Step 1: Install Requirements  
```bash
pip install matplotlib numpy
```

### Step 2: Configure the Script  
Edit these variables in the script:  
```python
TARGET_PASSWORD = "cat"                  # Password to crack
CHARSET = string.ascii_lowercase         # Options: digits/lowercase/alphanumeric/full
MAX_LENGTH = 5                           # Max password length to attempt
```

### Step 3: Run the Simulation  
```bash
python brute_force_simulator.py
```

### Step 4: Interpret Results  
- **Terminal Output**:  
  ```
  Password cracked: 'cat'
  Total attempts: 2074
  Time taken: 0.001000 seconds
  ```
- **Graph**: Shows attack progress vs. theoretical complexity.

 <img width="1241" height="824" alt="Screenshot 2025-07-16 162207" src="https://github.com/user-attachments/assets/7e6f7a89-5a70-4fd1-9ec6-fe397a0b3ea6" />

---

## Key Security Lessons  
1. **Password Length > Complexity**  
   - 12+ characters recommended even with simple letters  
2. **Avoid Common Patterns**  
   - `Password123` cracks 100,000× faster than `PurpleTurtle73!`  
3. **Enable 2FA**  
   - Renders brute force useless without physical token  

