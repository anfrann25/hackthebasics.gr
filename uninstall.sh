#!/bin/bash

#!/bin/bash

set -e

echo "Linux Challenges Uninstaller"
echo ""

read -p "Are you sure you want to uninstall? (y/N): " CONFIRM

if [[ ! "$CONFIRM" =~ ^[Yy]$ ]]; then
    echo "Cancelled."
    exit 0
fi

echo ""

# Remove redeem command
if [ -f "/usr/local/bin/redeem" ]; then
    sudo rm -f /usr/local/bin/redeem
    echo "✅ Removed redeem command."
else
    echo "ℹ️ redeem is not installed."
fi

# Remove score file
if [ -f "$HOME/.linux_challenges_score" ]; then
    rm -f "$HOME/.linux_challenges_score"
    echo "✅ Removed score file."
else
    echo "ℹ️ Score file already removed."
fi

# Remove progress file
if [ -f "$HOME/.linux_challenges_progress" ]; then
    rm -f "$HOME/.linux_challenges_progress"
    echo "✅ Removed progress file."
else
    echo "ℹ️ Progress file already removed."
fi

# Remove challenge user
if id "flaguser" >/dev/null 2>&1; then
    sudo userdel -r flaguser
    echo "✅ Removed user flaguser."
else
    echo "ℹ️ User flaguser does not exist."
fi

echo ""
echo "🎉 Uninstall completed."
