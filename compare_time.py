#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# --------------------------------------------
# make a time comparison
# --------------------------------------------

# specify experiment - number of iterations 
niter = 50

# use function name check to avoid infinite cycles/incorrect time measurement 
if __name__ == '__main__':
    import time
    
# run experiment with multiprocessing and measure time
    start_time_multi = time.perf_counter()
    exec(open('experiment_script_multiprocessing.py').read())
    finish_time_multi = time.perf_counter()
    
    run_time_multi = finish_time_multi - start_time_multi
    print(f'Execution time of the script running in parallel is {round(run_time_multi,2)}, amount of iterations is {niter}')
    
# run original experiment (without multiprocessing) and measure time
    start_time_orig = time.perf_counter()
    exec(open('experiment_script_original.py').read())
    finish_time_multi = time.perf_counter()
    
    run_time_orig = finish_time_multi - start_time_multi
    print(f'Execution time of the script running in parallel is {round(run_time_orig,2)}, amount of iterations is {niter}')
    
    print(f'\nRunning in parallel takes {round(run_time_orig/run_time_multi, 2)} times less time ')
