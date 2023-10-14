import requests
import subprocess


def download_python_file(url, filename):
    """Downloads a Python file from a URL.

    Args:
        url: The URL of the Python file.
        filename: The name of the Python file to save to.
    """

    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)


def execute_python_file(filename):
    """Executes a Python file.

    Args:
        filename: The name of the Python file to execute.
    """

    subprocess.run(["python", filename])

def run_file(url):
    # Download the Python file.
    download_python_file(url, "python_file.py")

    # Execute the Python file.
    execute_python_file("python_file.py")

run_file("https://drive.google.com/drive/u/0/folders/1tOME6insCy7sQ7-7ltr9krjN-mr6F0i1")