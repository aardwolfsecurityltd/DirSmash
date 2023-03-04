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
# Directory Enumerator

This Python script searches for directories of a given domain name. It does this by testing all possible directories using a wordlist of common directory names. The script uses multi-threading to speed up the process and includes a progress bar to monitor progress.

## Installation

1. Install Python 3.x
2. Install `requests` module: `pip install requests`
3. Install `tqdm` module: `pip install tqdm`
4. Clone this repository: `git clone https://github.com/username/repo.git`

## Usage

1. Navigate to the directory where the script is located.
2. Run the script: `python directory_enumerator.py`
3. Enter the domain name when prompted (e.g., example.com).
4. Wait for the script to finish running.

## Acknowledgments

This script was inspired by a similar script created by V0re. The default wordlist used in this script is from their repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
