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

def system_monitor():
    all_systemd_files = os.listdir(systemd_path)
    for i in all_systemd_files:
        print(i)
        if i in second_instance_service:
            status = os.popen("systemctl --user is-failed {}.service".format(i)).read()
            print("app:",i)
            print("status:",status)
            
            
system_monitor()