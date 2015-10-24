import webbrowser
import time

number = 1
while number < 4:
    print "wait for 10 seconds"
    time.sleep(10)
    print "10 seconds over"
    webbrowser.open("http://www.youtube.com")
    number = number + 1
