import glob
import shutil

for i in glob.glob("D://fjeport//ICPS//CPS//Container_CPS//FuZhou_HaiYing//*"):
    print(i)
    print(i.split('.')[0][-4:])
    if i.split('.')[0][-4:] == '- 副本':
        shutil.move(i, 'D://fjeport//ICPS//CPS//Container_CPS//FuZhou_zh//')
