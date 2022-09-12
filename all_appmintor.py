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
arr_apps=[]



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

"""
Class app_monitor is decalared below with all its functions

"""


class app_monitor():
    """
    These below given function will get all apps intalled on service
    """

    def get_docker_apps(self, path):
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

    def sql_based_apps(self, path):
        remove_apps = ['backup', 'nginx']
        all_apps = os.listdir(path)
        installed_apps = list(set(all_apps).difference(remove_apps))
        for i in sql_apps:
            if i in installed_apps:
                mysql_apps.append(i)

    def get_torrent_clients(self, path):
        remove_config = ['systemd']
        all_configs = os.listdir(path)
        all_torrent_clients = list(set(all_configs).difference(remove_config))
        if "rtorrent" in all_torrent_clients:
            torrent_client.append('rtorrent')
        if "deluge" in all_torrent_clients:
            torrent_client.append('deluge')
        if "qbittorrent-nox" in all_torrent_clients:
            torrent_client.append('qbittorrent')
        if "transmission-daemon" in all_torrent_clients:
            torrent_client.append('transmission')
            
    def get_arr_apps(self,path):
        remove_apps = ['backup', 'nginx']
        all_apps = os.listdir(path)
        installed_apps = list(set(all_apps).difference(remove_apps))
        for i in arr_apps_list:
            if i in installed_apps:
                arr_apps.append(i)
                
                
                

    """
    Below given function will monitor the apps
    """

    def Monitor_Webserver(self):
        status = os.popen("ps aux | grep -i nginx")
        count = len(status.readlines())
        if count <= 2:
            os.system("app-nginx restart")

    def dockerized_app(self, apps):
        for i in apps:
            status = os.popen("ps aux | grep -i {}| grep -v grep".format(i)).read()
            count = len(status.splitlines())
            if count <= 1:
                os.system("app-{} upgrade".format(i))
                print("{} app upgrade".format(i))
                with open(log_file, "a") as f:
                    f.write("\nTIME: "+current_time+"\n")
                    f.write('{} was down and has been RESTARTED'.format(i)+"\n")
                    os.system("clear")
            
                time.sleep(180)
                status = os.popen("ps aux | grep -i {} | grep -v grep".format(i)).read()
                count = len(status.splitlines())
                if count <= 1:
                    os.system("app-{} upgrade".format(i))
                    with open(log_file, "a") as f:
                        f.write("\nTIME: "+current_time+"\n")
                        f.write(
                        '{} was down and has been RESTARTED(2nd attempt)'.format(i)+"\n")
                    os.system("clear")
                    
                time.sleep(50)
                status = os.popen("ps aux | grep -i {} | grep -v grep".format(i)).read()
                count = len(status.splitlines())
                if count <= 1:
                    with open(log_file, "a") as f:
                        f.write(
                        "\nScript is unable to FIX your {} so please open a support ticket from here - https://my.ultraseedbox.com/submitticket.php\n".format(i))
            else:
                pass

            

    def torrent_client_fixing(self, apps):
        for i in apps:
            status = os.popen("ps aux | grep -i {}".format(i)).read()
            count = len(status.splitlines())
            if count <= 2:
                os.system("app-{} restart".format(i))
                with open(log_file, "a") as f:
                    f.write("\nTIME: "+current_time+"\n")
                    f.write('{} was down and has been RESTARTED'.format(i) +"\n")
                    os.system("clear")
            else:
                pass
            time.sleep(2)
            status = os.popen("ps aux | grep -i {}".format(i)).read()
            count = len(status.splitlines())
            if count <= 2:
                os.system("app-{} repair".format(i))
                with open(log_file, "a") as f:
                    f.write("\nTIME: "+current_time+"\n")
                    f.write('{} was down and has been repair'.format(i) + "\n")
                    os.system("clear")
            time.sleep(2)
            status = os.popen("ps aux | grep -i {}".format(i)).read()
            count = len(status.splitlines())
            if count <= 2:
                with open(log_file, "a") as f:
                    f.write(
                        "\nScript is unable to FIX your {} so please open a support ticket from here - https://my.ultraseedbox.com/submitticket.php\n".format(i))

    def sql_app_monitor(self, apps):
        for i in apps:
            status = os.popen("ps aux | grep -i {}".format(i)).read()
            count = len(status.splitlines())
            if count <= 2:
                os.system("app-{} restart".format(i))
                with open(log_file, "a") as f:
                    f.write("\nTIME: "+current_time+"\n")
                    f.write('{} was down and has been RESTARTED'.format(i)+ "\n")
                    os.system("clear")
            
                time.sleep(120)
                status = os.popen("ps aux | grep -i {} ".format(i)).read()
                count = len(status.splitlines())
                if count <= 2:
                    with open(log_file, "a") as f:
                        f.write(
                        "\nScript is unable to FIX your {} so please open a support ticket from here - https://my.ultraseedbox.com/submitticket.php\n".format(i))

            else:
                pass
            
    def monitor_arr_apps(self):
        all_systemd_files = os.listdir(systemd_path)
        for i in arr_apps:
            if "{}.service".format(i) in all_systemd_files:
                    status = os.popen("ps aux | grep -i {}| grep -v grep".format(i)).read()
                    count = len(status.splitlines())
                    if count <= 1:
                        os.system("app-{} upgrade".format(i))
                        print("{} app upgrade".format(i))
                        with open(log_file, "a") as f:
                            f.write("\nTIME: "+current_time+"\n")
                            f.write('{} was down and has been RESTARTED'.format(i)+"\n")
                        os.system("clear")
            
                        time.sleep(180)
                        status = os.popen("ps aux | grep -i {} | grep -v grep".format(i)).read()
                        count = len(status.splitlines())
                        if count <= 1:
                            os.system("app-{} upgrade".format(i))
                            with open(log_file, "a") as f:
                                f.write("\nTIME: "+current_time+"\n")
                                f.write(
                        '{} was down and has been RESTARTED(2nd attempt)'.format(i)+"\n")
                        os.system("clear")
                    
                        time.sleep(50)
                        status = os.popen("ps aux | grep -i {} | grep -v grep".format(i)).read()
                        count = len(status.splitlines())
                        if count <= 1:
                            with open(log_file, "a") as f:
                                f.write(
                                "\nScript is unable to FIX your {} so please open a support ticket from here - https://my.ultraseedbox.com/submitticket.php\n".format(i))
                    else:
                        pass
            else:
                status = os.popen("ps aux | grep -i {}| grep -v grep".format(i)).read()
                count = len(status.splitlines())
                if count <= 0:
                    os.system("app-{} upgrade".format(i))
                    print("{} app upgrade".format(i))
                    with open(log_file, "a") as f:
                        f.write("\nTIME: "+current_time+"\n")
                        f.write('{} was down and has been RESTARTED'.format(i)+"\n")
                    os.system("clear")
        
                    time.sleep(180)
                    status = os.popen("ps aux | grep -i {} | grep -v grep".format(i)).read()
                    count = len(status.splitlines())
                    if count <= 0:
                        os.system("app-{} upgrade".format(i))
                        with open(log_file, "a") as f:
                            f.write("\nTIME: "+current_time+"\n")
                            f.write(
                    '{} was down and has been RESTARTED(2nd attempt)'.format(i)+"\n")
                    os.system("clear")
                
                    time.sleep(50)
                    status = os.popen("ps aux | grep -i {} | grep -v grep".format(i)).read()
                    count = len(status.splitlines())
                    if count <= 1:
                        with open(log_file, "a") as f:
                            f.write(
                            "\nScript is unable to FIX your {} so please open a support ticket from here - https://my.ultraseedbox.com/submitticket.php\n".format(i))
                else:
                    pass
                
    def bazarr_monitor(self):
        if "bazarr" in arr_apps:
            all_systemd_files = os.listdir(systemd_path)
            if "bazarr.service" in all_systemd_files:
                status = os.popen("ps aux | grep -i bazarr| grep -v grep").read()
                count = len(status.splitlines())
                if count <= 2:
                    os.system("app-bazarr upgrade")
                    with open(log_file, "a") as f:
                        f.write("\nTIME: "+current_time+"\n")
                        f.write('bazarr was down and has been RESTARTED'+"\n")
                    os.system("clear")
        
                    time.sleep(180)
                    status = os.popen("ps aux | grep -i bazarr | grep -v grep").read()
                    count = len(status.splitlines())
                    if count <= 2:
                        os.system("app-bazarr upgrade")
                        with open(log_file, "a") as f:
                            f.write("\nTIME: "+current_time+"\n")
                            f.write(
                    'bazarr was down and has been RESTARTED(2nd attempt)'+"\n")
                    os.system("clear")
                
                    time.sleep(50)
                    status = os.popen("ps aux | grep -i bazarr | grep -v grep").read()
                    count = len(status.splitlines())
                    if count <= 1:
                        with open(log_file, "a") as f:
                            f.write(
                            "\nScript is unable to FIX your bazarr so please open a support ticket from here - https://my.ultraseedbox.com/submitticket.php\n")
                else:
                    pass
            else:
                status = os.popen("ps aux | grep -i bazarr| grep -v grep").read()
                count = len(status.splitlines())
                if count <= 0:
                    os.system("app-bazarr upgrade")
                    with open(log_file, "a") as f:
                        f.write("\nTIME: "+current_time+"\n")
                        f.write('bazarr was down and has been RESTARTED'+"\n")
                    os.system("clear")
        
                    time.sleep(180)
                    status = os.popen("ps aux | grep -i bazarr | grep -v grep").read()
                    count = len(status.splitlines())
                    if count <= 0:
                        os.system("app-bazarr upgrade")
                        with open(log_file, "a") as f:
                            f.write("\nTIME: "+current_time+"\n")
                            f.write(
                    'bazarr was down and has been RESTARTED(2nd attempt)'+"\n")
                    os.system("clear")
                
                    time.sleep(50)
                    status = os.popen("ps aux | grep -i bazarr | grep -v grep").read()
                    count = len(status.splitlines())
                    if count <= 0:
                        with open(log_file, "a") as f:
                            f.write(
                            "\nScript is unable to FIX your bazarr so please open a support ticket from here - https://my.ultraseedbox.com/submitticket.php\n")
                else:
                    pass
        else:
            pass
    
    
    def monitor_syncthing(self,apps):
        if "syncthing" in apps:
            status = os.popen("ps aux | grep -i syncthing | grep -v grep").read()
            count = len(status.splitlines())
            if count <= 0:
                os.system("app-syncthing upgrade")
                with open(log_file, "a") as f:
                    f.write("\nTIME: "+current_time+"\n")
                    f.write('syncthing was down and has been RESTARTED'+"\n")
                os.system("clear")

                time.sleep(180)
                status = os.popen("ps aux | grep -i syncthing | grep -v grep").read()
                count = len(status.splitlines())
                if count <= 0:
                    os.system("app-syncthing upgrade")
                    with open(log_file, "a") as f:
                        f.write("\nTIME: "+current_time+"\n")
                        f.write(
                'syncthing was down and has been RESTARTED(2nd attempt)'+"\n")
                os.system("clear")
            
                time.sleep(50)
                status = os.popen("ps aux | grep -i syncthing | grep -v grep").read()
                count = len(status.splitlines())
                if count <= 1:
                    with open(log_file, "a") as f:
                        f.write(
                        "\nScript is unable to FIX your syncthing so please open a support ticket from here - https://my.ultraseedbox.com/submitticket.php\n")
            else:
                pass        
        else:
            pass
    
monitor = app_monitor()
if __name__ == '__main__':
    # monitor.Monitor_Webserver()
    apps = monitor.get_docker_apps(apps_path)
    monitor.get_arr_apps(apps_path)
    print("apps:",apps)
    print("arrs:",arr_apps)
    # print(apps)
    monitor.get_torrent_clients(config_path)
    monitor.sql_based_apps(apps_path)
    print("mysql",mysql_apps)
    # print(torrent_client)
    monitor.monitor_arr_apps()
    # monitor.dockerized_app(apps)
    # monitor.torrent_client_fixing(torrent_client)
    # monitor.sql_app_monitor(mysql_apps)
