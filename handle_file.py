# -*- coding: utf-8 -*-
import os
import shutil


def mkdir_for_each_file(path):
    '''
    功能：为每一个文件创建一个文件夹，并将文件拷贝到对应的文件夹中。
    参数：待创建文件夹的文件所在的路径。
    子目录：不处理。
    '''
    for name in os.listdir(path):
        full_path = os.path.join(path,name)
        
       # print(full_path)
        if os.path.isfile(full_path):
            file_name = os.path.splitext(full_path)[0]
            # (file_name,ext_name) = os.path.splitext(full_path)
            # print(file_name)
            if not os.path.exists(file_name):
                os.mkdir(file_name)
            shutil.move(full_path,file_name+'/')
        

def del_prefix_for_each_file(path):
    '''
    功能：删除每一个文件包含的"1~100"的前缀，如果前缀是01-09的部分无法删除。
    参数：待删除前缀的文件所在的路径。
    子目录：已处理。
    '''
    for name in os.listdir(path):
        full_path = os.path.join(path,name)
        
        if os.path.isdir(full_path):
            del_prefix_for_each_file(full_path)
        # print(full_path)
        new_path_name = full_path

        for i in range(1,101):
            # print(i)
            new_path_name = new_path_name.replace(str(i)+'-','')
            
            
if __name__ == '__main__':
    '''
    使用方法：将 path 替换成想要处理的路径，替换想要执行的函数名，在命令行下执行即可。
    '''
    path = 'E:/a/b'
    mkdir_for_each_file(path)


