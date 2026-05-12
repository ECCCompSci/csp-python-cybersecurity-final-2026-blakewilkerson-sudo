"""
╔══════════════════════════════════════════════════════════════╗
║        CSP Python & Cybersecurity Final Exam - 2026          ║
║                                                              ║
║  Name:  _______________________________________________      ║
║  Date:  _______________________________________________      ║
╚══════════════════════════════════════════════════════════════╝

GITHUB CLASSROOM INSTRUCTIONS:
  1. This assignment was distributed via GitHub Classroom.
     You should already have your own personal copy of this
     repository created automatically when you accepted the
     assignment link from your teacher.

  2. Complete ALL sections in this file.
     Replace every  # YOUR CODE HERE  comment with working code.
     Do NOT delete any existing code — only ADD your code.

  3. Run this file to check your output:
       python final_exam.py
     Fix any errors before submitting.

  4. Submit by committing and pushing this file to YOUR
     GitHub Classroom repository. Your teacher will see it
     automatically — no email or separate submission needed.

  5. Verify: Visit your repo on GitHub and confirm
     final/final_exam.py shows your completed code.

SCORING:
  Section 1 - Python Basics             [40 pts]
    1A. Variables & Output               (10 pts)
    1B. Grade Calculator Function        (16 pts)
    1C. List Operations                  (14 pts)

  Section 2 - File I/O                  [40 pts]
    2A. Write a File                     (20 pts)
    2B. Read and Search the File         (20 pts)

  Section 3 - Caesar Cipher             [40 pts]
    3A. Encrypt Function                 (20 pts)
    3B. Decrypt Function                 (20 pts)

  Section 4 - Password Strength Checker [40 pts]
    Length Check                          (8 pts)
    Uppercase Check                       (8 pts)
    Lowercase Check                       (8 pts)
    Digit Check                           (8 pts)
    Special Character Check               (8 pts)

  Section 5 - File System & Log Analysis[40 pts]
    5A. Build a Folder Structure         (20 pts)
    5B. Log File Analysis                (20 pts)
  ─────────────────────────────────────────────
  TOTAL                                 [200 pts]
"""

import os

print("=" * 60)
print("  CSP Python & Cybersecurity Final Exam")
print("=" * 60)


# ════════════════════════════════════════════════════════════
# SECTION 1 — Python Basics                         [40 pts]
# ════════════════════════════════════════════════════════════
print("\n--- Section 1: Python Basics ---")

student_name = "Blake"
print(f"{student_name}")
student_grade = int(input("9, 10, 11, 12: "))
favorite_topic = ("cybersecurity")  
print(f"Hi, im {student_name} im in {student_grade} who loves {favorite_topic}")



def letter_grade(score):  
    if score >= 90-100: 
        return 'A'
    elif score >= 80-89:
        return 'B'
    elif score >= 70-79:
        return 'C'
    elif score >= 60-69:
        return 'D'
    else:
        return 'F'
pass

test_scores = [100, 88, 73, 61, 45]
for s in test_scores:
    print(f"  Score {s} -> {letter_grade(s)}")


# ── 1C. List Operations [14 pts] ─────────────────────────
# Given this list of cybersecurity threats:
threats = ["phishing", "malware", "ransomware", "spyware", "DDoS"]


brute_list = []

for c1 in threats:  
    for c2 in threats:
        for c3 in threats:
            guess = c1 + c2 + c3
            brute_list.append(guess)
print(len(brute_list))
print(brute_list[:5])
uppercase_list = [word.upper() for word in threats]
print(uppercase_list)


# ════════════════════════════════════════════════════════════
# SECTION 2 — File I/O                              [40 pts]
# ════════════════════════════════════════════════════════════
print("\n--- Section 2: File I/O ---")

# ── 2A. Write a File [20 pts] ────────────────────────────

with open('cyber_glossary.txt', 'r') as file:
    for line in file:
        print(line.strip()) 




# ════════════════════════════════════════════════════════════
# SECTION 3 — Caesar Cipher                         [40 pts]
# ════════════════════════════════════════════════════════════
print("\n--- Section 3: Caesar Cipher ---")


def encrypt_message(text, shift):
    key = encrypt_message()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def encrypt_message(message):
    key = open("secret.key", "rb").read()
    f = encrypt_message(key)
   
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message
encrypt_message()
secret = encrypt_message("Hello!", 4)
print(secret)
pass
def decrypt_message(text, shift):
    """Decrypts a message using a provided Fernet key."""
    d = decrypt_message
   
    decrypted_bytes = d.text(encrypt_message)
    return decrypted_bytes.decode()
pass



original  = "Cybersecurity Is Fun!"
shift_val = 5
encoded   = encrypt_message(original, shift_val)
decoded   = decrypt_message(encoded, shift_val)
print(f"  Original:  {original}")
print(f"  Encrypted: {encoded}")
print(f"  Decrypted: {decoded}")
print(f"  Match: {original == decoded}")


# ════════════════════════════════════════════════════════════
# SECTION 4 — Password Strength Checker             [40 pts]
# ════════════════════════════════════════════════════════════
print("\n--- Section 4: Password Strength Checker ---")


def is_strong_password(password):
    if len(password) < 10:  
        return False
    if not is_strong_password(r'[A-Z]', password):   
        return False
    if not is_strong_password(r'\d', password): 
        return False
    if not is_strong_password(r'[!@#$%^&*]', password): 
        return False
    return True
pass


# Test passwords (do not change these lines)
test_passwords = [
    "abc",
    "helloworld",
    "Hello123",
    "Secur3!Pass",
    "MyStr0ng!PW",
]

for pw in test_passwords:
    result = is_strong_password(pw)
    status = "STRONG ✅" if result["strong"] else "WEAK ❌"
    print(f"  '{pw}' -> {status}")
    if result["feedback"]:
        for tip in result["feedback"]:
            print(f"      - {tip}")


# ════════════════════════════════════════════════════════════
# SECTION 5 — File System & Log Analysis            [40 pts]
# ════════════════════════════════════════════════════════════
print("\n--- Section 5: File System & Log Analysis ---")

os.makedirs()


security_log = [
    "2026-04-23 07:00 - SUCCESS: alice logged in from 192.168.1.10",
    "2026-04-23 07:02 - FAILED: unknown user 'hacker' from 10.0.0.99",
    "2026-04-23 07:05 - SUCCESS: bob logged in from 192.168.1.11",
    "2026-04-23 07:07 - FAILED: alice wrong password from 192.168.1.10",
    "2026-04-23 07:09 - FAILED: unknown user 'admin' from 10.0.0.99",
    "2026-04-23 07:10 - SUCCESS: charlie logged in from 192.168.1.12",
    "2026-04-23 07:15 - SUCCESS: alice logged in from 192.168.1.10",
    "2026-04-23 07:18 - FAILED: bob wrong password from 192.168.1.11",
]

filename = 'final_exam.py'

success_count = 0
failed_count = 0

print("--- Analyzing Log File ---")

try:
    with open(filename, 'r') as file:
        for line in file:
           
            line = line.strip()
            
          
            if 'SUCCESS' in line:
                success_count += 1
                
            
            elif 'FAILED' in line:
                failed_count += 1
                
                print(f"⚠️ WARNING: {line}")
                
    
    print("\n--- Summary ---")
    print(f"{success_count} successful logins, {failed_count} failed attempts.")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")


# ════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("  Final Exam Complete — Review your output above!")
print("  Remember to commit and push to your GitHub Classroom repo!")
print("=" * 60)
