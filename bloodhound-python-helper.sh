#!/bin/bash

# Prompt user for BloodHound-python info and run the ingestor
# Copied and remade from TeneBrae93

echo -n "Domain (e.g., administrator.htb): "
read domain

echo -n "Username: "
read username

echo -n "Password: "
read -s password
echo

echo -n "IP of Domain Controller: "
read ip_address

# Save current dir
original_dir=$(pwd)

# Run bloodhound-python
cd /home/axoryn/tools/bloodhound/ingestor || exit
python3 bloodhound.py -d "$domain" -u "$username" -p "$password" -gc "$domain" -c all -ns "$ip_address"

# Move loot
mkdir -p ~/.bloodhound/.loot
mv *.json ~/.bloodhound/.loot/ 2>/dev/null

# Return to original dir
cd "$original_dir"

echo "The loot is saved to ~/.bloodhound/.loot"
echo "You're back in: $original_dir"

