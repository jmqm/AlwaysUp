># Archived
> AnonFiles.com has decided to shut down, this program is no longer working in its current state (2023/09/22).

Keep files alive, using AnonFiles.com.

## About this project
Using AnonFiles.com, files are uploaded and a corresponding text file is created with the link to the file. If a link goes down, the file is uploaded again and its text file's link is changed.

## docker-compose
```
services:
  alwaysup:
    image: jmqm/alwaysup:latest
    container_name: alwaysup
    volumes:
      - /host_files:/files:ro # Read-only
      - /host_links:/links

      - /etc/localtime:/etc/localtime:ro # Container uses date and time from host.
    environment:
      - DELAY_MINUTES=60 # Minimum 5 minutes.
      # - TZ=Asia/Tokyo # Alternative to mounting /etc/localtime.
```

## Volumes _(permission required)_
`/files` _(read)_ - Files to upload. All files in this directory will be considered.

`/links` _(write)_ - Where to store links to.

### Other info
Thought to create this software because it seemed fun. In no way do I support the distribution of illegal material, this software was not made for that. Do not abuse this software, or else ![monkaS](https://cdn.betterttv.net/emote/59ca6551b27c823d5b1fd872/1x).

This project is not associated with AnonFiles.com aside from using its services for file upload.
