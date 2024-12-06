import os
import requests

# Configuration
YEAR = 2024
DAY = 1  # Change this to the day you want
# Replace with your session cookie
SESSION_COOKIE = "53616c7465645f5f12c69d3462b8e1bd70521f6ab7d69672e1a05650139b78abad9f9e7954266954676949723eca2c01ae1182973707f5df3ae15b5d4eede6c6"
OUTPUT_DIR = "2k24_py/input"  # Directory to store inputs
OUTPUT_FILE = f"day{DAY:02}.txt"


def fetch_input(year, day, session_cookie):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {"Cookie": f"session={session_cookie}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        raise Exception(
            f"Failed to fetch input: {response.status_code} {response.reason}")


def save_to_file(content, output_dir, output_file):
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, output_file)
    with open(file_path, "w") as file:
        file.write(content)
    print(f"Input saved to {file_path}")


if __name__ == "__main__":
    try:
        input_data = fetch_input(YEAR, DAY, SESSION_COOKIE)
        save_to_file(input_data, OUTPUT_DIR, OUTPUT_FILE)
    except Exception as e:
        print(f"Error: {e}")
