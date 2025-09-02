import hashlib
from time import sleep
import urllib.request
import os

print("[*] Author: TH3LILJ4NN47\n[*] Title]: Hash Cracker\n[*] Version: 1.0\n\n")
sleep (1
       )
print("Guideline:\nCross check file path.\n")
sleep(2)

type = str(input("Input type of hash: "))
hash_value = str(input("Enter the hash you want to crack: "))
wordlist = str(input("Enter path to wordlist | Input none if you want default list: "))
if wordlist.lower().strip() == "none":
    url = "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"
    wordlist = "rockyou.txt"
    if not os.path.exists(wordlist):
        urllib.request.urlretrieve(url, wordlist)

def bruteforce_hash(type, hash_value, wordlist):
    with open(wordlist, "r", encoding="utf-8", errors="replace") as wordlist:
        for word in wordlist.readlines():
            plain_text = word.strip()
            try:
                hash_func = getattr(hashlib, type)
            except AttributeError:
                raise ValueError(f"{type} hash type not supported.")
            hash_obj = hash_func(plain_text.encode()) #not hashlib because of getattr
            hash_word = hash_obj.hexdigest()
            if hash_word == hash_value:
                print(f"Found plain text: {plain_text}")
                exit()

        print("Plain text not found.")

bruteforce_hash(type, hash_value, wordlist)