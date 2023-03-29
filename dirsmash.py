import requests
import threading
import os
from tqdm import tqdm
import pyfiglet
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

result = pyfiglet.figlet_format("DirSmash")
print(result)

print('				   		   By Aardwolf Security\n\n')

# Define a function to test directories
def test_directories(domain_name, wordlist, progress, results):
    session = requests.Session()
    retries = Retry(total=3, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retries)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    
    for word in wordlist:
        url = f"http://{domain_name}/{word}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        try:
            response = session.get(url, headers=headers)
            if response.status_code < 500:
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
