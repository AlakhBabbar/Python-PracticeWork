from pygame import mixer
import time, datetime


def anychar(value, list):
    for item in list:
        if value== item:
            return item


shedule_eye = ["9:30", "10:00", "21:40", "11:00", "11:30", "12:00","12:30", "13:00", "13:30",
           "14:00", "14:30", "15:00","15:30", "16:00", "16:30", "17:00"]
shedule_exercise = ["9:45","21:40","11:15","12:00", "12:45", "13:30","14:15","15:00","15:45","16:30"]
shedule_water = ["10:00","21:40","12:00","13:00","14:00","15:00","16:00","17:00"]


def soundplay(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)
    stop = input("if you have completed your task type done")
    if stop.lower()== "done":
        mixer.music.stop()
        print("great! you invested some of your precious time for your healthy life!")

def log(var):
    try:
        file = open("health summary.txt", "x")
    except Exception as galti_ho_gai:
        pass
    file = open("health summary.txt", "a")
    if var==shedule_eye:
        file.write(f"you completed EYE EXERCISE task at {datetime.datetime.now()}\n")
    elif var==shedule_exercise:
        file.write(f"you completed PHYSICAL EXERCISE task at {datetime.datetime.now()}\n")
    else:
        file.write(f"you completed DRINKING WATER task at {datetime.datetime.now()}\n")


eye = "eye exercise.mp3"
exercise = "exercise.mp3"
water = "water.mp3"
greetings = int(time.asctime()[11:13])
if 12>greetings:
    print("Hello sir, good morning! don't worry about your health during your work.")
    print("I will remind your health task when you are busy in your work!")

elif 12 < greetings < 18:
    print("Hello sir, good afternoon! don't worry about your health during your work.")
    print("I will remind your health task when you are busy in your work!")

else:
    print("Hello sir, good evening! don't worry about your health during your work.")
    print("I will remind your health task when you are busy in your work!")

while True:
    primary_time = time.asctime()[11:16]
    if primary_time == anychar(primary_time, shedule_eye):
        print("its time for eye exercise!")
        print(f"its {primary_time}")
        soundplay(eye)
        log(shedule_eye)

    if primary_time== anychar(primary_time, shedule_exercise):
        print("its time for physical exercise!")
        print(f"its {primary_time}")
        soundplay(exercise)
        log(shedule_exercise)

    if primary_time== anychar(primary_time, shedule_water):
        print("its time to drink water!")
        print(f"its {primary_time}")
        soundplay(water)
        log(shedule_water)

