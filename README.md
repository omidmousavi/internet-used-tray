# internet-used-tray
A program for display total internet used **on the current day** in linux system tray
<br>
<br>
![image](https://github.com/omidmousavi/internet-used-tray/assets/67155909/23ca3680-d669-49ec-83fb-bd3c2e89e43b)


## Dependencies

1. Python
2. [vnstat](https://humdi.net/vnstat/) - ```sudo apt install vnstat``` (for ubuntu)
3. These python libraries are required `pystray`, `PIL`, `subprocess`, `json`, `math`, `time`, `threading`. install requirements with `pip install -r requirements.txt` 

## Setup

1. Clone repository `git clone https://github.com/omidmousavi/internet-used-tray`
2. Setup dependencies
3. Run `python3 ./internet_used_tray.py`

## Suggestions 

- you can add this command to startup system to start program after boot `/usr/bin/python3 /PATH/internet_used_tray.py &`
- you can create a .desktop file for run program with icon (without terminal)
