#!/usr/bin/env python3

from gtts import gTTS 
import os
from datetime import datetime, timedelta
import time

enabled = True

if not enabled:
    exit(0)

time.sleep(50)

now = datetime.now()

d = now

mm = str(d.month).zfill(2)

dd = str(d.day).zfill(2)

yyyy = str(d.year)

hour = str(d.hour).zfill(2)

mi = str(d.minute).zfill(2)

ss = str(d.second).zfill(2)

text = None

if mi == "00":
    text = "... ..., o'clock"
else:
    text = "... ..., " + mi +" minutes  with " + ss

language = 'en'

speech = gTTS(text = text, lang = language, slow = False)

speech.save("/tmp/text.mp3")

os.system("mpg123 /tmp/text.mp3")
