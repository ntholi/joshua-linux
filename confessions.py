import pynotify
import time
import random

print("Running Confessions...");
lines = [line.rstrip('\n') for line in open('confessions-power') if line.strip()]
print("Successfully loaded %d confessions" %len(lines));
icon = "/home/itadmin/custom-scripts/confessions/icon.jpg"
pynotify.init("Confessions")
while True:
	time.sleep(10); #wait 5 seconds
	i = random.randint(0, len(lines)-1)
	body, title = lines[i].split('(');
	title = title.replace(")", "")
	pynotify.Notification(title, body, icon).show()
	print("- {0:s} ({1:s})".format(body,title)); 
	time.sleep(15 * 60); #wait 15 minutes
