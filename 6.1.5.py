class CustomException(Exception):
    _file = "logs.txt"
    def __init__(self, *args, file_log_msg='', **kwargs):

        if file_log_msg != '' :
            print("file_log_msg   :  " + file_log_msg)
            f=open(self._file, 'a+')
            print(file_log_msg, file=f)
            f.close()
        elif len(args) != 0:
            print(f" len args   : {len(args)} \n args   :   {args}")
            f=open(self._file, 'a+')
            print(args[0], file=f)
            f.close() 
        elif len(kwargs) != 0:
            f=open(self._file, 'a+')
            print(next(iter(kwargs.values())), file=f)
            f.close()
        
        
        else:
            pass
       
            
     


#if __name__ == "__main__":
#    raise CustomException('hello')     
#p = CustomException()


print("-------------------------p2-------------------------")
p2 = CustomException("hfhjkhg",file_log_msg='22222222222222',fish=["Larry", "Curly", "Moe"], turtle="Shelldon")

print("-------------------------p3-------------------------")
p3 = CustomException('hfhjkhg',fish=["Larry", "Curly", "Moe"], turtle="Shelldon")

print("-------------------------p4-------------------------")
p4 = CustomException(fish=["Larry", "Curly", "Moe"], turtle="Shelldon")

print("-------------------------p5-------------------------")
p5 = CustomException()
