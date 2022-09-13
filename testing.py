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
List of apps installed on user's service
"""

docker_app = []
torrent_client = []
mysql_apps = []
arr_apps = []
second_verify_app = []


"""
List of all application provide by us
"""
all_apps = ['airsonic', 'couchpotato', 'jackett', 'medusa', 'ombi', 'pydio', 'radarr', 'resilio', 'transmission', 'deluge',
            'jdownloader2','mylar3','pyload', 'rapidleech', 'rtorrent', 'ubooquity', 'autodl', 'deluge',
            'jellyfin', 'nextcloud', 'overseerr', 'sonarr', 'znc', 'bazarr', 'emby', 'lazylibrarian', 'plex', 'rapidleech',
            'sabnzbd', 'syncthing', 'btsync', 'filebot', 'lidarr', 'nzbget', 'readarr', 'sickbeard', 'tautulli',
            'filebrowser', 'mariadb', 'nzbhydra2', 'prowlarr', 'qbittorrent', 'requestrr', 'sickchill', ]

sql_apps = ['mariadb', 'filebrowser', 'nextcloud', 'pydio', 'thelounge']

second_instance = ['radarr2', 'sonarr2', 'lidarr2', 'prowlarr2',
                   'whisparr2', 'bazarr2', 'readarr2', 'autobrr', 'navidrome']

second_instance_service = ['autobrr.service', 'navidrome.service', 'prowlarr.service', 'rclone-vfs.service', 'xteve.service',
                           'lidarr.service', 'radarr.service','bazarr.service', 'whisparr.service', 'sonarr.service', 'rclone-normal.service', 'mergerfs.service', 'proftpd.service']

arr_apps_list = ['readarr', 'prowlarr', 'radarr', 'sonarr', 'bazarr', 'lidarr']

"""
Class app_monitor is decalared below with all its functions

"""


class app_monitor():
    def get_docker_apps(self, path):
        docker_app = []
        remove_apps = ['backup', 'nginx']
        all_apps = os.listdir(path)
        installed_apps = list(set(all_apps).difference(remove_apps))
        docker_app = list(set(all_apps).intersection(installed_apps))
        for s in sql_apps:
            if s in docker_app:
                docker_app.remove(s)
            else:
                pass
        for j in second_instance:
            if j in docker_app:
                docker_app.remove(j)
            else:
                pass
        for w in arr_apps_list:
            if w in docker_app:
                docker_app.remove(w)
            else:
                pass
        if "wireguard" in all_apps:
            docker_app.remove("wireguard")
        if "overseerr" in all_apps:
            docker_app.remove("overseerr")
        if "jdownloader2" in all_apps:
            docker_app.remove("jdownloader2")
        return docker_app
    
    def sql_based_apps(self, path):
        remove_apps = ['backup', 'nginx']
        all_apps = os.listdir(path)
        installed_apps = list(set(all_apps).difference(remove_apps))
        for i in sql_apps:
            if i in installed_apps:
                mysql_apps.append(i)
                
    
    def sql_app_monitor(self, apps):
        for i in apps:
            if i == "nextlcoud":
                status = os.popen("ps aux | grep -i '/usr/local/bin/supercronic /etc/crontabs/abc' | grep -v grep".format(i)).read()
                count = len(status.splitlines())    
            else:
                status = os.popen("ps aux | grep -i {} | grep -v grep".format(i)).read()
                count = len(status.splitlines())
            if count <= 0:
                os.system("app-{} restart".format(i))
                with open(log_file, "a") as f:
                    f.write("\nTIME: "+current_time+"\n")
                    f.write('{} was down and has been RESTARTED'.format(i) + "\n")
                    os.system("clear")

                time.sleep(120)
                if i == "nextlcoud":
                    status = os.popen("ps aux | grep -i '/usr/local/bin/supercronic /etc/crontabs/abc' | grep -v grep".format(i)).read()
                    count = len(status.splitlines())    
                else:
                    status = os.popen("ps aux | grep -i {} | grep -v grep".format(i)).read()
                    count = len(status.splitlines())
                if count <= 0:
                    with open(log_file, "a") as f:
                        f.write(
                            "\nScript is unable to FIX your {} so please open a support ticket from here - https://my.ultraseedbox.com/submitticket.php\n".format(i))

            else:
                pass
            
            
monitor = app_monitor()
if __name__ == '__main__':
    apps = monitor.get_docker_apps(apps_path)
    monitor.sql_based_apps(apps_path)
    monitor.sql_based_apps(apps_path)