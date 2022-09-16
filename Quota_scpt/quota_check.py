import os
import requests
import re
import configparser

work_dir = os.getcwd()
config_path = work_dir + '/bin'
#base variable
config = configparser.ConfigParser()
config_file = '{}/scripts/quota_check/config.ini'.format(work_dir)

threshold = 90

class Quota_check():
    """
    Get all torrent client installed on service
    """
    
    def get_torrent_clients(self, path):
        torrent_client = []
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
            
        return torrent_client
    
    def get_quota_value(self):
       Quota = os.popen("quota -s 2>/dev/null").read().split() # example 133M
       Used_Quota_Value = re.sub("[^0-9]", "", Quota[17]) # output 133
       Used_Quota_metric = re.sub("[^A-Z]", "", Quota[17]) # M
       Quota_Limit = re.sub("[^0-9]", "", Quota[19]) # quota limit value
       return Used_Quota_metric, Used_Quota_Value, Quota_Limit
    
    def quota_percentage(self,Used_Quota_metric,Used_Quota_Value,Quota_Limit):
        Used_Quota_Value = float(Used_Quota_Value)
        Quota_Limit = float(Quota_Limit)
        if Used_Quota_metric == "G":
            quota_percent = (Used_Quota_Value / Quota_Limit) * 100
        if Used_Quota_metric == "M":
            Used_Quota_Value = Used_Quota_Value * 0.1027
            quota_percent = (Used_Quota_Value/Quota_Limit) * 100
        else:
            pass
        return round(quota_percent,1)
    
    def compare_quota(self,threshold,quota_percent):
        if threshold < quota_percent:
            return True
        else:
            False


    """
    Discord functions are below
    """
    
    def Discord_Notifications_Accepter(self):
        Web_Url = input("Please enter your Discord Web Hook Url Here:")
        return Web_Url
        
    def Discord_notification_(self,webhook,alert):
        if alert:
            data = {"content": '**You are going to hit your disk quota please delete some data or upgrade your service to larger plan** :)'}
            response = requests.post(webhook, json=data)
            
    def stop_torrent_client(self,choice,torrent_client):
        if choice == "yes" or "Yes":
            for i in torrent_client:
                os.system("app-{} stop".format(i))
        else:
            pass
        
    def torrent_stopping_opt(self):
        opt = input("Do you wish to stop torrent client on hitting disk limit ? (yes/no): ")
        return opt
        
    def create_config_file(self, url,opt):
        config.add_section('Webhook')
        config.set('Webhook', 'value', url)
        config.add_section('option')
        config.set('option', 'stop_torrentclient', opt)
        with open(config_file, '+w') as configfile:
            config.write(configfile)
    

checker = Quota_check()
if __name__ == '__main__':
    check = os.path.exists(config_file)
    if check == False:
        url = checker.Discord_Notifications_Accepter()
        opt = checker.stop_torrent_client()
        checker.create_config_file(url,opt)
    else:
        pass
        #Used_Quota_metric, Used_Quota_Value, Quota_Limit = checker.get_quota_value()
        #quota_percent = checker.quota_percentage(Used_Quota_metric, Used_Quota_Value, Quota_Limit)
        #checker.compare_quota(threshold,quota_percent)