# Dingtalk Notify Python_sdk
钉钉机器人通知(支持加签). dingtalk robot notification python sdk.

## Installation

```
pip3 install dingtalk_notify
```

## Usage

```
from dingtalk_notify.ding_talk import DingTalkRobot

dt = DingTalkRobot('token', 'sec')
dt.send_text('this is a test message')
```

## Pypi Upload Notice 

* 安装依赖

```
python3 -m pip install --user --upgrade setuptools wheel twine

```

* 校验

```
python3 setup.py check
```

* 打包

```
python3 setup.py sdist bdist_wheel
```

* 上传发布

```
python3 -m twine upload  dist/*
```
