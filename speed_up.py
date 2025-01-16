import multiprocessing
from functools import partial

def speedup(function, text, dict):
    num_cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_cores)
    applied_function = partial(function, dict)
    process_text = pool.map(applied_function, text.split())
    pool.close()
    pool.join()
    return "".join(process_text)
