Automatic PDF certificates creation from .xml files with Firefox
-

**Install requirements:**
```
# install dependencies
sudo apt update
sudo apt install python3 python3-pip xvfb
pip3 install 'selenium<4.0.0'

# Get proper package for your distribution
sudo apt install firefox/firefox-esr-l10n-en-gb 

# Create web driver with webdrivermanager
sudo pip3 install webdrivermanager
sudo webdrivermanager firefox --linkpath /usr/local/bin
```

**Run**:  `./WebsiteMaker.py`

Remember to have actual geckodriver for firefox.

File "strona.txt", should be in upper directory with login and password to cert site on two last lines.