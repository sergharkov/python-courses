def create_file(file_name):
	file = open(file_name,'w+')
	file.write("Hello file world!\n")
	file.close()
create_file("/myfile.txt")

def read_file(file_name):
	file = open(file_name,'r')
	data_file = file.readline()
	file.close()
	return data_file


print(read_file("/myfile.txt"))

