import subprocess, shlex, datetime, csv, os

basedir = os.path.abspath(os.path.dirname(__file__))
speedtest_log = os.path.join(basedir, 'speedtest_log.csv')

def curr_date():
	now = datetime.datetime.now()
	now_date = now.strftime("%d-%m-%Y")
	now_time = now.strftime("%H:%M")
	return [now_date, now_time]


def nettest():
	cmd = "speedtest-cli --simple"
	result = subprocess.check_output(shlex.split(cmd))
	result = result.decode('ascii').strip()
	lines = result.split('\n')
	res_list = curr_date()
	for line in lines:
		res_list.append(line.split(":")[1].strip())

	return res_list

def csv_write(lst):
	if os.path.isfile(speedtest_log):
		with open(speedtest_log, "a") as log:
			writer = csv.writer(log, delimiter=';')
			writer.writerow(lst)
	else:
		with open(speedtest_log, "w") as log:
			writer = csv.writer(log, delimiter=';')
			writer.writerow(['Date', 'Time', 'Ping', 'Download', 'Upload'])
			writer.writerow(lst)
		


csv_write(nettest())
