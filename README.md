```
pip3 install gtts
sudo apt install mpg123 -y
```

```
crontab -e

# every five minutes                                                            
#4,9,14,19,24,29,34,39,44,49,54,59 * * * * XDG_RUNTIME_DIR=/run/user/$(id -u) /\
home/yamir/bin/python-voice-clock.py                                            
# every minute                                                                  
* * * * * XDG_RUNTIME_DIR=/run/user/$(id -u) /home/yamir/bin/python-voice-clock\
.py
```

