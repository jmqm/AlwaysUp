Keep files alive, using AnonFiles.com.

## About this project.
Using AnonFiles.com, files are uploaded and a corresponding text file is created with the link to the file. If a link goes down, the file is uploaded again and its text file's link is changed.

## docker-compose
```
services:
  alwaysup:
    image: jmqm/alwaysup:latest
    container_name: alwaysup
    network_mode: none
    volumes:
      - /host_files:/files:ro # Read-only
      - /host_links:/links

      - /etc/localtime:/etc/localtime:ro # Container uses date from host.
    environment:
      - DELAY_MINUTES=60
```

## Volumes _(permission required)_
`/files` _(read)_- Files to upload. All files in this directory will be considered.

`/links` _(write)_ - Where to store links to.

### Other info
Thought to create this software because it seemed fun, and in no way do I support the distribution of illegal material. Do not abuse this software.

This project is not associated with AnonFiles.com aside from using its services for file upload.
