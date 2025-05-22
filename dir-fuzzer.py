import argparse
import subprocess
import sys

def help():
    print("""
FFuF directory fuzzer wrapper

Usage:
    python3 dir-fuzzer.py -u http://10.10.10.11 -w /usr/share/wordlists/dirb/common.txt -fs 4242

Arguments: 
    -u, --url          Base URL (e.g., http://10.10.10.11)
    -w, --wordlist     Path to wordlist
    -fs, --filter-size (Optional) Response size to filter out (e.g., 4242)

Note:
    Colouring is enabled by default.
    FUZZ placeholder is automatically appended to the end of the URL.
    """)
    sys.exit(0)

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("-h", "--help", action="store_true")
parser.add_argument("-u", "--url", required=False)
parser.add_argument("-w", "--wordlist", required=False)
parser.add_argument("-fs", "--filter_size", required=False)

args = parser.parse_args()

if args.help or not all([args.url, args.wordlist]):
    help()

url = args.url
if not url.endswith("/FUZZ"):
    if not url.endswith("/"):
        url += "/"
    url += "FUZZ"

command = [
    "ffuf",
    "-u", url,
    "-w", args.wordlist,
    "-c"
]

if args.filter_size:
    command += ["-fs", args.filter_size]

try:
    subprocess.run(command)
except KeyboardInterrupt:
    print("\nInterrupted by user.")
except Exception as e:
    print(f"Error: {e}")
