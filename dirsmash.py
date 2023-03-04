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

# Open the wordlist file and read the contentsimport requests
import threading
import os
from tqdm import tqdm

# Define a function to test directories
def test_directories(domain_name, wordlist, progress, results):
    for word in wordlist:
        url = f"http://{domain_name}/{word}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        try:
            response = requests.get(url, headers=headers)
            if response.status_code < 400:
                results.append(url)
        except:
            pass
        progress.update(1)

# Get the domain name from the user
domain_name = input("Enter a domain name (e.g., example.com): ")

# Set the default wordlist filename and URL
wordlist_filename = "common.txt"
wordlist_url = "https://github.com/v0re/dirb/raw/master/wordlists/common.txt"

# Check if the wordlist file exists, and download it if not
if not os.path.exists(wordlist_filename):
    print(f"Wordlist not found: {wordlist_filename}")
    download = input("Do you want to download the wordlist? (y/n): ")
    if download.lower() == "y":
        response = requests.get(wordlist_url)
        with open(wordlist_filename, "wb") as f:
            f.write(response.content)
        print(f"Wordlist downloaded: {wordlist_filename}")
    else:
        print("Exiting script.")
        exit()

# Open the wordlist file and read the contents
with open(wordlist_filename, "r") as f:
    wordlist = f.read().splitlines()

# Divide the wordlist into chunks based on the number of threads
num_threads = 40
chunk_size = len(wordlist) // num_threads
chunks = [wordlist[i:i + chunk_size] for i in range(0, len(wordlist), chunk_size)]

# Create a list to hold the threads
threads = []

# Create a progress bar for the total number of directories to test
total_directories = len(wordlist)
progress = tqdm(total=total_directories, desc="Testing directories")

# Create a list to hold the directories discovered
results = []

# Create and start a thread for each chunk of the wordlist
for i in range(num_threads):
    thread = threading.Thread(target=test_directories, args=(domain_name, chunks[i], progress, results))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Close the progress bar
progress.close()

# Print the results
if len(results) > 0:
    print("Directories found:")
    for result in results:
        print(result)
else:
    print("No directories found.")
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
