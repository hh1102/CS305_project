import ctypes
import inspect
import math
import os
import sys
import threading
import time
from urllib import request
from flask import Flask, Response, Request
import requests

app = Flask(__name__)
rates = []


@app.route('/')
def get_page():
    url = 'http://127.0.0.1:8080'
    print(url)
    return Response(requests.get(url))


@app.route('/<part>')
def forward(part):
    return Response(requests.get('http://127.0.0.1:8080/%s' % part))


throughput = None
count = 1


@app.route('/vod/<string:part>')
def video(part):
    if part == 'big_buck_bunny.f4m':
        f4m = Response(requests.get('http://127.0.0.1:8080/vod/big_buck_bunny.f4m'))
        no_list = Response(requests.get('http://127.0.0.1:8080/vod/big_buck_bunny_nolist.f4m'))
        lines = f4m.data.splitlines()
        x = len(lines)
        for i in range(1, x):
            line = lines[i].decode()
            if line.startswith('\t\t bitrate='):
                ratesx = line.split('"')
                rates.append(int(ratesx[1]))
        return no_list
    else:
        global count
        begin = time.time()
        begin_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        chars1 = part.split('Seg')  # chars[0] represent rate
        chars2 = chars1[1].split('-Frag')  # chars2[0] represent segment number
        # chars[1] represent frag number
        global throughput
        if count == 1:
            global flag
            flag = True
            content = Response(requests.get('http://127.0.0.1:8080/vod/100Seg1-Frag1'))
            size = sys.getsizeof(content.data)
            end = time.time()
            throughput = size * 8 / ((end - begin) * 1024)
            logging(begin_time, end - begin, throughput, throughput, 10, 8080, 'Seg1-Frag1')
            # print(throughput)
        else:
            my_rate = 10
            for i in range(1, len(rates) - 1):
                if 1.5 * rates[i - 1] <= throughput < 1.5 * rates[i]:
                    my_rate = rates[i - 1]
                    break
            if throughput >= 1.5 * rates[len(rates) - 1]:
                my_rate = rates[len(rates) - 1]
            print(my_rate)
            print(throughput)
            content = Response(
                requests.get('http://127.0.0.1:8080/vod/%d%s%s%s%s' % (my_rate, 'Seg', chars2[0], '-Frag', chars2[1])))
            alpha = 0.3
            t = calculate_throughput(sys.getsizeof(content.data), begin, time.time(), alpha)
            logging(begin_time, time.time() - begin, t, throughput, my_rate, 8080,
                    'Seg%s-Frag%s' % (chars2[0], chars2[1]))
        count += 1
        return content


def logging(begin, spend, throughput, avgtput, bitrate, port, chunkname):
    # begin_time=time.strftime('%Y-%m-%d %H:%M:%S',begin)
    log_file.write('%s\t%.4f\t%.2f\t%.2f\t%s\t%s\t%s\n' % (begin, spend, throughput, avgtput, bitrate, port, chunkname))


def modify_request(message):
    """
    Here you should change the requested bit rate according to your computation of throughput.
    And if the request is for big_buck_bunny.f4m, you should instead request big_buck_bunny_nolist.f4m 
    for client and leave big_buck_bunny.f4m for the use in proxy.
    """


def request_dns():
    """
    Request dns server here.
    """


def calculate_throughput(size, begin, end, alpha):
    """
    Calculate throughput here.
    """
    global throughput
    t = size * 8 / ((end - begin) * 1024)
    throughput = alpha * t + (1 - alpha) * throughput
    return t


log_file = open('log_file.txt', 'a')
flag = False


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""

    tid = ctypes.c_long(tid)

    if not inspect.isclass(exctype):
        exctype = type(exctype)

    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))

    if res == 0:

        raise ValueError("invalid thread id")

    elif res != 1:

        # """if it returns a number greater than one, you're in trouble,

        # and you should call it again with exc=NULL to revert the effect"""

        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)

        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


class clock(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global count
        while True:
            last = count
            time.sleep(2)
            now = count
            if (now == last and flag):
                stop_thread(thread_main)
                sys.exit(0)


class main_thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        app.run(port=21102)


# def stop_thread(thread):
#     _async_raise(thread.ident, SystemExit)
Time = clock()
thread_main = main_thread()

if __name__ == '__main__':
    Time.start()
    thread_main.start()

    # app.run(port=21102)
