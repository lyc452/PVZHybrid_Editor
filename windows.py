import os
import PyInstaller.__main__

# 设置版本号
version = "0.28"

# 设置当前目录为脚本所在目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 生成打包命令
PyInstaller.__main__.run([
    '--name=PVZHybrid_Editor_b{}'.format(version),
    '--onefile',
    '--noconsole',
    '--icon=res/icon/editor.ico',
    '--add-data=res;res',
    'editor.py'
])