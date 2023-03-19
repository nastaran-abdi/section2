
seconds =int(input("please enter second"))
minutes = int(seconds/60)
seconds = seconds-minutes*60
hour=0
if minutes > 60:
    hour = int(minutes / 60)
    minutes = minutes-hour*60

print(hour,":",minutes,":",seconds)

