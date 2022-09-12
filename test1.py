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



"""
List of all application provide by us
"""
all_apps = ['airsonic', 'couchpotato', 'jackett', 'medusa', 'ombi', 'pydio', 'radarr', 'resilio', 'transmission', 'deluge',
            'jdownloader2', 'mylar3', 'openvpn', 'pyload', 'rapidleech', 'rtorrent', 'ubooquity', 'autodl', 'deluge',
            'jellyfin', 'nextcloud', 'overseerr', 'sonarr', 'znc', 'bazarr', 'emby', 'lazylibrarian', 'plex', 'rapidleech',
            'sabnzbd', 'syncthing', 'btsync', 'filebot', 'lidarr', 'nzbget', 'readarr', 'sickbeard', 'tautulli',
            'filebrowser', 'mariadb', 'nzbhydra2', 'prowlarr', 'qbittorrent', 'requestrr', 'sickchill', ]

sql_apps = ['mariadb', 'filebrowser', 'nextcloud', 'pydio', 'thelounge']

second_instance = ['radarr2', 'sonarr2', 'lidarr2', 'prowlarr2',
                   'whisparr2', 'bazarr2', 'readarr2', 'autobrr', 'navidrome']

second_instance_service = ['autobrr.service', 'navidrome.service', 'prowlarr.service', 'rclone-vfs.service', 'xteve.service',
                           'lidarr.service', 'radarr.service', 'whisparr.service', 'sonarr.service', 'rclone-normal.service', 'mergerfs.service', 'proftpd.service']

arr_apps_list = ['readarr','prowlarr','radarr','sonarr','bazarr','lidarr']

def get_docker_apps( path):
    docker_app = []
    remove_apps = ['backup', 'nginx']
    all_apps = os.listdir(path)
    installed_apps = list(set(all_apps).difference(remove_apps))
    docker_app = list(set(all_apps).intersection(installed_apps))
    for s in sql_apps:
        if s in docker_app:
            docker_app.remove(s)
    for j in second_instance:
        if j in docker_app:
            docker_app.remove(j)
    for w in arr_apps_list:
        if w in docker_app:
            docker_app.remove(w)
    return docker_app

def monitor_jdownloader(apps):
    if "jdownloader2" in apps:
        status = os.popen("ps aux | grep /usr/bin/openbox | grep -v grep ").read()
        count = len(status.splitlines())
        if count == 0:
            os.system("app-jdownloader2 upgrade")
            with open(log_file, "a") as f:
                f.write("\nTIME: "+current_time+"\n")
                f.write('Jdownloader2 was down and has been RESTARTED'+"\n")
            os.system("clear")
            time.sleep(180)
            status = os.popen("ps aux | grep /usr/bin/openbox | grep -v grep ").read()
            count = len(status.splitlines())
            if count <= 0:
                os.system("app-jdownloader2 upgrade")
                with open(log_file, "a") as f:
                    f.write("\nTIME: "+current_time+"\n")
                    f.write('bazarr was down and has been RESTARTED(2nd attempt)'+"\n")
                os.system("clear")
            time.sleep(50)
            status = os.popen("ps aux | grep /usr/bin/openbox | grep -v grep ").read()
            count = len(status.splitlines())
            if count <= 0:
                with open(log_file, "a") as f:
                    f.write(
                "\nScript is unable to FIX your bazarr so please open a support ticket from here - https://my.ultraseedbox.com/submitticket.php\n")
        else:
            pass
    else:
        print("no jdownloader2 installed")


apps = get_docker_apps(apps_path)
monitor_jdownloader(apps)