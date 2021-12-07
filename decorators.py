import time
from collections import OrderedDict
from functools import lru_cache


def fabrik_decorator(arg1):
    print(f"Аргумент фабрики декораторов {arg1}")
    def decorator(fn):
        print(f"Я вызываюсь при декорировании с аргументоv {arg1} из фабрики декораторов")

        def wrapper(*args, **kwargs):
            print("Я вызываюсь в задекорированной функции")
            return fn(*args, **kwargs)
        return wrapper
    return decorator


def decorator(fn):
    print("Я вызываюсь при декорировании")

    def wrapper(*args, **kwargs):
        print("Я вызываюсь в задекорированной функции")
        return fn(*args, **kwargs)
    return wrapper


@decorator
def test():  # test = decorator(test)
    ...


@fabrik_decorator(123)
def test2():  # test = decorator(test)
    ...


def cache(size=3):
    def decorator_cache(fn):
        # cache_dict = {}
        cache_dict = OrderedDict()  # - то же, что обычный словарь (для старых версий Python)


        def wrapper(*args):
            # cache_dict.popitem()
            if args not in cache_dict:
                if len(cache_dict) == size:
                    cache_dict.popitem(last=False)
                result = fn(*args)
                cache_dict[args] = result
            return cache_dict[args]
        return wrapper
    return decorator_cache

# @cache()


@lru_cache(maxsize=3)
def my_sleep():
    time.sleep(3)


if __name__ == '__main__':
    # test2()
    # test2()
    t0 = time.time()

    my_sleep()
    my_sleep()

    print(time.time() - t0)

