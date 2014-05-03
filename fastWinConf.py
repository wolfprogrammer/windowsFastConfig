#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rosete
#
# Created:     02/04/2014
# Copyright:   (c) rosete 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def cmd_output(command):
    """
    Get output from windows command
    """

    from subprocess import Popen, PIPE, STDOUT
    p = Popen(command ,shell=True, stdout=PIPE)
    out= p.communicate()[0]
    return out

def execute(command):
    from subprocess import Popen, PIPE, STDOUT
    Popen(command)


def hostname():
    return cmd_output('hostname')


def emptydir(directory):
    import os
    os.chdir(directory)

    filelist = [ f for f in os.listdir(".") if f.endswith("*") ]
    for f in filelist:
        print f
        #os.remove(f)



control_panel_menu = [
["User Accounts",           "control userpasswords"],
["User Accounts Advanced",  "control userpasswords2"],
["Windows Firewall",        "firewall.cpl" ],
["Connection Manager",      "cmstp" ],
["Internet Options",        "control inetcpl.cpl"],
["Network and Sharing Center", "control ncpa.cpl"],
['Password Properties',      'control password.cpl'],
["Date and time",           "control timedate.cpl"],
["Device Manager",          "devmgmt.msc"],
["Devices and printers",    "control printers" ],
[ "Keyboard Properties", 	"control keyboard"],
["Windows Features control panel.", "OptionalFeatures.exe"],
[ "System Configuration Editor.", "sysedit.exe" ]
]

system_settings_menu = [
["System Properties",       "sysdm.cpl"],
["Advanced System Properties", "SystemPropertiesAdvanced.exe"],
["Advanced System Properties Remote", "SystemPropertiesRemote.exe"],
["Environment Variables", "rundll32.exe sysdm.cpl,EditEnvironmentVariables"],
["Task Scheduller", "taskschd.msc"],
["Power Options",           "control powercfg.cpl"],
["Command Prompt",          "cmd" ],
["Windows Register",        "regedit" ],
["Folder Options",          "control folders"],
['Backup and Restore', 	'sdclt.exe'],
["Program Access and Computer defautls", "ComputerDefaults.exe"],
["Certificate Manager", 	"certmgr.msc"],
[ "Component Services", 	"dcomcnfg"],
["Event Viewer", 	"eventvwr.msc"],
[ "WMI Management",	"wmimgmt.msc"],
[ "Java Control Panel (if installed)", 	"jpicpl32.cpl" ],
[ "Java Control Panel (if installed)", 	"javaws"]

]

tools_menu = [
["Windows Explorer", 	"explorer" ],
["Command Prompt",          "cmd" ],
["Windows Register",        "regedit" ],
["Environment Variables", "rundll32.exe sysdm.cpl,EditEnvironmentVariables"],
["Shared Folders", 	"fsmgmt.msc"],
["Create A Shared Folder Wizard", 	"shrpubw"],

["Windows Script Host", "wscript" ],
["Advanced System Properties/Remote tab", "SystemPropertiesRemote.exe"],

['Connect to a Network Projector', 'NetProj'],
['Presentation Settings', 'PresentationSettings'],
['Connect to a Projector', 'displayswitch'],

["Remote Desktop", 	"mstsc"],
["Windows Remote Assistance", 	"msra"],
["Remote Desktop Sessions", "control.exe /name Microsoft.RemoteAppandDesktopConnections"],
["File Signature Verification Tool", "sigverif"],
["Analyzes and verifies drivers. Command line & GUI.", "verifier.exe"],
["Map Network Drive", "RunDll32.exe shell32.dll,SHHelpShortcuts_RunDLL Connect"],
[ "Network Connections",  "RunDll32.exe shell32.dll,Control_RunDLL ncpa.cpl"],
["Snipping Tool", 	"snippingtool"],
["Problem Steps Recorder", 	"psr"]
]

management_menu = [
["Computer Management", "compmgmt.msc "],
["Disk Management", "diskmgmt.msc"],
["Event Viewer", "eventvwr.msc"],
["Local Users and Groups", "lusrmgr.msc"],
["Local Group Policy Editor ", "gpedit.msc"],
["Local Security Policy ", "secpol.msc"],
["Security Center", 	"wscui.cpl"],
["Performance Monitor", "perfmon.msc"],
[" Services", "services.msc"],
["Shared Folders/MMC", "fsmgmt.msc"],
["Task Scheduler", "control schedtasks"],
["Windows Management Infrastructure", "wmimgmt.msc"],
["Device Manager", "devmgmt.msc"]
]

fast_folder_menu = [
["Windows Explorer", 	"explorer" ],
["Profile", "start shell:Profile"],
["Downloads", "start shell:Downloads"],
["Documents", "start shell:Personal"],
["Favourites", "start  shell:Favorites"],
["Start Menu", "start shell:Start Menu"],
[ "Start Menu Directory", "start shell:Programs"],
[ "Links  	C:\Users\User-Name\Links", "start shell:Links"],

["Recent",     "start shell:Recent"],
[ "Recycle Bin", "start shell:RecycleBinFolder"],

["Templates", "start shell:Templates"],
["Temporary Files", "explorer %temp%"],

["Internet Explorer History", "start shell:History"],

["Send To Folder", "explorer %appdata%\microsoft\windows\sendto"],
["Startup Folder", "start shell:startup"],
["Connection Folder", "start shell:ConnectionsFolder"]

]

"""
 shell:Cookies
 shell:Original Images
 shell:CommonMusic
 shell:My Pictures
 shell:Cache
 shell:Downloads
 shell:CommonDownloads
 shell:AppData

"""

"""

 cmd /c start url

Keyboard Properties 	control keyboard



System Information 	msinfo32

System Restore 	rstrui.exe
Create a System Repair Disc 	recdisc
Credential Backup and Restore Wizard 	credwiz
Stored User Names and Passwords 	credwiz

Data Execution Prevention 	systempropertiesdataexecutionprevention



Remote Desktop Connection 	mstsc






"""



def show_menu_cmd(menu):

    options = [m[0] for m in menu]

    print "Enter the desired option:\n- To exit"

    for idx, opt in enumerate(options):
        print str(idx),"\t",options[idx]

    cmd = ""
    import os
    from subprocess import Popen, PIPE, call



    while True:
        try:
            opt = raw_input(">> ")

            if opt == "-":
                return

            opt = int(opt)

            row  = menu[opt]
            cmd  = row[1]


        except:
            pass

        Popen(cmd , shell=True, stderr=PIPE, stdout=PIPE, stdin=PIPE)
        #os.system(cmd)


    #return cmd

import sys

while True:

    print "Windows Fast Access Tool\n"
    print "1 - Control Panel Access"
    print "2 - System Settings"
    print "3 - Computer Management"
    print "4 - Windows Tools"
    print "5 - Fast Folders"
    print "- - Exit"

    r = raw_input(">> ")

    if r  == '1':
        show_menu_cmd(control_panel_menu)
    elif r == '2':
        show_menu_cmd(system_settings_menu)

    elif r == '3':
        show_menu_cmd(management_menu)

    elif r == '4':
        show_menu_cmd(tools_menu)

    elif r == '5':
        show_menu_cmd(fast_folder_menu)

    elif r == '-':
        sys.exit(0)
    else:
        pass



