# 🍅 Tomato Timer
[![PyPI version](https://badge.fury.io/py/tomato-timer.svg)](https://badge.fury.io/py/tomato-timer)

Tomato Timer is a simple command line pomodoro app.

## Installation

Install python from https://www.python.org/

- Install via pip:
```
$ pip install tomato-timer
```

- Install via source code:
```
$ git clone https://github.com/pashkatrick/tomato-timer.git
$ cd tomato-timer
$ chmod +x tomato.py 
```

## How to use

- if you install via pip

```
$ tomato                              # start a 20 minutes tomato clock + 10 minutes break in 9 times
$ tomato --work 25 --rest 5 --loop 4  # start a 25 minutes tomato clock + 5 minutes break in 4 times
$ tomato -h                           # help

```

- if you install via source code
```
$ ./tomato.py                              # start a 30 minutes tomato clock + 10 minutes break in 9 times
$ ./tomato.py --work 25 --rest 5 --loop 4  # start a 25 minutes tomato clock + 5 minutes break in 4 times
$ ./tomato.py -h                           # help
```

## Terminal Output
```
🍅 tomato 25 minutes. Ctrl+C to exit
 🍅🍅---------------------------------------------- [8%] 23:4 ⏰ 
```

## Desktop Notification

- MacOS

```
$ brew install terminal-notifier 
```

`terminal-notifier` actually is a cross-platform desktop notifier, please refer to ➜ [terminal-notifier](https://github.com/julienXX/terminal-notifier#download)

<img src="https://github.com/coolcode/tomato-clock/blob/master/img/screenshot-macos.png?raw=true" alt="terminal-notifier" width="300"/>

- Ubuntu

`notify-send`

<img src="https://github.com/coolcode/tomato-clock/blob/master/img/screenshot-ubuntu.png?raw=true" alt="ubuntu-notification" width="300"/>



## Voice Notification
We use `say`(text-to-speech) for voice notification 

- MacOS

MacOS already has `say`. see [here](https://ss64.com/osx/say.html) or [more detail](https://gist.github.com/mculp/4b95752e25c456d425c6)  

- Ubuntu

see this link: [say](http://manpages.ubuntu.com/manpages/trusty/man1/say.1.html)
```
sudo apt-get install gnustep-gui-runtime
```
