import os
import time
import datetime
"""
Data and time to store restart time of application
"""

now = datetime.datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")
"""
Variable for location log files
"""
work_dir = os.getcwd()
log_file = '{}/scripts/app_monitor/apps_log.log'.format(work_dir)
torrent_client_list = ['deluge', 'transmission', 'qbittorrent', 'rtorrent']
apps_path = work_dir + '/.apps'
config_path = work_dir + '/bin'
systemd_path = work_dir + '/.config/systemd/user/'

docker_apps = ['readarr','prowlarr','radarr','sonarr','bazarr','lidarr']
all_systemd_files = os.listdir(systemd_path)
print(all_systemd_files)
for i in docker_apps:
    print("app:",i)
    if "{}.service".format(i) in all_systemd_files:
        print("yes")
    else:
        print("no")
    
    # status = os.popen("ps aux | grep -i {} | grep -v grep ".format(i)).read()
    # count = len(status.splitlines())
    # #print("stat",status.splitlines())
    # print(count)