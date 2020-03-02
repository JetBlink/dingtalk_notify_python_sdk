# dingtalk_notify_python_sdk
钉钉机器人通知(支持加签). dingtalk robot notification python sdk.

## Installation

```
pip3 install ding_talk_robot
```

## Usage

```
from dingtalk.ding_talk import DingTalkRobot

dt = DingTalkRobot('token', 'sec')
dt.send_text('this is a test message')
```

## pypi upload Notice 

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
