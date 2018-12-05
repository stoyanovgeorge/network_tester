import subprocess, shlex, datetime, csv, os

basedir = os.path.abspath(os.path.dirname(__file__))
speedtest_log = os.path.join(basedir, 'speedtest_log.csv')

def curr_date():
    ``` Returns a list containing the date as a first
    component and the time as a second component. The 
    format of the date is DD-MM-YYYY```
    now = datetime.datetime.now()
    now_date = now.strftime("%d-%m-%Y")
    now_time = now.strftime("%H:%M")
    return [now_date, now_time]


def nettest():
    ``` Returns a list containing the date, time, ping time
    download speed and upload speed from the best server```
    cmd = "speedtest-cli --simple"
    result = subprocess.check_output(shlex.split(cmd))
    result = result.decode('ascii').strip()
    lines = result.split('\n')
    res_list = curr_date()
    for line in lines:
	res_list.append(line.split(":")[1].strip())

    return res_list

def csv_write(lst):
    ``` Checks if the speedtest_log file exists, if it doesn't
    it creates it and adds the header row labesl, if it does, 
    it will append the result to the end adding a new row. The
    CSV delimiter is set to be ';' which works well with Excel```
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
