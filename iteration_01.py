#! /bin/env python
#-*- coding: utf-8 -*-
# __author__ = "linyu"
# date : 2018/09/02

"""
    简单的迭代器
    python中想要成为一个迭代器的对象必须都支持__iter__和next函数
    __iter__返回整个类对象作为一个迭代器对象
    next返回迭代器里的下一个值。
    next()函数访问迭代器中的连续元素。
    iter()函数用来在循环体中循序访问元素，在内部实现中使用了next函数
    
"""

class SimpleCount(object):
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        'returns itself as an iterator object'
        return self

    def next(self):
        'retruns the next value till current is lower than end'
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


if __name__ == '__main__':
    c = SimpleCount(1, 3)
    print c.next()
    print c.next()
    print c.next()
    #序列到尾部再调用c.nexr()会触发一个StopIteration异常
    #iter()函数会处理这个异常，当数据访问完成的时候退出循环
    #print c.next()

    #一个迭代器对象只能被使用一次
    c = SimpleCount(1, 3)
    for entry in iter(c):
        print entry

    #在python中一个文件对象就是一个迭代器，它支持iter()和next()函数，
    #因此，每次只处理一行数据，而不是将文件加载到内存中。
    #python提供了多种多样的迭代器使用方法的信息，无限迭代器itertools中
    #count()、cycle()以及repeat()等。
        




        
