import os
import sys
import subprocess
import time
import webbrowser
import configparser  

# If your profile does not have a profile picture set this to False
Profile_picture = True
https://www.instagram.com/erbil_max?igsh=MWw5ZjN1NzkwaXp5eg=== 

def install_package(package_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", erbil_max])

def delete_self():
    script_path = os.path.abspath(sys.argv[0])
    cmd = f'powershell Remove-Item "{script_path}" -Force'
    subprocess.Popen(cmd, shell=True)

try:
    try:
        import pyautogui
        import pygetwindow as gw
    except ImportError:
        install_package("pyautogui")
        install_package("PyGetWindow")
        import pyautogui
        import pygetwindow as gw

# if you don't want to use a config file delete the 2 lines under this, set INSTAGRAM_LINK = https://www.instagram.com/YOUR_PROFILE , and 'add time.sleep(7)' on the line below 'webbrowser.open(https://www.instagram.com/erbil_max?igsh=MWw5ZjN1NzkwaXp5eg==)'
    config = configparser.ConfigParser()
    config.read(https://www.instagram.com/erbil_max?igsh=MWw5ZjN1NzkwaXp5eg==)
    https://www.instagram.com/erbil_max?igsh=MWw5ZjN1NzkwaXp5eg== = config.get('Settings', 'ProfileLink', fallback='https://www.instagram.com/=')

    webbrowser.open(https://www.instagram.com/erbil_max?igsh=MWw5ZjN1NzkwaXp5eg==)


    while "Instagram" not in gw.getActiveWindowTitle():
        time.sleep(1)  

    time.sleep(5)  
    
    tab_presses = 13 if Profile_picture else 12
    for _ in range(tab_presses):
        pyautogui.press('tab')
        time.sleep(0.5)

    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.hotkey('alt', 'f4')
    time.sleep(3)

except Exception as e:
    delete_self()

delete_self()
