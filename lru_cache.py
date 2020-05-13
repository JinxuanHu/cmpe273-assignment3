import collections
import datetime
class lru_cache:
    def __init__(self, size):
        self.size = size
        self.dict = collections.OrderedDict()

    def get(self, key):
        value = self.dict.get(key) 
        self.dict.move_to_end(key)  
        return value

    def add_or_update(self, key, value):
        if key in self.dict:  # update
            self.dict[key] = value
            self.dict.move_to_end(key)
        else:  # insert
            self.dict[key] = value
            if len(self.dict) > self.size:  # full
                self.dict.popitem(last=False)

    def __call__(self, func):
        def decorator(n):
            name = func.__name__
            if n in self.dict:
                value = self.get(n)
                print('[cache-hit] {}({}) -> {}'.format(name,n ,value))
                return value
            else:
                starttime = datetime.datetime.now()
                value = func(n)
                endtime = datetime.datetime.now()
                time = endtime - starttime
                self.add_or_update(n, value)
                print('[{} ]{}({}) -> {}'.format(time,name, n, value))
                return value
        return decorator


# @LRUCache(3)
# def f(n):
#     if n <= 1:  # 0 or 1
#         return n
#     return f(n - 1) + f(n - 2)


# def test():
#     import time
#     beg = time.time()
#     for i in range(6):
#         print(f(i))
#     print(time.time() - beg)
#     beg = time.time()
#     for i in range(6):
#         print(f(i))
#     print(time.time() - beg)


# if __name__ == '__main__':
#     f(6)