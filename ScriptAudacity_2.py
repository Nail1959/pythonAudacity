import os

import pipeclient
import sys
import time

if sys.version_info[0] < 3 and sys.version_info[1] < 7:
    sys.exit('PipeClient Error: Python 2.7 or later required')

# Platform specific constants
if sys.platform == 'win32':
    WRITE_NAME = '\\\\.\\pipe\\ToSrvPipe'
    READ_NAME = '\\\\.\\pipe\\FromSrvPipe'
    EOL = '\r\n\0'
else:
    # Linux or Mac
    PIPE_BASE = '/tmp/audacity_script_pipe.'
    WRITE_NAME = PIPE_BASE + 'to.' + str(os.getuid())
    READ_NAME = PIPE_BASE + 'from.' + str(os.getuid())
    EOL = '\n'

# Соединие с Audacity
client = pipeclient.PipeClient()

# Импорт аудио файла в Audacity
path_clips = r'C:\MyCorpus\wav_new\KlukvinA'
path_out = r'C:\MyCorpus\wav_new\KlukvinA'
flst = os.listdir(path_clips)
flst.sort()
os.chdir(path_clips)

for fn in flst:
    fin = os.path.join(path_clips, fn)
    str = "Import2: Filename=" + fin
    client.write(str)
    result = client.read()
    client.write("SetProject: Rate=22050")
    fout = os.path.join(path_out, fn)
    str = "Export2: Filename=" + fout
    client.write(str)
    result = client.read()
    client.write("RemoveTracks: ")

print(f'Все аудио файлы с частотой 22050')
