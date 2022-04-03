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

    def build_mystic_square(self):
        if not self.__source_file:
            self.__tiles = random.sample(self.__VALID_TILES,
                                         len(self.__VALID_TILES))
        else:
            self.__tiles = self.__parse_mystic_txt()

    def __parse_mystic_txt(self):
        os.chdir("../test/")
        file = open(self.__source_file, "r")
        raw_lines = file.readlines()
        file.close()

        mystic_tiles = []
        lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
        tile_rows = [line.split(" ") for line in lines]
        for tile_row in tile_rows:
            mystic_tiles.extend(tile_row)

        return mystic_tiles

    def display_mystic_square(self):
        for i in range(len(self.__tiles)):
            print(self.__tiles[i], end="")
            if i % 4 != 3:
                print(end=" ")
            else:
                print(end="\n")

