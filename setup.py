#!/usr/bin/python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='dingtalk_notify',
    url='https://github.com/JetBlink/dingtalk_notify_python_sdk',
    author='sh7ning',
    author_email='sh7ning@qq.com',
    version='1.0.0',
    packages=find_packages(),
    license="MIT",
    description="the dingtalk robot, 钉钉报警（带签名）",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
