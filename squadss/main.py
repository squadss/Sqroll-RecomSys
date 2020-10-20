import time
from datetime import datetime
t_end = time.time() + 60 * 2
while time.time() < t_end:
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print(current_time)
	time.sleep(5)