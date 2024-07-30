**## Brute Force Password Recovery for Excel and Zip Files (Educational Use Only)**

**Disclaimer:** This script is for educational purposes only. Brute-forcing passwords is illegal without proper authorization. Using this script on files you don't own is strictly prohibited.

**Project Description:**

This script helps you recover forgotten passwords for password-protected Excel (XLSX) and Zip files using a brute-force approach. It tries various combinations of characters until it finds the correct password. However, brute-forcing can be time-consuming and ineffective for complex passwords.

**Target Audience:**

This script is intended for users who understand the risks and limitations of brute-forcing passwords and only want to use it for educational purposes on their own files.

**Dependencies:**

* `itertools`
* `string`
* `io`
* `msoffcrypto`
* `multiprocessing`
* `pyzipper`

**Installation:**

1. Download and install Python ([https://www.python.org/downloads/](https://www.python.org/downloads/)).
2. Install the required libraries using pip:

   ```bash
   pip install itertools string io msoffcrypto multiprocessing pyzipper
   ```

**Usage:**

1. Save the script as `brute_force.py`.
2. Open a command prompt and navigate to the directory where you saved the script.
3. Run the script using the following command:

   ```bash
   python3 brute_force.py
   ```

4. You will be prompted to enter the following information:
    * File path (including filename) of the password-protected file (e.g., `C:/Users/abc/file.xlsx`).
    * Number of processors on your computer (for faster processing, but be mindful of resource usage).
    * File type (1 for Excel or 2 for Zip).

**Important Notes:**

* Brute-forcing passwords can be a time-consuming process. The success rate and speed depend on the password complexity and the number of processors used. There's no guarantee of success, especially for long or complex passwords.
* **This script may run endlessly if the file is not password-protected.**
* Be aware that brute-forcing attacks can be computationally intensive and put a strain on your system's resources.

**Disclaimer (again):** Using this script for malicious purposes is strictly prohibited. Only use it on your own files and with proper authorization.

**Known Issues or Limitations:**

* The script will run indefinitely if you try to recover the password for a non-password-protected file.
* Recovering passwords longer than 8 characters can take a very long time, potentially days, depending on your system's hardware.
* This script is limited to recovering passwords for Excel and Zip files.

**Contributing:**

Currently, there are no formal contribution guidelines. However, if you have any improvements or suggestions, feel free to create a pull request on a forked repository.
