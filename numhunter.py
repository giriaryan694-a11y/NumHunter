#!/usr/bin/env python3
import argparse
import random
import itertools
import re
from tqdm import tqdm
from termcolor import colored
from colorama import init
import pyfiglet

init(autoreset=True)

# ------------------------------
# Banner
# ------------------------------
def print_banner():
    banner = pyfiglet.figlet_format("NumHunter")
    print(colored(banner, "cyan"))
    print(colored("   Phone Number Intelligence Generator", "yellow"))
    print(colored("         Made by Aryan Giri", "green"))
    print(colored("------------------------------------------------------\n", "magenta"))

# ------------------------------
# Guess numbers from pattern
# ------------------------------
def guess_numbers(pattern):
    x_count = 0
    for char in reversed(pattern):
        if char.lower() == 'x':
            x_count += 1
        else:
            break
    prefix = pattern[:-x_count] if x_count > 0 else pattern
    return [''.join([prefix]+list(p)) for p in itertools.product('0123456789', repeat=x_count)]

# ------------------------------
# Realistic number generator
# ------------------------------
def detect_repeated_digits(number):
    digits = re.sub(r"\D","",number)
    if len(digits)==0: return None
    freq={}
    for d in digits: freq[d]=freq.get(d,0)+1
    max_digit = max(freq,key=freq.get)
    count = freq[max_digit]
    if count >= len(digits)//2:
        return max_digit
    return None

def generate_realistic(prefix,length,pattern_digit=None):
    if pattern_digit:
        base="".join(random.choice([pattern_digit,str(random.randint(0,9))]) for _ in range(length))
    else:
        base="".join(str(random.randint(0,9)) for _ in range(length))
    return prefix+base

# ------------------------------
# Helper to limit consecutive repeats
# ------------------------------
def has_excessive_repeat(s,max_repeat):
    count=1
    last=''
    for c in s:
        if c==last:
            count+=1
            if count>max_repeat: return True
        else:
            count=1
            last=c
    return False

# ------------------------------
# Main
# ------------------------------
def main():
    print_banner()

    parser = argparse.ArgumentParser(description="NumHunter - Phone Number Generator & Guesser")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-q","--quantity", type=int, help="Number of numbers to generate")
    group.add_argument("-g","--guess", type=str, help="Pattern to guess, e.g. +9199xxxx")
    parser.add_argument("-r","--range", type=int, default=10, help="Length of number after prefix")
    parser.add_argument("-c","--country", type=str, default="+91", help="Country prefix")
    parser.add_argument("-s","--sample", type=str, help="Sample number to detect pattern")
    parser.add_argument("-o","--output", type=str, help="Save output to file")

    args=parser.parse_args()
    numbers=set()

    # ----------------------
    # Guessing Mode
    # ----------------------
    if args.guess:
        print(colored("[+] Running Guess Mode", "cyan"))
        guessed = guess_numbers(args.guess)
        for n in tqdm(guessed, desc="Guess Progress"):
            numbers.add(n)

    # ----------------------
    # Generation Mode
    # ----------------------
    elif args.quantity:
        print(colored("[+] Running Generation Mode", "cyan"))
        pattern_digit = None
        if args.sample:
            pattern_digit = detect_repeated_digits(args.sample)
            if pattern_digit:
                print(colored(f"[Pattern] Detected dominant digit: {pattern_digit}", "yellow"))

        for _ in tqdm(range(args.quantity), desc="Generating Numbers"):
            num = generate_realistic(args.country,args.range,pattern_digit)
            # Optional repeat limit
            while has_excessive_repeat(num[len(args.country):], args.range):
                num = generate_realistic(args.country,args.range,pattern_digit)
            numbers.add(num)

    # ----------------------
    # Write Output
    # ----------------------
    if args.output:
        with open(args.output,"w") as f:
            for n in numbers: f.write(n+"\n")
        print(colored(f"[✔] Saved {len(numbers)} numbers into {args.output}", "green"))
    else:
        for n in numbers: print(n)
    print(colored("\n[✓] Finished!", "green"))

if __name__=="__main__":
    main()
