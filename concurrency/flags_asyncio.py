import asyncio
import aiohttp
import types
import tqdm
from concurrency_futures import BASE_URL, save_flag, show, main

async def get_flag(cc):
    url = f'{BASE_URL}/{cc}/{cc}.gif'
    # print(url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            image = await response.read()

    return image

async def download_one(cc, semaphore):
    async with semaphore: # await is a replacement of yield from
        image = await get_flag(cc)
        show(cc)
        # run in executor pool
        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, save_flag, image, cc.lower()+'.gif')
    return cc




def download_many_async(cc_list):

    result = download_coro(cc_list)
    loop = asyncio.get_event_loop()
    # wait_coro = asyncio.wait(to_do) # wait is not a blocking function, it's a coroutine that completes when all coroutines passed to it are complete
    res = loop.run_until_complete(result) # this is the blocking part
    loop.close()
    return len(res)

async def download_coro(cc_list):
    semaphore = asyncio.Semaphore(5)
    ls = []
    to_do = [download_one(cc, semaphore) for cc in cc_list]
    to_do_iter = asyncio.as_completed(to_do)
    for future in to_do_iter:
        # drive to completion here
        res = await future
        ls.append(res)
    return ls

if __name__ == '__main__':
    main(download_many_async)