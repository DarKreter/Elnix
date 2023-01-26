Fetching data from Elnix inverter with selenium.
-

**Install requirements:**
```
# install dependencies
sudo apt update
sudo apt install python3 python3-pip xvfb
pip3 install 'selenium<4.0.0' argparse

# Get proper package for your distribution
sudo apt install firefox/firefox-esr-l10n-en-gb 

# Create web driver with webdrivermanager
sudo pip3 install webdrivermanager
sudo webdrivermanager firefox --linkpath /usr/local/bin
```

**Run**:  `./run.sh`

Script emulate firefox site with fake X11 server.
Then it's accessing proper fields with javascript.