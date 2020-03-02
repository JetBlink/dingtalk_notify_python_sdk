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
