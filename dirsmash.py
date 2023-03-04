import requests
import os
from tqdm import tqdm
from multiprocessing import Pool

# Define a function to test subdomains
def test_subdomains(subdomain):
    url = f"http://{subdomain}"
    try:
        response = requests.get(url)
        if response.status_code < 400:
            return subdomain
    except:
        pass

# Define a function to get the wordlist file path
def get_wordlist_path():
    wordlist_path = input("Enter the path to your wordlist file (or leave blank to use default): ")
    if wordlist_path == "":
        wordlist_path = "subdomains-top1million-5000.txt"
    return wordlist_path

# Get the domain name from the user
domain_name = input("Enter a domain name (e.g., example.com): ")

# Get the wordlist file path from the user
wordlist_path = get_wordlist_path()

# Check if the wordlist file exists
if not os.path.exists(wordlist_path):
    print(f"Wordlist not found: {wordlist_path}")
    download = input("Do you want to download the default wordlist? (y/n): ")
    if download.lower() == "y":
        # Download the default wordlist
        wordlist_url = "https://github.com/danielmiessler/SecLists/raw/master/Discovery/DNS/subdomains-top1million-5000.txt"
        response = requests.get(wordlist_url)
        with open("subdomains-top1million-5000.txt", "wb") as f:
            f.write(response.content)
        wordlist_path = "subdomains-top1million-5000.txt"
        print(f"Wordlist downloaded: {wordlist_path}")
    else:
        print("Exiting script.")
        exit()

# Open the wordlist file and read the contents
with open(wordlist_path, "r") as f:
    wordlist = f.read().splitlines()

# Use a Set to hold the subdomains discovered
results = set()

# Use multi-processing to test subdomains
pool = Pool(processes=os.cpu_count())
for subdomain in tqdm(wordlist, desc="Testing subdomains"):
    result = pool.apply_async(test_subdomains, args=(f"{subdomain}.{domain_name}",))
    if result.get():
        results.add(result.get())

# Close the multi-processing pool
pool.close()
pool.join()

# Print the results
if len(results) > 0:
    print("Subdomains found:")
    for result in results:
        print(result)
else:
    print("No subdomains found.")
