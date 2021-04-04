# import the time module
import time


# define the countdown func.
def config_recovery():
    content = []

    fichier = open("config.txt", "r")
    for line in fichier:
        content.append(line)
    print(content)
    fichier.close()
    timer_s = int(content[0])
    live_min = content[1]
    live_sec = content[2]
    end = content[3]
    return timer_s, live_min, live_sec, end

def plural_management(minute, sec):
    plural_min = "" if int(minute) == (0 or 1) else "s"
    plural_sec = "" if int(sec) == (0 or 1) else "s"
    return plural_min, plural_sec

# define the countdown func.
def countdown(t, msg_wait_min, msg_wait_sec, msg_end):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        minute = '{:01d}'.format(mins)
        second = '{:02d}'.format(secs)
        plural_min, plural_sec = plural_management(minute=minute, sec=second)
        if int(minute) == 0 :
            msg1 = msg_wait_sec.replace("{timer}", timer)
        else:
            msg1 = msg_wait_min.replace("{timer}", timer)
        msg2 = msg1.replace("{min}", minute)
        msg3 = msg2.replace("{sec}", second)
        msg4 = msg3.replace("{plural_min}", plural_min)
        msg = msg4.replace("{plural_sec}", plural_sec)
        print(msg, end='')
        fichier = open("output.txt", "w")
        fichier.write(msg)
        time.sleep(1)
        t -= 1
    print(msg_end)
    fichier = open("output.txt", "r+")
    fichier.truncate(0)
    fichier.write(msg_end)
    fichier.close()


# main
timer, msg_live_min, msg_live_sec, msg_fin = config_recovery()
countdown(t=timer, msg_wait_min=msg_live_min, msg_wait_sec=msg_live_sec, msg_end=msg_fin)
