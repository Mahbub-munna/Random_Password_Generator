import datetime
import time
import winsound
alarm_time=input("Enter Alarm time (HH:MM:SS in 24 HOUR FORMAT): ")
print(f"Alarm Set for {alarm_time}")
while True:
    now=datetime.datetime.now().strftime("%H:%M:%S")
    if now==alarm_time:
        print(f"wake up its {now} O'clock....")
        print("Alarm is Ringing....")
        melody=[
            (1000,400),(1200,400),(1400,400),
            (1000,400),(1200,400),(1400,400),
            (1000,600),(1200,600),(1400,600)
        ]
        for freq,dur in melody:
            winsound.Beep(freq,dur)
        break
    time.sleep(1)