#!/usr/local/bin/python2.7
# -*- coding:utf-8; mode:python-mode -*-
# Last Change:2009/08/03 00:43:36.

class MargeSort(object):
    """ マージソートするクラス """
    def __init__(self, cmp=None):
        self.cmp = cmp  # まだ使ってない
                        # データ側で比較演算子を定義してくれてれば必要無し。

    def sort(self, array):
        if len( array ) == 1:
            return

        left_size = len( array ) / 2
        right_size = len( array ) - left_size

        left_array = array[:left_size]
        right_array = array[left_size:]

        self.sort(left_array)
        self.sort(right_array)

        left_pos = 0
        right_pos = 0

        while left_pos < left_size or right_pos < right_size:

            if right_size <= right_pos:
                array[ left_pos + right_pos ] = left_array[ left_pos ]
                left_pos += 1

            elif left_size <= left_pos:
                array[ left_pos + right_pos ] = right_array[ right_pos ]
                right_pos += 1

            elif right_array[ right_pos ] < left_array[ left_pos ]:
                array[ left_pos + right_pos ] = right_array[ right_pos ]
                right_pos += 1

#            elif left_array[ left_pos ] <= right_array[ right_pos ]:
            else:
                array[ left_pos + right_pos ] = left_array[ left_pos ]
                left_pos += 1


def main():
    import random
    import sys
    import datetime


    TEST_SAMPLE = 100000
#    a = [ 7, 9, 3, 2, 8, 10, 28, 30, 11, 21, 3 ]
    a = [random.randrange( TEST_SAMPLE ) for x in range( TEST_SAMPLE )]

    ms = MargeSort()
    start = datetime.datetime.now()
    ms.sort( a )
    end = datetime.datetime.now()

    time = end - start

    for i in range( len(a) ):
        if i == 0: continue
        assert a[i-1] <= a[i]

    if TEST_SAMPLE <= 1000:
        p_time = time.microseconds
        t = 'microseconds'
    elif TEST_SAMPLE < 10000000:
        p_time = time.microseconds / 1000
        t = 'milliseconds'

    print(('Sample: %d\ntime:%d %s' % \
            (TEST_SAMPLE, p_time, t)))

if __name__ == '__main__':
    import sys
    import cProfile
    cProfile.run('main()')
#    main()
