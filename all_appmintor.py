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
List of apps installed on user's service
"""

docker_app = []
torrent_client = []
mysql_apps =[]

sql_apps = ['mariadb','filebrowser','nextcloud','pydio']


"""
List of all application provide by us
"""
all_apps = ['airsonic', 'couchpotato', 'jackett', 'medusa', 'ombi', 'pydio', 'radarr', 'resilio', 'transmission', 'deluge',
            'jdownloader2', 'mylar3', 'openvpn', 'pyload', 'rapidleech', 'rtorrent', 'ubooquity', 'autodl', 'deluge', 
            'jellyfin', 'nextcloud', 'overseerr', 'sonarr', 'znc', 'bazarr', 'emby', 'lazylibrarian', 'plex', 'rapidleech',
            'sabnzbd', 'syncthing', 'btsync', 'filebot', 'lidarr', 'nzbget', 'readarr', 'sickbeard', 'tautulli',
            'filebrowser', 'mariadb', 'nzbhydra2', 'prowlarr', 'qbittorrent', 'requestrr', 'sickchill', 'thelounge']


class app_monitor():
    
    def get_docker_apps(self,path):
        remove_apps = ['backup', 'nginx']
        all_apps = os.listdir(path)
        installed_apps = list(set(all_apps).difference(remove_apps))
        for i in installed_apps:
            if i in all_apps:
                docker_app.append(i)
        for s in sql_apps:
            #print(s)
            if s in docker_app:
                docker_app.remove(s)
            
    def sql_based_apps(self,path):
        remove_apps = ['backup', 'nginx']
        all_apps = os.listdir(path)
        installed_apps = list(set(all_apps).difference(remove_apps))
        for i in sql_apps:
            if i in installed_apps:
                mysql_apps.append(i)
        print(mysql_apps)        
        
        
    def get_torrent_clients(self,path):
        remove_config = ['systemd']
        all_configs = os.listdir(path)
        all_torrent_clients = list(set(all_configs).difference(remove_config))
        if "rtorrent" in all_torrent_clients:
            torrent_client.append('rtorrent')
        if "deluge" in all_torrent_clients:
            torrent_client.append('deluge')
        if "qBittorrent" in all_torrent_clients:
            torrent_client.append('qbittorrent')
        if "transmission-daemon" in all_torrent_clients:
            torrent_client.append('transmission')

    def Monitor_Webserver(self):
        status = os.popen("ps aux | grep -i nginx")
        count = len(status.readlines())
        if count <= 2:
                os.system("app-nginx restart")
                
    def monitor_docker_app(self,apps):
        for i in apps:
            status = os.popen("ps aux | grep -i {}".format(i)).read()
            count = len(status.splitlines())
            if count <= 2:
                os.system("app-{} upgrade".format(i))
                with open(docker_log_file, "a") as f:
                    f.write("\nTIME: "+current_time+"\n")
                    f.write('{} was down and has been RESTARTED'.format(i))
                    os.system("clear")
            else:
                pass
            time.sleep(40)
            status = os.popen("ps aux | grep -i {}".format(i)).read()
            count = len(status.splitlines())
            if count <= 2:
                os.system("app-{} upgrade".format(i))
                with open(docker_log_file, "a") as f:
                    f.write("\nTIME: "+current_time+"\n")
                    f.write('{} was down and has been RESTARTED(2nd attempt)'.format(i))
                    os.system("clear")
            else:
                pass
            
            time.sleep(40)
            status = os.popen("ps aux | grep -i {}".format(i)).read()
            count = len(status.splitlines())
            if count <= 2:
                with open(docker_log_file, "a") as f:
                    f.write(
                        "\nScript is unable to FIX your {} so please open a support ticket from here - https://my.ultraseedbox.com/submitticket.php\n".format(i))
                    
                    
    def torrent_client_fixing(self, apps):
        for i in apps:
            status = os.popen("ps aux | grep -i {}".format(i)).read()
            count = len(status.splitlines())
            if count <= 2:
                os.system("app-{} restart".format(i))
                with open(rtorrent_log_file, "a") as f:
                    f.write("\nTIME: "+current_time+"\n")
                    f.write('{} was down and has been RESTARTED'.format(i))
                    os.system("clear")
            else:
                pass
            time.sleep(2)
            status = os.popen("ps aux | grep -i {}".format(i)).read()
            count = len(status.splitlines())
            if count <= 2:
                os.system("app-{} repair".format(i))
                with open(rtorrent_log_file, "a") as f:
                    f.write("\nTIME: "+current_time+"\n")
                    f.write('{} was down and has been repair'.format(i))
                    os.system("clear")
            time.sleep(2)
            status = os.popen("ps aux | grep -i {}".format(i)).read()
            count = len(status.splitlines())
            if count <= 2:
                with open(rtorrent_log_file, "a") as f:
                    f.write(
                        "\nScript is unable to FIX your {} so please open a support ticket from here - https://my.ultraseedbox.com/submitticket.php\n".format(i))

monitor = app_monitor()
if __name__ == '__main__':
    # monitor.get_docker_apps(apps_path)
    # monitor.get_torrent_clients(config_path)
    monitor.sql_based_apps(apps_path)