import webbrowser as wb
import datetime

#the time now
now = datetime.datetime.now()

if 3 >= now.day:
    wb.open("https://arbetsformedlingen.se/loggain")
    wb.open("https://arbetsformedlingen.se/platsbanken/annonser?l=3:kuMn_feU_hXx")
else:
    wb.open("https://www.youtube.com/feed/subscriptions")