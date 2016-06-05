import os

def decode_message():
    #list all files
    os.chdir(r"D:\Pavlo\My Files\YaDisk\YandexDisk\courses\Udacity\Python1\alphabet\message")
    files  = os.listdir("./")
    #print(files)
    #rename files
    num = 1
    for file_name in files:
        os.rename(file_name, "julia" + str(num) + ".jpg")
        num += 1 
        #print file_name.translate(None, "0123456789")
    #print(files)    
decode_message()
