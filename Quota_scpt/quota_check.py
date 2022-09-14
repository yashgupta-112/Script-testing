import os
import requests

work_dir = os.getcwd()
config_path = work_dir + '/bin'


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
       QuotaOutPut = os.popen("quota -s 2>/dev/null").read()
       QuotaFormat = os.popen("echo '{}' | awk 'END{print substr($2, length($2))}'".format(QuotaOutPut)).read()
       QuotaUsed = os.popen("echo '{}' | awk 'END{print substr($2, 1, length($2)-1)}'".format(QuotaOutPut)).read()
       print("quotaused",QuotaUsed)
       print(QuotaFormat)
       print(QuotaOutPut)
    
    
    def compare_quota(self,threshold):
        pass
    
    def send_discord_notification(self,WebHookURL):
        pass
    

checker = Quota_check()
if __name__ == '__main__':
    checker.get_quota_value()