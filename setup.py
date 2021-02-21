# coding: utf-8
 
from setuptools import setup, find_packages
 
setup(
    name='zzztestest',  # 项目名称,也就是pip list后会出来的包名
    version='1.0.0',
    packages=find_packages(), # 包含所有的py文件
    include_package_data=True, # 将数据文件也打包
    zip_safe=True
    )

