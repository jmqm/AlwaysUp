import os
import json
import requests
from datetime import datetime

API_URL = "https://api.anonfiles.com"

#region Helper Methods

def isURLValid(file_url: str):
    """Checks if a file is still available for download."""
    try:
        file_id = file_url.split("/")[-1]

        response = requests.get(f"{API_URL}/v2/file/{file_id}/info")
        return json.loads(response.content)["status"]
    except:
        return False

def uploadFile(file_location: str):
    """Uploads a file and returns its short url."""
    file = open(file_location, "rb")

    response = requests.post(f"{API_URL}/upload", files = { "file": file })
    responseJson = json.loads(response.content)

    # If not uploaded properly, return an empty string.
    if not responseJson["status"]:
        return ""
    
    return responseJson["data"]["file"]["url"]["short"]

def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#endregion

for file in os.listdir("/files"):
    file_location = f"/files/{file}"
    url_location = f"/links/{file}.txt"

    # If the file is not a file, skip it.
    if not os.path.isfile(file_location):
        continue

    # If url file exists and is valid, skip it; continue otherwise.
    if os.path.exists(url_location):
        url = open(url_location).read()

        if isURLValid(url):
            print(f"[{timestamp()}] {file} - Link still valid, skipping...")
            continue

    # Upload file.
    response = uploadFile(file_location)

    if response:
        open(url_location, "w+").write(response)

        print(f"[{timestamp()}] {file} - File uploaded successfully, link file created.")
    else:
        print(f"[{timestamp()}] {file} - ERROR Could not upload file.")

print("Finished processing all files.")