import glob
import os
import re
import shutil
import random, string

class MainScript():


    def __init__(self):
        self.download_path = ""
        self.zip = 0
        self.rar = 0
        self.z7 = 0
        self.IMAGE_DIRECTORY_NAME = "images"
        self.MUSIC_DIRECTORY_NAME = "music"
        self.MOVIE_DIRECTORY_NAME = "movie"
        self.EXE_DIRECTORY_NAME = "exe"
        self.DOCUMENT_DIRECTORY_NAME = "document" 
        self.OTHER_DIRECTORY_NAME = "other"
        self.FOLDER_DIRECTORY_NAME = "folder"


    def delete_file(self,toggle,file_kind):
        if toggle == 1 :
            file_list = glob.glob(self.download_path + "/*." + file_kind)
            for file_name  in file_list:
                os.remove(file_name)
        else:
            pass


    def randomname(self,n):
        randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
        return ''.join(randlst)

    def move_files(self,rand_dir, list_name):
        for file_path in list_name:
            if os.path.isdir(file_path) == False:
                shutil.move(file_path,self.download_path + "/" + rand_dir)

    def main(self,download_path,zip,rar,z7):

        self.download_path = download_path
        self.zip = zip
        self.rar = rar
        self.z7 = z7

        self.delete_file(self.zip,'zip')
        self.delete_file(self.rar,'rar')
        self.delete_file(self.z7,'7z')

        directory = [
                self.IMAGE_DIRECTORY_NAME,
                self.MUSIC_DIRECTORY_NAME,
                self.MOVIE_DIRECTORY_NAME,
                self.EXE_DIRECTORY_NAME,
                self.DOCUMENT_DIRECTORY_NAME,
                self.OTHER_DIRECTORY_NAME,
                self.FOLDER_DIRECTORY_NAME
                ]

        rand_name = self.randomname(12)
        rand_dir = []
        for index, dir_name in enumerate(directory):
            rand_dir.append(rand_name + dir_name)
            os.makedirs(download_path + "/" + rand_dir[index])

        image_list = [p for p in glob.glob(download_path + "/*") if re.search('\.(png|gif|jpg|svg|jpeg|ico)$',p)]
        music_list = [p for p in glob.glob(download_path + "/*") if re.search('\.(mp3|m4a|aac|flac)$',p)]
        movie_list = [p for p in glob.glob(download_path + "/*") if re.search('\.(mp4|avi|wmv)$',p)]
        exe_list = [p for p in glob.glob(download_path + "/*") if re.search('\.(exe|msi)$',p)]
        document_list = [p for p in glob.glob(download_path + "/*") if re.search('\.(pdf|txt|xlsx|xls|csv|docx)$',p)]


        self.move_files(rand_dir[0], image_list)
        self.move_files(rand_dir[1], music_list)
        self.move_files(rand_dir[2], movie_list)
        self.move_files(rand_dir[3], exe_list)
        self.move_files(rand_dir[4], document_list)

        other_list = [p for p in glob.glob(download_path + "/*") if re.search('\.',p)]

        self.move_files(rand_dir[5], other_list)

        folder_list = [p for p in glob.glob(download_path + "/*") if re.search('^(?!.*%s).*$' % rand_name ,p)]
        for folder_path in folder_list:
            count = 0
            for dir_name in directory:
                if folder_path.replace("\\","/") == download_path + "/" + dir_name:
                    count = 1
            if count == 0:
                shutil.move(folder_path,download_path + "/" + rand_dir[6])
            else:
                pass

        for index, dir_name in enumerate(rand_dir):
            if os.path.isdir(download_path + "/" + directory[index]):
                pass
            else:
                os.makedirs(download_path + "/" + directory[index])
            for file_path in glob.glob(download_path + "/" + dir_name + "/*"):
                shutil.move(file_path, download_path + "/" + directory[index])
            os.rmdir(download_path + "/" + dir_name)
