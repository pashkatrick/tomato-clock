#!/usr/bin/env python3
# ====== 🍅 Tomato Clock =======
# ./tomato.py         # start a 30 minutes tomato clock + 10 minutes break in 9 times
# ./tomato.py --work 25 --rest 5 --loop 4      # start a 25 minutes tomato clock + 5 minutes break in 4 times


import sys
import time
import subprocess
import argparse

WORK_MINUTES = 30
BREAK_MINUTES = 10
LOOP_COUNT = 9


parser = argparse.ArgumentParser()


def main():
    try:
        parser.add_argument("-w", "--work", help="work minutes", type=int)        
        parser.add_argument("-r", "--rest", help="break minutes", type=int)
        parser.add_argument("-l", "--loop", help="loop count", type=int)
        args = parser.parse_args()
        if len(sys.argv) <= 1:
            loop(WORK_MINUTES, BREAK_MINUTES, LOOP_COUNT)

        elif len(sys.argv) > 1:
            work = args.work if args.work else WORK_MINUTES
            rest = args.rest if args.rest else BREAK_MINUTES
            loops = args.loop if args.loop else LOOP_COUNT
            loop(work, rest, loops)
        
        else:
            print('Something wrong')
            exit()

    except KeyboardInterrupt:
        print('\n👋 goodbye')
    except Exception as ex:
        print(ex)
        exit(1)

def loop(_work, _break, _loops):
    for i in range(0, _loops-1):
        print(f'🍅 tomato {_work} minutes. Ctrl+C to exit')
        tomato(_work, 'It is time to take a break')
        print(f'🛀 break {_break} minutes. Ctrl+C to exit')
        tomato(_break, 'It is time to work again')

def tomato(minutes, notify_msg):
    start_time = time.perf_counter()
    while True:
        diff_seconds = int(round(time.perf_counter() - start_time))
        left_seconds = minutes * 60 - diff_seconds
        if left_seconds <= 0:
            print('')
            break

        countdown = '{}:{} ⏰'.format(int(left_seconds / 60), int(left_seconds % 60))
        duration = min(minutes, 25)
        progressbar(diff_seconds, minutes * 60, duration, countdown)
        time.sleep(1)

    notify_me(notify_msg)
        


def progressbar(curr, total, duration=10, extra=''):
    frac = curr / total
    filled = round(frac * duration)
    print('\r', '🍅' * filled + '--' * (duration - filled), '[{:.0%}]'.format(frac), extra, end='')


def notify_me(msg):
    '''
    # macos desktop notification
    terminal-notifier -> https://github.com/julienXX/terminal-notifier#download
    terminal-notifier -message <msg>

    # ubuntu desktop notification
    notify-send

    # voice notification
    say -v <lang> <msg>
    lang options:
    - Daniel:       British English
    - Ting-Ting:    Mandarin
    - Sin-ji:       Cantonese
    '''

    print(msg)
    try:
        if sys.platform == 'darwin':
            # macos desktop notification
            subprocess.run(['terminal-notifier', '-message', '🍅 ' + msg])
            subprocess.run(['say', '-v', 'Daniel', msg])
        elif sys.platform.startswith('linux'):
            # ubuntu desktop notification
            subprocess.Popen(["notify-send", '🍅 ' + msg])
        else:
            # windows?
            # TODO: windows notification
            pass

    except:
        # skip the notification error
        pass

if __name__ == "__main__":
    main()
