import os
import time
from datetime import datetime
"""
Data and time to store restart time of application
"""
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
"""
Variable for location log files
"""
work_dir = os.getcwd()
monitor_app_list = []
rtorrent_log_file = '{}/scripts/app_monitor/torrentapps.txt'.format(work_dir)
docker_log_file = '{}/scripts/app_monitor/docker_apps.txt'.format(work_dir)
torrent_client_list = ['deluge', 'transmission', 'qbittorrent', 'rtorrent']
path = os.getcwd()  # homex/username
apps_path = path + '/.apps'
config_path = path + '/bin'

"""
List of apps installed on user's service
"""

apps = []
torrent_client = []
mysql_apps =[]

sql_apps = ['mariadb','filebrowser','nextcloud','pydio','thelounge']

second_instance = ['radarr2','sonarr2','lidarr2','prowlarr2','whisparr2','bazarr2', 'readarr2', 'autobrr', 'navidrome']

second_instance_service = ['autobrr.service','navidrome.service','prowlarr.service','rclone-vfs.service','xteve.service',
'lidarr.service','radarr.service','whisparr.service','sonarr.service','rclone-normal.service','mergerfs.service','proftpd.service']

"""
List of all application provide by us
"""
all_apps = ['airsonic', 'couchpotato', 'jackett', 'medusa', 'ombi', 'pydio', 'radarr', 'resilio', 'transmission', 'deluge',
            'jdownloader2', 'mylar3', 'openvpn', 'pyload', 'rapidleech', 'rtorrent', 'ubooquity', 'autodl', 'deluge', 
            'jellyfin', 'nextcloud', 'overseerr', 'rutorrent', 'sonarr', 'znc', 'bazarr', 'emby', 'lazylibrarian', 'plex', 'rapidleech',
            'sabnzbd', 'syncthing', 'btsync', 'filebot', 'lidarr', 'nzbget', 'readarr', 'sickbeard', 'tautulli',
            'filebrowser', 'mariadb', 'nzbhydra2', 'prowlarr', 'qbittorrent', 'requestrr', 'sickchill', 'thelounge']

"""
Main function is defined below
"""

class app_monitor():
    def get_docker_apps(self,path):
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
        return docker_app 
    
    def app_dockers(self, apps):
        for i in apps:
            print(i)
                
    
monitor = app_monitor()
if __name__ == '__main__':
    apps = monitor.get_docker_apps(apps_path)
    monitor.app_dockers(apps)