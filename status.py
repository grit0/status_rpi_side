import time
import io,json
import subprocess
import requests
import json
import copy
status={
"basic":{ "hostname" : "hostname -b",
		"distro_name":"uname -s",
		"kernel_version":"uname -v",
		"date":"date",
		"machine":"uname -m",
		"voltage":"vcgencmd measure_volts core |cut -c6-| sed 's/.$//'",
		"temperature":"vcgencmd measure_temp|cut -c6-| sed 's/..$//'",
		"firmware_version":"/opt/vc/bin/vcgencmd version"

},"network":{
                                                                                                                                                                        
			x:{
				"ip" : "/sbin/ifconfig "+x+" | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}'",
				"ip_loopback": "hostname -i",
				"bcast"  : "/sbin/ifconfig "+x+" | grep 'inet addr:' | cut -d: -f3 | awk '{ print $1}'",
				"sub" : "/sbin/ifconfig "+x+" | grep 'inet addr:' | cut -d: -f4 | awk '{ print $1}'",
				"mac"		 :"/sbin/ifconfig "+x+" | grep 'HWaddr' | tr -s ' ' |cut -d' ' -f5",
                                "inet6_global" : "/sbin/ifconfig eth | grep -oP '(?<=addr: ).*?(?=Scope:Global)'",
                                "inet6_link" : "/sbin/ifconfig eth | grep -oP '(?<=addr: ).*?(?=Scope:Link)'",
				"rx_packet"  :"/sbin/ifconfig "+x+" | grep 'RX packet' | cut -d: -f2 | awk '{ print $1}'",
				"tx_packet"  :"/sbin/ifconfig "+x+" | grep 'TX packet' | cut -d: -f2 | awk '{ print $1}'",
				"rx_bytes"   :"/sbin/ifconfig "+x+" | grep 'RX bytes' | cut -d: -f2 | awk '{ print $1$2$3}'",
				"tx_bytes"	 :"/sbin/ifconfig "+x+" | grep 'TX bytes' | cut -d: -f2 | awk '{ print $1$2$3}'"
				} for x in ("eth0","lo","wlan0")
},"physical":{
		"ram":{"total":"free -m  | grep 'Mem' | tr -s ' ' |cut -d' ' -f2",
			"used":"free -m  | grep 'Mem' | tr -s ' ' |cut -d' ' -f3",
			"free":"free -m  | grep 'Mem' | tr -s ' ' |cut -d' ' -f4",
			"shared":"free -m  | grep 'Mem' | tr -s ' ' |cut -d' ' -f5",
			"buffefs":"free -m  | grep 'Mem' | tr -s ' ' |cut -d' ' -f6",
			"cached":"free -m  | grep 'Mem' | tr -s ' ' |cut -d' ' -f7"
		},
		"harddisk":{"size":"df -h |grep 'root' | tr -s ' '|cut -d ' ' -f2 | sed 's/.$//'",
			"used":"df -h |grep 'root' | tr -s ' '|cut -d ' ' -f3 | sed 's/.$//'",
			"avail":"df -h |grep 'root' | tr -s ' '|cut -d ' ' -f4 | sed 's/.$//'",
			"user":"df -h |grep 'root' | tr -s ' '|cut -d ' ' -f5 | sed 's/.$//'"
		},
		"cpu":{"current":"cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq",
			"max":"cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq"
		}
},"peripheral":{
		"hdmi":"tvservice -n",
		"camera":"vcgencmd get_camera | grep -o '.$'",
		"usb":"lsusb |tr -d ':'| awk '$4 > 3 { print $4$7$8$9$10}'",
                "gpio":r"""gpio readall |tr -d " "|awk -F"|" 'NR >= 4 && NR <=23 {print $7"|"$6"|"$5"-"$9"|"$10"|"$11"-"}'""" 
}
}
#print(commands.getoutput(basic["Date"]))
#for key, value in status["basic"].items():
#	status["basic"][key]=commands.getoutput(status["basic"][key])
#print(bGasic)

#for key, value in status["network"]["eth0"].items():
#	status["network"]["eth0"][key]=commands.getoutput(status["network"]["eth0"][key])

#status={basic,network}
def add_geo(current_status):
    geo_url='http://freegeoip.net/json'
    geo_request = requests.get(geo_url)
    json_request =  json.loads(geo_request.text)
    current_status['geo']=json_request
    return current_status

def check_pin(pin,type):                                                                                                                                                                                                             
        GPIO.setmode(GPIO.BOARD)                                                                                                                                                                                                
        GPIO.setup(pin,type)                                                                                                                                                                                               
        return GPIO.input(pin) 

def split_usb(text):
    dic_usb={}
    for usb in text.split('\n'):
        dic_usb[usb[:3]]=usb[3:usb.find("\n")]
    return dic_usb

def split_gpio(text):
    dic_gpio={}
    text=text.replace("\n","").split('-')#delete '\n' from '1||-2||-\n3|1|ALT0-4||-\n5|1|ALT0-6'
    for x in range(0,40):#['1||', '2||', '3|1|ALT0', '4||', '5|1|ALT0', '6']
        dicGpioDetail={}
        listGpioDetail=text[x].split('|')
        dicGpioDetail["value"]=listGpioDetail[1]
        dicGpioDetail["mode"]=listGpioDetail[2]
        dic_gpio[x+1]=dicGpioDetail
    return dic_gpio

def runCommand(dic):
	for key, value in dic.items():
		if isinstance(value, dict):
			runCommand(value)      
		else:
			#dic[key]=commands.getoutput(value)
			dic[key]=subprocess.getoutput(value)
			if dic[key] == '' : # Debug cdicate empty obj in usb
				continue
			#print(value)
			if key is "usb" :
				dic[key]=split_usb(dic[key])
			if key is "gpio" :
                                dic[key]=split_gpio(dic[key]) 
                        



#print(status)
#print("\n",re,">>>>>>>>>>>>")
#time.sleep(5)
#runCommand(re)
#print("\n\n\n<<<<<<<<<<<<<",re)
#print(status)
def getStatus():
    total={}
    re={}
    re=copy.deepcopy(status)
    runCommand(re)
    mac_connect=[]
    add_geo(re)
    for x in ['eth0','lo','wlan0']:
        result=re['network'][x]['mac']
        if  result.find("not found")<0 and result != "":
            mac_connect.append(result)
    
    total={mac_connect[0]:re}
    return total
#print(getStatus())
#print("/n---",status)
#print("\n",re)
#time.sleep(5)
#print("\n\n",getStatus())

