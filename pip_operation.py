import sys, subprocess
from typing import IO


def pip_install(library: str, source_use: bool = False, source='https://pypi.tuna.tsinghua.edu.cn/simple',
                stdout_use: bool = False, stdout: IO = sys.stdout):
    if source_use:
        commod = f'pip install {library} -i {source}'
    else:
        commod = f'pip install {library}'
    if stdout_use:
        subprocess.run(commod, stdout=stdout)
    else:
        subprocess.run(commod)


def pip_list():
    # 运行 pip freeze 命令并获取输出
    output = subprocess.check_output(['pip', 'freeze']).decode('utf-8')
    a = []
    # 按行分割输出并提取库的名称部分
    lines = output.strip().split('\n')
    # 解析每行，提取库的名称
    for line in lines:
        # 使用等号分割字符串
        parts = line.split('==')
        # 如果分割后的结果有多个部分，则取第一个部分作为库的名称
        if len(parts) > 1:
            library_name = parts[0].strip()
        else:
            # 如果分割后的结果只有一个部分，则使用@符号分割字符串，并取第一个部分作为库的名称
            library_name = line.split('@')[0].strip()
        a.append(library_name)
    return a
