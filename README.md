# ical2vcal
Python script to convert ical to vcal format. Requires python2 (please somebody rewrite for 3. I'm too lazy and 2to3 doesn't work straight on it)

Original cgi script https://web.archive.org/web/20091231023913/http://code.google.com:80/p/ical2vcal/source/browse/trunk/ical2vcal.cgi

````
[parker@stealth ~]$ python2 ical2vcal.py Downloads/sample.ics 
BEGIN:VCALENDAR
VERSION:1.0
BEGIN:VEVENT
ACTION:DISPLAY
BEGIN:VALARM
DESCRIPTION:Pickup Reminder
DTEND:20130802T110400
DTSTART:20130802T103400
DURATION_SECONDS:1800
END:VALARM
LOCATION:1000 Broadway Ave.\, Brooklyn
SEQUENCE:3
STATUS:CONFIRMED
SUMMARY:Access-A-Ride Pickup
TRIGGER:-PT10M
END:VEVENT
BEGIN:VEVENT
ACTION:DISPLAY
BEGIN:VALARM
DESCRIPTION:Pickup Reminder
DTEND:20130802T203000
DTSTART:20130802T200000
DURATION_SECONDS:1800
END:VALARM
LOCATION:900 Jay St.\, Brooklyn
SEQUENCE:3
STATUS:CONFIRMED
SUMMARY:Access-A-Ride Pickup
TRIGGER:-PT10M
END:VEVENT
END:VCALENDAR
````
