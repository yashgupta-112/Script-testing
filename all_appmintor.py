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
apps_file = '{}/scripts/app_monitor/apps.txt'.format(work_dir)
monitor_app_list = []
rtorrent_log_file = '{}/scripts/app_monitor/torrentapps.txt'.format(work_dir)
docker_log_file = '{}/scripts/app_monitor/docker_apps.txt'.format(work_dir)
torrent_client_list = ['deluge', 'transmission', 'qbittorrent', 'rtorrent']
path = os.getcwd()  # homex/username
apps_path = path + '/.apps'
config_path = path + '/.config'
"""
List of all application provide by us
"""
all_apps = ['airsonic', 'couchpotato', 'jackett', 'medusa', 'ombi', 'pydio', 'radarr', 'resilio', 'transmission', 'deluge',
            'jdownloader2', 'mylar3', 'openvpn', 'pyload', 'rapidleech', 'rtorrent', 'ubooquity', 'autodl', 'deluge', 
            'jellyfin', 'nextcloud', 'overseerr', 'sonarr', 'znc', 'bazarr', 'emby', 'lazylibrarian', 'plex', 'rapidleech',
            'sabnzbd', 'syncthing', 'btsync', 'filebot', 'lidarr', 'nzbget', 'readarr', 'sickbeard', 'tautulli',
            'filebrowser', 'mariadb', 'nzbhydra2', 'prowlarr', 'qbittorrent', 'requestrr', 'sickchill', 'thelounge']


class app_monitor():
    
    def get_docker_apps(self):
        remove_apps = ['backup', 'nginx']
        all_apps = os.listdir(path)
        installed_apps = list(set(all_apps).difference(remove_apps))
        print(installed_apps)
        

monitor = app_monitor()
if __name__ == '__main__':
    monitor.get_docker_apps(apps_path)