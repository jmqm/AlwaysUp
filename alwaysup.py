import os
import json
import requests
from time import sleep
from datetime import datetime

DELAY = int(os.environ["DELAY_MINUTES"])
DELAY = 5 if DELAY < 5 else DELAY
API_URL = "https://api.anonfiles.com"

# region Functions


def isURLValid(file_url: str):
    """Checks if a file is still available for download."""
    try:
        if not file_url:
            return False

        file_id = file_url.split("/")[-1]
        response = requests.get(f"{API_URL}/v2/file/{file_id}/info")

        return json.loads(response.content)["status"].lower() == "true"
    except:
        pass

    return ""


def uploadFile(file_location: str):
    """Uploads a file and returns its short url."""
    try:
        file = open(file_location, "rb")
        response = requests.post(f"{API_URL}/upload", files={"file": file})
        responseJson = json.loads(response.content)

        # If not uploaded properly, raise exception.
        if not responseJson["status"]:
            raise

        return responseJson["data"]["file"]["url"]["short"]
    except:
        pass

    return ""


def timestamp():
    """Returns current date and time formatted."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def printf(file: str, message: str):
    print(f"[{timestamp()}] ", end="")

    if file:
        print(f"{file} - ", end="")

    print(message)


def run():
    for file in os.listdir("/files"):
        file_location = f"/files/{file}"
        url_location = f"/links/{file}.txt"

        if not os.path.isfile(file_location):
            continue

        # If url file exists and is valid, skip it; continue otherwise.
        if os.path.exists(url_location):
            url = open(url_location).read()

            urlValid = isURLValid(url)

            if urlValid or len(urlValid) <= 0:
                printf(file, "Link still valid, skipping..." if urlValid else
                             "ERROR Could not check file status, skipping...")
                continue

            printf(file, "Link down, uploading...")

        # Upload file.
        response = uploadFile(file_location)

        if response:
            writer = open(url_location, "w+")
            writer.write(response)

        printf(file, "File uploaded successfully, link file created." if response else
                     "ERROR Could not upload file.")

# endregion


if __name__ == "__main__":
    printf("", "Started")

    while True:
        run()

        printf("", f"Sleeping for {DELAY} minutes.")
        sleep(DELAY * 60)
