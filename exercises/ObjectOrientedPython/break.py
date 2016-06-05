import webbrowser
import time

breaks = 5
timer = 20
while breaks > 0:
    time.sleep(timer)
    webbrowser.open("https://www.google.com.ua/#q=" + str(breaks))
    print(time.ctime())
    breaks-=1
    
    
