def write_data():
        inf = open('myfile.txt','w')
        text = "Hello file world!\n"
        inf.write(text)
        inf.close()
write_data()
