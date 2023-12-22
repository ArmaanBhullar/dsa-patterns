import os
import time
import sys
import requests
POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()
BASE_URL = 'http://flupy.org/data/flags'
MAX_WORKERS = 20
DEST_DIR = './'
def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)

def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return resp.content

def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc

def show(text):
    print(text, end=' ')
    sys.stdout.flush()

def download_many(cc_list):
    for cc in sorted(cc_list):
        image = get_flag(cc)
        show(cc)
        save_flag(image, cc.lower() + '.gif')
    return len(cc_list)

from concurrent import futures
def download_many_threaded(cc_list):
    executor = futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) # define the executor
    with executor: # executor's __exit__ method will call .shutdown(wait = True) which will block till all have returned
        res = executor.map(download_one, sorted(cc_list)) # returns a generator
    return len(list(res))


def download_many_with_processes(cc_list):
    executor = futures.ProcessPoolExecutor() # define the executor
    with executor: # executor's __exit__ method will call .shutdown(wait = True) which will block till all have returned
        res = executor.map(download_one, sorted(cc_list)) # returns a generator
    return len(list(res))

def download_many_basic(cc_list):
    executor = futures.ThreadPoolExecutor(20)
    ls_res = []
    with executor:
        ls_futures = []
        for flag in sorted(cc_list):
            future = executor.submit(download_one, flag)
            print(f'Submitted future = {future}')
            ls_futures.append(future)
        for future in futures.as_completed(ls_futures): # as the futures are completed, do something with the result
            res = future.result
            print(f"Done for result = {res}")
            ls_res.append(res)
    return len(ls_res)

def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))

if __name__ == '__main__':
    # main(download_many_threaded) # For multithreaded version simpl
    # main(download_many_basic) # for multithreaded version broken down
    # main(download_many_with_processes)
    main(download_many_threaded)
