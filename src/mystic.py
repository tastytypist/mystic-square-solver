import heapq
import os
import random
import timeit


class MysticSquare:
    def __init__(self, source_file):
        self.__VALID_TILES = (1, 2, 3, 4, 5, 6, 7, 8, 9,
                              10, 11, 12, 13, 14, 15, "-")

        self.__moves = []
        self.__node_count = 0
        self.__source_file = source_file
        self.__tiles = []
        self.__time = 0

