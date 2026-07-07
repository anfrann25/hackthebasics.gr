import sys
import os
import subprocess

def show_usage():
    print("❌ Usage: htb test <file.py> -l <level>")
    sys.exit(1)

# 1. Έλεγχος ορισμάτων από το htb script
if len(sys.argv) < 3:
    show_usage()

LEVEL = sys.argv[1]
USER_FILE = sys.argv[2]

# 2. Έλεγχος αν υπάρχει το αρχείο του χρήστη
if not os.path.exists(USER_FILE):
    print(f"❌ Error: Το αρχείο '{USER_FILE}' δεν βρέθηκε.")
    sys.exit(1)

# =====================================================================
# ⚡ TEST CASES ΑΝΑ LEVEL
# =====================================================================

# ---------------------------------------------------------------------
# LEVEL 1: Hello World
# ---------------------------------------------------------------------
if LEVEL == "1":
    print(f"🧪 Ξεκινάει ο έλεγχος για το Python Level 1...")
    print("------------------------------------------------")
    
    try:
        # Εκτελούμε το αρχείο του χρήστη και αποθηκεύουμε το output
        result = subprocess.run(
            [sys.executable, USER_FILE], 
            capture_output=True, 
            text=True, 
            timeout=5
        )
        
        # Καθαρίζουμε το output από κενά και αλλαγές γραμμής (.strip())
        user_output = result.stdout.strip()
        
        # Έλεγχος αν ο κώδικας του χρήστη πέταξε κάποιο error
        if result.returncode != 0:
            print("❌ Ο κώδικάς σου περιέχει κάποιο σφάλμα:")
            print(result.stderr)
            sys.exit(1)
            
        # Το αναμενόμενο output (κάνουμε ignore τα κεφαλαία/μικρά για ευκολία του μαθητή)
        expected = "hello world"
        
        if user_output.lower() == expected:
            print(f"✅ Output: '{result.stdout.strip()}'")
            print("\n🎉 [SUCCESS] Συγχαρητήρια! Το πρώτο σου script τρέχει άψογα!")
            print("🔑 FLAG: SFRCe3B5dGgwbl9oM2xsMF93MHJsZF9sMX0=")
        else:
            print(f"❌ Λάθος αποτέλεσμα.")
            print(f"Αναμενόμενο: 'Hello World'")
            print(f"Ο δικός σου κώδικας τύπωσε: '{result.stdout.strip()}'")
            sys.exit(1)
            
    except subprocess.TimeoutExpired:
        print("❌ Error: Ο κώδικάς σου πήρε πάρα πολύ χρόνο για να εκτελεστεί (Timeout).")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Προέκυψε κάποιο απρόσμενο σφάλμα: {e}")
        sys.exit(1)

# ---------------------------------------------------------------------
# LEVEL 2: 
# ---------------------------------------------------------------------
elif LEVEL == "2":
    try:
        result = subprocess.run([sys.executable, USER_FILE], capture_output=True, text=True, timeout=5)
        user_output = result.stdout.strip()
        
        if result.returncode != 0:
            print("❌ Ο κώδικάς σου κράσαρε:\n", result.stderr); sys.exit(1)
            
        if user_output == "HTB{pyth0n_v4r14bl3s_l2}":
            print(f"✅ Output: '{user_output}'")
            print("\n🎉 [SUCCESS] Επιτυχής ένωση μεταβλητών!")
            print("🔑 FLAG: SFRCe3B5dGgwbl92NHIxNGJsM3NfbDJ9")
        else:
            print(f"❌ Το output δεν είναι το σωστό ενωμένο flag.\nΈδωσες: '{user_output}'")
            sys.exit(1)
    except Exception as e:
        print(f"❌ Σφάλμα: {e}"); sys.exit(1)

# ---------------------------------------------------------------------
# LEVEL 3: 
# ---------------------------------------------------------------------
    
elif LEVEL == "3":
    try:
        # Test Case 1: Input 5 -> Expected (5^2)+10 = 35
        res1 = subprocess.run([sys.executable, USER_FILE], input="5\n", capture_output=True, text=True, timeout=5)
        # Test Case 2: Input 10 -> Expected (10^2)+10 = 110
        res2 = subprocess.run([sys.executable, USER_FILE], input="10\n", capture_output=True, text=True, timeout=5)
        
        out1 = res1.stdout.strip()
        out2 = res2.stdout.strip()
        
        if "35" in out1 and "110" in out2:
            print("✅ Test Case 1 (Input: 5 -> Output: 35): Passed!")
            print("✅ Test Case 2 (Input: 10 -> Output: 110): Passed!")
            print("\n🎉 [SUCCESS] Το Keygen σου δουλεύει άψογα!")
            print("🔑 FLAG: SFRCe200dGhfNG5kXzFucHV0X2wzfQ==")
        else:
            print("❌ Τα μαθηματικά ή το casting σου είναι λάθος.")
            print(f"Για input 5 έβγαλες: '{out1}' (Αναμενόμενο να περιέχει 35)")
            print(f"Για input 10 έβγαλες: '{out2}' (Αναμενόμενο να περιέχει 110)")
            sys.exit(1)
    except Exception as e:
        print(f"❌ Σφάλμα: {e}"); sys.exit(1)

# ---------------------------------------------------------------------
# LEVEL 4: 
# ---------------------------------------------------------------------

elif LEVEL == "4":
    try:
        # Δοκιμάζουμε 3 διαφορετικά ports
        res1 = subprocess.run([sys.executable, USER_FILE], input="443\n", capture_output=True, text=True, timeout=5)
        res2 = subprocess.run([sys.executable, USER_FILE], input="80\n", capture_output=True, text=True, timeout=5)
        res3 = subprocess.run([sys.executable, USER_FILE], input="22\n", capture_output=True, text=True, timeout=5)
        
        if res1.stdout.strip().upper() == "ALLOWED" and res2.stdout.strip().upper() == "ALLOWED" and res3.stdout.strip().upper() == "BLOCKED":
            print("✅ Test Port 443 -> ALLOWED: Passed!")
            print("✅ Test Port 80 -> ALLOWED: Passed!")
            print("✅ Test Port 22 -> BLOCKED: Passed!")
            print("\n🎉 [SUCCESS] Το Firewall Rule σετάblockαρε σωστά!")
            print("🔑 FLAG: SFRCe2MwbmQxdDEwbjRsc19mMXIzdzRsbF9sNH0=")
        else:
            print("❌ Το Firewall επιτρέπει ή κόβει λάθος πόρτες.")
            sys.exit(1)
    except Exception as e:
        print(f"❌ Σφάλμα: {e}"); sys.exit(1)

# ---------------------------------------------------------------------
# LEVEL 5: 
# ---------------------------------------------------------------------      

elif LEVEL == "5": 
    try:
        result = subprocess.run([sys.executable, USER_FILE], capture_output=True, text=True, timeout=5)
        lines = result.stdout.strip().split('\n')
        
        # Καθαρίζουμε τυχόν κενά από κάθε γραμμή
        lines = [l.strip() for l in lines if l.strip()]
        
        # Έλεγχος αν τύπωσε ακριβώς 50 γραμμές από το 1 έως το 50
        if len(lines) == 50 and lines[0] == "1" and lines[-1] == "50":
            print("✅ Το loop μέτρησε σωστά από το 1 έως το 50!")
            print("\n🎉 [SUCCESS] Μόλις έκανες brute-force το PIN! Το σωστό ήταν το 42.")
            print("🔑 FLAG: SFRCe2JydXQzX2YwcmMxbmdfdzF0aF9sMDBwc19sNX0=")
        else:
            print(f"❌ Το loop σου δεν τύπωσε ακριβώς τους αριθμούς 1 έως 50.")
            print(f"Σύνολο γραμμών που βρέθηκαν: {len(lines)}")
            sys.exit(1)
    except Exception as e:
        print(f"❌ Σφάλμα: {e}"); sys.exit(1)

# ---------------------------------------------------------------------
# LEVEL 6: 
# ---------------------------------------------------------------------  

elif LEVEL == "6":
    user_dir = os.path.dirname(os.path.abspath(USER_FILE))
    user_module_name = os.path.splitext(os.path.basename(USER_FILE))[0]
    sys.path.append(user_dir)

    try:
        user_module = __import__(user_module_name)
    except Exception as e:
        print(f"❌ Ο κώδικάς σου δεν μπορεί να γίνει import: {e}"); sys.exit(1)

    if not hasattr(user_module, "is_secure"):
        print("❌ Σφάλμα: Δεν βρέθηκε συνάρτηση με το όνομα 'is_secure'.")
        sys.exit(1)
        
    try:
        # Έλεγχος της συνάρτησης με AssertionError
        assert user_module.is_secure("12345") is False, "Απέτυχε: Κωδικός με 5 χαρακτήρες πρέπει να βγάζει False"
        assert user_module.is_secure("password123") is True, "Απέτυχε: Κωδικός με 11 χαρακτήρες πρέπει να βγάζει True"
        assert user_module.is_secure("12345678") is True, "Απέτυχε: Κωδικός με ακριβώς 8 χαρακτήρες πρέπει να βγάζει True"
        
        print("✅ Test '12345' -> False: Passed!")
        print("✅ Test 'password123' -> True: Passed!")
        print("✅ Test '12345678' -> True: Passed!")
        print("\n🎉 [SUCCESS] Η συνάρτηση 'is_secure' περνάει όλα τα validation tests!")
        print("🔑 FLAG: SFRCe2Z1bmN0MTBuNV80cjNfcDB3M3JmdTFfbDZ9")
    except AssertionError as e:
        print(f"❌ {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Σφάλμα κατά την εκτέλεση της συνάρτησης: {e}")
        sys.exit(1)

# ---------------------------------------------------------------------
# LEVEL 7: 
# ---------------------------------------------------------------------  

elif LEVEL == "7":
    # Για να μην εξαρτόμαστε από το αν ο χρήστης έχει το αρχείο τοπικά κατά το τεστ, 
    # ο parser δημιουργεί ένα προσωρινό shadow.txt πριν τρέξει το script του χρήστη!
    mock_file = "shadow.txt"
    with open(mock_file, "w") as f:
        f.write("Xroot:x:0:0:root:/root:/bin/bash\nXbin:x:1:1:bin:/bin:/sbin/nologin\nXHTB_FLAG_IS_HERE\n")
    
    try:
        result = subprocess.run([sys.executable, USER_FILE], capture_output=True, text=True, timeout=5)
        user_output = result.stdout.strip()
        
        # Σβήνουμε το mock αρχείο για να μην αφήνουμε σκουπίδια
        if os.path.exists(mock_file): os.remove(mock_file)
            
        if "HTB_FLAG_IS_HERE" in user_output and not "XHTB_FLAG_IS_HERE" in user_output:
            print("✅ Επιτυχής ανάγνωση και αποκρυπτογράφηση του shadow.txt!")
            print("\n🎉 [SUCCESS] Τα δεδομένα ανακτήθηκαν!")
            print("🔑 FLAG: SFRCe2YxbDNfaDRuZGwxbmdfYjRzMWNzX2w3fQ==")
        else:
            print("❌ Το output περιέχει ακόμα τα 'X' ή δεν διάβασες σωστά το αρχείο.")
            sys.exit(1)
    except Exception as e:
        if os.path.exists(mock_file): os.remove(mock_file)
        print(f"❌ Σφάλμα: {e}"); sys.exit(1)

else: 
    print(f"❌ Το Level {LEVEL} δεν έχει υλοποιηθεί ακόμα στον parser.")
    sys.exit(1)