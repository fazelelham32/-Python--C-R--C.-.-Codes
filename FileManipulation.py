import os
class File_Manipulator:
    def __init__(self):
	    pass
    def read(self,file_address,type):
	    if type=='line':
		    lines=[]
		    while True:
			    file = open(file_address, 'r',encoding='utf8')
			    line=file.readline()
			    file.close()
			    lines.append(line)
			    if not line:
				    break
	    elif type=='total':
		    file= open(file_address, 'r')
		    lines=file.readlines()
		    file.close()
	    else:
		    print('choose corect type of reading mode')
		    content=''.join(lines)
	    return content
    def write(self,file_address,content,mode='a+'):
	    file= open(file_address, mode, encoding='utf8')
	    file.write(content)
	    file.close()
    def copy(self,add1,add2):
	    content=self.read(add1,'total')
	    self.write(add2,content,'a+')
    def new_folder(self,folder_address):
	    os.makedirs(folder_address)
    def remove(self,add_list):
	    for item in add_list:
		    if os.path.isfile(item):
			    os.remove(item)
		    elif os.path.isdir(item):
			    shutil.rmtree(item)
    def existence(self,file_address):
        if os.path.exists(file_address):
            print('I find it')
        else:
            print('where is it?')
obj = File_Manipulator()
obj.new_folder('your_folder')


