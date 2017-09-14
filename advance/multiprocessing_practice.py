import multiprocessing
from multiprocessing import Pool

# multiprocessing without returning any data
def spawn(num,num2):
    print('Spawned! {} {}'.format(num,num2))

if __name__ == '__main__':
    for i in range(100):
        p = multiprocessing.Process(target=spawn, args=(i,i+1))
        p.start()
        p.join()

# multiprocessing returnin data
def job(num):
    return num*2

if __name__ == '__main__':
    p = Pool(processes=20)
    data = p.map(job, range(200))
    data2 = p.map(job, [5,2])
    p.close()
    print(type(data))
    print(type(data2))
