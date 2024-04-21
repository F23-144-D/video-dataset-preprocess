import os
import subprocess

from variables import FPS_RATE
from variables import raw_data as dir_path
from variables import n_frames as dst_dir_path

for class_name in os.listdir(dir_path):
    class_path = os.path.join(dir_path, class_name)
    if not os.path.isdir(class_path):
        continue

    dst_class_path = os.path.join(dst_dir_path, class_name)
    if not os.path.exists(dst_class_path):
        os.mkdir(dst_class_path)

    for file_name in os.listdir(class_path):
        if '.avi' not in file_name:
            continue
        name, ext = os.path.splitext(file_name)
    
        dst_directory_path = os.path.join(dst_class_path, name)

        video_file_path = os.path.join(class_path, file_name)
        try:
            if os.path.exists(dst_directory_path):
                if not os.path.exists(os.path.join(dst_directory_path, 'image_00001.jpg')):
                    subprocess.call('rm -r \"{}\"'.format(dst_directory_path), shell=True)
                    print('remove {}'.format(dst_directory_path))
                    os.mkdir(dst_directory_path)
            
                else:
                    continue
            else:
                os.mkdir(dst_directory_path)
        except:
            print(dst_directory_path)
            continue
        cmd = 'ffmpeg -i \"{}\" -vf "fps={},scale=-1:240" \"{}/image_%05d.jpg\"'.format(video_file_path, FPS_RATE, dst_directory_path)
    
        print(cmd)
        subprocess.call(cmd, shell=True)
        print('\n')