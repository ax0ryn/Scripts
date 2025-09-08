#!/bin/bash 

# really simple bash script to add entries to /etc/hosts quickly

read -p "enter IP address: " ip
read -p "enter hostname(s) (space-separated if multiple): " hostnames

# Append to /etc/hosts
echo "$ip $hostnames" | sudo tee -a /etc/hosts

echo "Entry added: $ip $hostnames"
