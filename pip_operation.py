import sys, subprocess, time
from typing import IO


def pip_install(bag: str, source_use: bool = False, source='https://pypi.tuna.tsinghua.edu.cn/simple',
                stdout_use: bool = False, stdout: IO = sys.stdout):
    if source_use:
        commod = f'pip install {bag} -i {source}'
    else:
        commod = f'pip install {bag}'
    if stdout_use:
        subprocess.run(commod, stdout=stdout)
    else:
        subprocess.run(commod)


def pip_list():
    # 运行 pip freeze 命令并获取输出
    output = subprocess.check_output(['pip', 'freeze']).decode('utf-8')
    a=[]
    # 按行分割输出并提取库的名称部分
    installed_libraries = output.strip().split('\n')
    for library in installed_libraries:
        library_name = library.split('=')[0].strip()
        a.append(library_name)
    return a


pip_list()
pip_install('ap')
