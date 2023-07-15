note: Linux and google-chrome only guide 

Insert username and password in automate_login.py

`sudo apt-get install xvfb`   

Download google-chrome  
Download chromedriver, version should match google-chrome  
`https://chromedriver.chromium.org/downloads`

`unzip chromedriver_linux64.zip`  
`sudo mv chromedriver /usr/bin/chromedriver`  

Install python packages  

`pip3 install -r requirements.txt`  

Add a cron job  

`crontab -e -u ${USER}`  

and add this line inside  

`1 7 * * * python3 INSERT_PATH_HERE/automate_login.py`  


