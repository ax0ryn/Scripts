import argparse
import subprocess
import sys

def help():
    print("""
FFuF vhost wrapper

Usage:
    python3 vhost-fuzzer.py -d 10.10.10.11 -u http://10.10.10.11 -w /usr/share/wordlist/dirb/common.txt -fs 243

Arguments: 
    -d, --domain       Domain (used in Host header like FUZZ.domain)
    -u, --url          Target URL
    -w, --wordlist     Wordlist for fuzzing
    -fs, --filter-size Filter size for ffuf

Note:
    Colouring is enabled by default.
    """)
    sys.exit(0)

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("-h", "--help", action="store_true")
parser.add_argument("-d", "--domain", required=False)
parser.add_argument("-u", "--url", required=False)
parser.add_argument("-w", "--wordlist", required=False)
parser.add_argument("-fs", "--filter_size", required=False)

args = parser.parse_args()

if args.help or not all([args.domain, args.url, args.wordlist]):
    help()

command = [
    "ffuf",
    "-u", args.url,
    "-w", args.wordlist,
    "-H", f"Host: FUZZ.{args.domain}",
    "-fs", args.filter_size if args.filter_size else "0",
    "-c"
]

try:
    subprocess.run(command)
except KeyboardInterrupt:
    print("\nInterrupted by user.")
except Exception as e:
    print(f"Error: {e}")
