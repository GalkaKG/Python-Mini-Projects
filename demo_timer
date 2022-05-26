import time

user_end = int(input())
counter = 0
tic = (time.perf_counter())

while True:
    toc = time.perf_counter()
    if toc - tic > 1:
        counter += 1
        print(counter)
        if counter >= user_end:
            print('Bang!')
            break
        tic = toc
