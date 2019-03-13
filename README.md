# Acryl-node-services config/binary files
Update repo for acryl-node-services

Branches: 
- master - production branch;
- test - branch for test nodes;
- dev - development branch (use it for localhost).

# Update algorithm
1. Change required files;
2. After files changes please update sha256 checksum by running hash updater:
    ```bash
    python3 sha256_writer.py
    ```
3. Bump updated file version number and url in `versions.json`.

if you made changes for test nodes, set file urls 
in `versions.json` and `config.json` changing `master` to `test` in url path e.g.:

`"https://github.com/acrylplatform/node-services-config/raw/master/acryl.jar?v=5"`

to

`"https://github.com/acrylplatform/node-services-config/raw/test/acryl.jar?v=5"`

don't forget update sha256
