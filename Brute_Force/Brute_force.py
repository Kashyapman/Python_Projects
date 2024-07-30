import itertools
import string
import io
import msoffcrypto
import multiprocessing
import pyzipper


def load_and_decrypt(file_path, file_type, password):
    if file_type == 1:
        decrypted_workbook = io.BytesIO()
        with open(file_path, 'rb') as file:
            office_file = msoffcrypto.OfficeFile(file)
            try:
                print(password)
                office_file.load_key(password=password)
                office_file.decrypt(decrypted_workbook)
                return password
            except Exception:
                return None

    elif file_type == 2:
        with pyzipper.AESZipFile(file_path, "r", compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as file:
            try:
                print(password)
                file.extractall(pwd=str.encode(password))
                return password
            except Exception:
                return None

    else:
        return None


def brute_force_parallel(file_path, max_length=8, num_processes=4):
    chars = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation

    print("1. Excel\t2.Zip")
    file_types = int(input("Enter file Type number from above List: "))
    if file_types != 1 and file_types != 2:
        return "Password Not found since you gave wrong input try again!"

    def generate_guesses(length):
        return (''.join(guess) for guess in itertools.product(chars, repeat=length))

    with multiprocessing.Pool(processes=num_processes) as pool:
        for length in range(1, max_length + 1):
            guesses = generate_guesses(length)
            results = pool.starmap(load_and_decrypt, [(file_path, file_types, guess) for guess in guesses])
            for password in results:
                if password:
                    return password

    return 'Password not found.'


if __name__ == "__main__":
    file_path = input("Enter file path as: C:/User/abc/file.xlsx\n")
    process = int(input("Enter number of processor your pc has to get result faster: "))
    cracked_password = brute_force_parallel(file_path, num_processes=process)
    print(f"\nYour file password is {cracked_password}")
