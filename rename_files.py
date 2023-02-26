import os

path_source = r'C:\MyCorpus\wav\KlukvinA'
path_target = r'C:\MyCorpus\wav_new\KlukvinA'

flst = os.listdir(path_source)
flst.sort()
cnt = 0
for fn in flst:
    fn_slice = fn[:-4]
    new_fn = ''
    for i in range(len(fn_slice)):
        if not fn_slice[i].isdigit():
           continue
        new_fn +=fn_slice[i]
    new_fn += '.wav'
    new_fn = os.path.join(path_target, new_fn)
    os.rename(os.path.join(path_source, fn), new_fn)
    cnt += 1
print(f'Переименовно файлов = {cnt}')