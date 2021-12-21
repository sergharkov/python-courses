import os

SPLIT = "│  "
END_SPLIT = "   "
TOKEN = "├──"
END_TOKEN = "└──"


def tree(path, padding=''):
    if (type(path) is not str):
        raise TypeError(f"path must been String type")
        
    if not os.path.exists(path):
        raise ValueError(f"path {path} not found")

    
    else:   
            print('.')
            for root, dirs, files in os.walk(path):
                level = root.replace(path, '').count(os.sep)
               
                indent = TOKEN + '\t' * 1 * (level)
                output_string = '{}{}'.format(indent, os.path.basename(root))
                print(f'{output_string}' )
                subindent = END_TOKEN +'\t' * 1 * (level + 1)
                print(SPLIT)
                size =0
                print('---------------------------------------')
                print(f'root : {root} \n  dirs : {dirs} \n files : {files}  ')
                print('---------------------------------------')
                 
                
                for f in files:
                    output_string = '{}{}'.format(subindent, f)

                    fp = os.path.join(root, f)
                    size += os.stat(fp).st_size
                    print(f'{output_string} ( {size} bytes)' )

    

if __name__ == "__main__":
    tree('D:\sample\inner1_dir')

