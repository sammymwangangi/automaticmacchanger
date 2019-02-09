# automaticmacchanger
Changes MAC address automatically in Linux machines.<br>
## How To Use<br>
1. Download Zip file and extract it in the directory of your choice.<br>
### Run the following commands on your teminal<br>

2. _cd /DIRECTORY YOU EXTRACTED YOU FILE/automaticmacchanger-master_<br>
3. _sudo chmod u+x mac.py_<br>
4. _apt-get install macchanger(if not installed on your OS)_<br>
5. _python mac.py_  OR _python3 mac.py_ <br>
Leave your script running and your MAC address will be changed at every 300sec (5mins).
## Customizing
6. You can change the time at which the MAC address takes to change by editing this line of code <br>
   _time.sleep(300)_  ----> at line 11 <br>
##### 7. You can open the file on a text editor and change _wlan0_ to  _eth0_ or  depending on the type of network you're connected to.

### The change is not permanent, NIC gets its real MAC address back as soon as you restart the PC.
