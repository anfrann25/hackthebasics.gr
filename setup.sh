#!/bin/bash

set -e

SCRIPT_DIR="$( pwd)"

chmod +x "$SCRIPT_DIR/redeem"

sudo cp "$SCRIPT_DIR/redeem" /usr/local/bin/redeem

echo "✅ redeem installed successfully"
echo "Try: redeem -h"


sudo useradd -m -s /bin/bash flaguser

echo "761496791b8e5990363c1c5107b6a7f44a1340d67b038906af5b08b5bae6d1e3" | sudo tee /home/flaguser/flag.txt >/dev/null

sudo chown flaguser:flaguser /home/flaguser/flag.txt





