import os
import socket

from django.apps import AppConfig
from django.core.management.commands.runserver import Command


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('192.168.0.0', 0))
        ip = s.getsockname()[0]
    except:
        ip = None
    finally:
        s.close()
    return ip

def red(string):
    return f'\033[31m{string}\033[0m'

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    def ready(self):
        ip = get_host_ip()
        if ip is None:
            print(red('Failed to get the host ip.'))
        else:
            print(red(
                      f'Make sure that the host device and other devices using this service connect to the same LAN.\n'
                      f'For non-host devices, access "http://{ip}:{Command.default_port}" to download files from the host device or upload files to the host device.\n'
                      f'For downloading a file from the host device, click the "Download" button next to the name of the file you want to download. Before downloading, put the files for downloading in "FileTransmitter/files" of the host device.\n'
                      f'For uploading a file to the host device, click the "Choose File" button to choose a file and click the "Upload" button to upload it to the host device. The uploaded file will be saved in "FileTransmitter/files" of the host device, and it will overwrite the existing file with the same name.'))
        if not os.path.exists('files'):
            os.makedirs('files', exist_ok=True)


