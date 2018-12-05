# Network Tester

### Introduction

This is a simple Python script to test the network speed based on speedtest-cli. It records the current date, time and the ping, download and upload speed in a `speedtest_log.csv` file in the same directory. In case that the `speedtest_log.csv` doesn't exist it will be created otherwise it will just append the results to the end of the file, adding new rows. 

### Configuration 

You can also define the server using the `--server` option to the `speedtest-cli` command. You can get a list of all available servers sorted by their distance to you by executing: 
```
$ speedtest-cli --list > speedtest_servers.txt
```
From this list you can select your own server and add its ID in the `cmd`:

```
speedtest-cli --server ID --simple
```

where ID is the numerical ID of the selected server. This will force `speedtest-cli` to use every time this server. 

### Automation of the Script

In order to run it continuously you can add an entry to the crontab and the interval at each to make the poll like:
```
*/10 * * * * python3 /home/<username>/<path_to_the_script>/network_test.py
``` 
This means that the script will run every 10 minutes. 
