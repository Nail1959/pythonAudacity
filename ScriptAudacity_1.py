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
client.write("SetProject: Rate=22050")
only_tracks = False
if only_tracks is False:
    # Импорт аудио файла в Audacity
    # client.write('Import2: Filename="D:\\AudioBooks\\Dolnik_Klukvin\\00_00_Vstuplenie.mp3"',
    #              timer=True)
    # Преобразование стерео в моно
    client.write("Stereo to Mono: ")
    client.write("SelTrackStartToEnd: ")

    client.write("Disjoin: ")
    client.write("CursTrackStart: ")
    b = 'N'
    while True:
        b = input("Продлжить обработку?(Y/N) ")
        if b.lower() == 'y': break


counts_clip = int(input("Количество клипов меток = "))
i = 0
client.write("CursTrackStart: ")
while i < counts_clip:
      client.write("SelNextClip: ")
      # client.write(f"SetClip: At='{i}'")
      # reply = client.read()
      label = f"AddLabel: Label={str(i)}"
      client.write(label)
      reply = client.read()
      rs = reply[-8:]
      if rs == 'Failed!\n':
          print(replay)
          break
      time.sleep(0.1)
      i += 1
#client.write(u"Macro_Разметкаклипов: ")
#client.write('Command=Exit', timer=True)
print(client.read())