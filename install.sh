if [ "$(which git)" == "" ]; then
	echo "You haven't git"
	sudo apt-get install git -y
fi
if [ "$(which python3)" == "" ]; then
        echo "You haven't python3"
        sudo apt-get install python3 -y
fi
echo "You have python3"
if [ "$(python3 -c "import pyrebase" 2>&1)" != "" 2>&1 ]; then
        echo "Not haven't pyrebase"
        if [ "$(which pip3)" == "" ]; then
                sudo apt-get install python3-pip
        fi
        echo "You have pip3"
        sudo pip3 install pyrebase -y
fi
echo "You have pyrebase module"
git clone https://github.com/grit0/status_rpi_side.git status_app
sudo echo 'alias status="python3 ~/status_app/menu.py"'>> ~/.profile
cd status_app
#----start cron----
crontab -l > status_cron
#echo "* * * * * python3 ~/status_app/__init__.py" >> status_cron
echo "@reboot python3 /home/pi/status_app/__init__.py" >> status_cron
crontab status_cron
rm status_cron

#python3 menu.py
status
