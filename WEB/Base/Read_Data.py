import yaml,os

#读取yml类型文件
def read_yaml(filename):
    file_path = os.getcwd() + os.sep + 'Data' + os.sep + filename + '.yml'
    with open(file_path,'r')as f:
        return yaml.load(f)
