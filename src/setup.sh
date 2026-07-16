#!/bin/bash
set -e

SCRIPT_DIR="$(pwd)"

# Δίνουμε δικαιώματα εκτέλεσης στα Bash scripts
chmod +x "$SCRIPT_DIR/htb"
chmod +x "$SCRIPT_DIR/redeem"

# Αντιγραφή όλων στο /usr/local/bin για να είναι διαθέσιμα global
sudo cp "$SCRIPT_DIR/htb" /usr/local/bin/htb
sudo cp "$SCRIPT_DIR/redeem" /usr/local/bin/redeem
sudo cp "$SCRIPT_DIR/test.py" /usr/local/bin/test.py


echo "✅ HackTheBasics Suite installed!"
echo "Now you can use: htb test OR htb redeem"

# Η δική σου λογική για τον flaguser (αν δεν υπάρχει, τον φτιάχνει)
if ! id "flaguser" &>/dev/null; then
    sudo useradd -m -s /bin/bash flaguser
    echo "761496791b8e5990363c1c5107b6a7f44a1340d67b038906af5b08b5bae6d1e3" | sudo tee /home/flaguser/flag.txt >/dev/null
    sudo chown flaguser:flaguser /home/flaguser/flag.txt
fi