import os
import requests
import re
work_dir = os.getcwd()
config_path = work_dir + '/bin'

Discord_WebHook_File = '{}/scripts/quota_check/discord.txt'.format(work_dir)

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
        print(quota_percent)
    
    def compare_quota(self,threshold):
        pass


    """
    Discord functions are below
    """
    
    def Discord_Notifications_Accepter(self):
        Web_Url = input("Please enter your Discord Web Hook Url Here:")
        with open(Discord_WebHook_File, '+w') as f:
            f.write(Web_Url)
        f.close()
    
        
    def Discord_WebHook_Reader(self):
        with open(Discord_WebHook_File, 'r') as f:
            return f.read()
        
    def Discord_notification_(self,webhook):
        data = {"content": '**You are going to hit your disk quota please delete some data or upgrade your service to larger plan** :)'}
        response = requests.post(webhook, json=data)
    

checker = Quota_check()
if __name__ == '__main__':
    Used_Quota_metric, Used_Quota_Value, Quota_Limit = checker.get_quota_value()
    print(Used_Quota_metric, Used_Quota_Value, Quota_Limit)
    checker.quota_percentage(Used_Quota_metric, Used_Quota_Value, Quota_Limit)