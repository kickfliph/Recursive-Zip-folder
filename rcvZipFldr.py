import os
from datetime import datetime, date, timedelta
import time
import shutil
import zipfile 

src_fld = r'the\path'
dy_bfr = datetime.today() - timedelta(days=6) # Up to the day in numbers
dy_bck = datetime.today() - timedelta(days=20) # From day back  in mumbers

def filter_by_date(src_folder, archive_date):

    relevant_folders = []
    for file in os.listdir(src_folder):
        full_name = os.path.join(src_folder, file)
        if os.path.isdir(full_name):
           if datetime.fromtimestamp(os.path.getmtime(full_name)) >= dy_bck and datetime.fromtimestamp(os.path.getmtime(full_name)) <= dy_bfr:
              selected = full_name.replace('\\','*')
              selected = full_name.replace('**','\\')
              relevant_folders.append(selected)
    return relevant_folders

def retrieve_file_paths(dirName):
 
  filePaths = []
   
  for root, directories, files in os.walk(dirName):
    for filename in files:
        filePath = os.path.join(root, filename)
        filePaths.append(filePath)         
  return filePaths
  
def zip_folder(dir_name):
   
  filePaths = retrieve_file_paths(dir_name)
   
  print('The following list of files will be zipped:')
  for fileName in filePaths:
    print(fileName)
     
  zip_file = zipfile.ZipFile(dir_name+'.zip', 'w')
  with zip_file:
    for file in filePaths:
      zip_file.write(file)
  print(dir_name+'.zip file is created successfully!')    

def dlt_folder(dir_name):

   shutil.rmtree (dir_name) 

if __name__ == '__main__':
  relevant_folders = filter_by_date(src_fld, datetime.today())
  for i in relevant_folders:
     print (i)
     zip_folder (i)
     dlt_folder (i)
