# FileTransmitter
This is a tool for transmitting files over a LAN.

## version
v1.0.0

## Environmental Requirements
Python >= 3.10.6, Django >= 5.0.1

## How to use
Make sure that the host device and other devices using this service connect to the same LAN.<br>
Execute "python manage.py runserver 0.0.0.0:8000 --noreload" or execute "run.bat" (in Windows) on the host device to start the service.<br>
For non-host devices, access "http://{hsot ip}:{port}" to download files from the host device or upload files to the host device. The host ip can be obtained via "ipconfig", and the default port is 8000.<br>
For downloading a file from the host device, click the "Download" button next to the name of the file you want to download. Before downloading, put the files for downloading in "FileTransmitter/files" of the host device.<br>
For uploading a file to the host device, click the "Choose File" button to choose a file and click the "Upload" button to upload it to the host device. The uploaded file will be saved in "FileTransmitter/files" of the host device, and it will overwrite the existing file with the same name.<br>

## Author
[FSPolarBear](https://github.com/FSPolarBear)