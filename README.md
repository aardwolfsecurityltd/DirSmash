# DirSmash
A multi-threaded directory scanning tool

This Python script is designed to test subdomains for a given domain name using a wordlist. It is a multi-threaded program that uses a default wordlist to check if subdomains exist for the specified domain name.

Getting Started
To get started with this script, clone the repository and run the following command in the terminal:

Copy code
python subdomain_tester.py
Follow the prompts to enter the domain name and the path to your wordlist file.

By default, the script uses the following wordlist: https://github.com/danielmiessler/SecLists/blob/master/Discovery/DNS/subdomains-top1million-5000.txt

Requirements
This script requires the requests and tqdm modules to be installed. You can install these modules using pip by running the following command:

pip install requests tqdm
This script also uses the multiprocessing module from Python's standard library.

How it Works
The script reads in a wordlist file and generates subdomains by appending each line of the wordlist to the specified domain name. It then tests each subdomain by sending an HTTP GET request with a well-known user-agent. If the response status code is less than 400, the subdomain is considered valid and added to a Set of discovered subdomains.

The program uses multi-processing to test subdomains in parallel, speeding up the process.

At the end of the script, the discovered subdomains are printed to the console.

Default Wordlist
The default wordlist used in this script is the "common.txt" wordlist from the Dirb tool. If the wordlist file is not found, the script will prompt the user to download the default wordlist.

License
This project is licensed under the MIT License - see the LICENSE file for details.
