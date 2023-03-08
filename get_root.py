import subprocess
import os

OSNAME = 2
OSVERSION = 3
ARCHITECTURE = 14

UAC_DEFAULT = "5"

ADMINISTRATORS_SID = 'S-1-5-32-544'
LOW_INTEGRITY_LEVEL_SID = 'S-1-16-4096'

windows_versions = ["7", "8", "2008", "2012", "10", "11"]


def os_compatibile():
    print("the bypassuac_dornet_profiler working with Windows (7|8|2008|2012|10) [64 bits]")
    print("getting system info ...")

    sysinfo_splited = subprocess.run('systeminfo',capture_output=True).stdout.split(b"\r\n")
    print(sysinfo_splited[OSNAME].decode(), 
        "\n"+sysinfo_splited[OSVERSION].decode(),
        "\n"+sysinfo_splited[ARCHITECTURE].decode())

    for version in windows_versions:
        if version in sysinfo_splited[OSNAME].decode() :
            if "64" in sysinfo_splited[ARCHITECTURE].decode():
                print("windows version suppoerted [ ", version," ] ( 64 bits )")
                return True
    return False

def uac_status():
    print("checking for uac status ...")
    sysregister_splited = subprocess.run("reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System",capture_output=True).stdout.split(b"\r\n")
    if "0x1" in sysregister_splited[8].decode():
        print("uac is enabled.")
        print("checking for uac level ...")

        #TODO:
        #change in to not in

        if UAC_DEFAULT not in sysregister_splited[2].decode():
            print("uac is set to default.")
            return True
        else:
            print("error uac is not set to default")
            return False
    else:
        print("uac is not enabled")
        return False

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
def get_env_vars():
    print(os.getenv('windir'), os.getenv('tmp'))
    return True
    
if os_compatibile():
    if uac_status():
        if in_admin_grp_and_integrity_lvl():
            if get_env_vars():
                print("good")
else:
    print("error windows version is not supported")