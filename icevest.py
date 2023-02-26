#!/usr/bin/env python3
import requests
import time
from datetime import date
import os
import sys

showdict = {"mmo": {"show": "MMO", "url":"http://namillennial.asuscomm.com:6969/NAMillennial", "hours":4},
"bab":{"show":"BowlAfterBowl", "url":"https://stream.bowlafterbowl.com/listen/bowlafterbowl/stream.mp3","hours":5},
"bts":{"show":"BehindTheSchemes", "url":"http://scream.behindthesch3m3s.com/radio/8000/.mp3", "hours":5},
"lotus":{"show":"LotusEffect", "url":"http://stream.lotuseffect.stream:8000/lotus", "hours":3},
"na":{"show":"NoAgenda", "url":"http://listen.noagendastream.com/noagenda", "hours":5},
"hog":{"show":"HogStory", "url":"http://stream.hogstory.net:8000/stream", "hours":4},
"ntr":{"show":"NickTheRat", "url":"https://s2.reliastream.com/proxy/nick1?mp=/stream", "hours":5},
"pc20":{"show":"Podcasting20", "url":"http://listen.noagendastream.com/noagenda", "hours":5},
"gob":{"show":"GrumpyOldBens", "url":"http://listen.noagendastream.com/noagenda", "hours":5},
"re":{"show":"RareEncounter","url":"https://cast1.asurahosting.com/proxy/able/live", "hours":3},
"folk":{"show":"TwoHourFolkHour","url":"http://listen.noagendastream.com/noagenda","hours":2},
"rage":{"show":"PlanetRage","url":"http://listen.noagendastream.com/noagenda","hours":3},
"rnr":{"show":"RocknRollPreshow","url":"http://listen.noagendastream.com/noagenda","hours":2},
"trash":{"show":"Unrelenting","url":"http://listen.noagendastream.com/noagenda","hours":4}
}

x = 0
stream_url = showdict[sys.argv[1].lower()]["url"]
rectime = (3600*showdict[sys.argv[1].lower()]["hours"])
path = "/media/usb/touchfiles/icevest/"
show = showdict[sys.argv[1].lower()]["show"]
start = time.time()

def record(x):
    try:
        while True:
            with open(path + show + "-" +str(date.today())+'-'+str(x)+'.mp3', 'wb') as f:
                r = requests.get(stream_url, stream=True)
                for block in r.iter_content(1024):
                        f.write(block)
                        if time.time()> start + rectime:
                            breakerbreaker19 = True
                            break
                if breakerbreaker19:
                    break
            if breakerbreaker19:
                break
        return True
    except:
        time.sleep(10)
        record(x+1)
record(x)
