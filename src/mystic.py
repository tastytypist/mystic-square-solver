import copy
import heapq
import os
import random
import timeit


class MysticSquare:
    def __init__(self, source_file):
        self.__SOLUTION = ("1", "2", "3", "4", "5", "6", "7", "8", "9",
                           "10", "11", "12", "13", "14", "15", "-")
        self.__VALID_MOVES = ("up", "right", "down", "left")

        self.__inversion_count = 0
        self.__moves = []
        self.__node_count = 0
        self.__solution_stack = []
        self.__source_file = source_file
        self.__tiles = []
        self.__time = 0

    def build_mystic_square(self):
        if not self.__source_file:
            self.__tiles = random.sample(self.__SOLUTION, len(self.__SOLUTION))
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

    def display_mystic_square(self, tiles=None):
        if not tiles:
            tiles = self.__tiles
        for i in range(len(tiles)):
            print(tiles[i], end="")
            if i % 4 != 3:
                print(end=" ")
            else:
                print(end="\n")
        print()

    def solvable_check(self):
        self.__time = timeit.default_timer()
        for i in range(1, 17):
            inversion_count = 0
            if i == 16:
                inversion_count += 15 - self.__tiles.index("-")
            else:
                for j in range(1, i):
                    if self.__tiles.index(str(j)) > self.__tiles.index(str(i)):
                        inversion_count += 1
            print(f"Inversion count of {i}: {inversion_count}")
            self.__inversion_count += inversion_count

        if self.__tiles.index("-") % 8 in (2, 3, 4, 6):
            self.__inversion_count += 1

        print()
        print(f"Inversion sum: {self.__inversion_count}")
        print()

    def solve_mystic(self):
        if self.__inversion_count % 2 == 1:
            print("Mystic square is not solvable :(")
        else:
            start_instance = copy.deepcopy(self.__tiles)
            self.__build_tree(start_instance)
            self.__time -= timeit.default_timer()
            self.__time *= -1

    def __build_tree(self, start_instance, depth=1):
        blank_index = start_instance.index("-")
        for move in self.__VALID_MOVES:
            tile_instance = copy.deepcopy(start_instance)

            if move == "up" and blank_index not in (0, 1, 2, 3):
                (tile_instance[blank_index],
                 tile_instance[blank_index - 4]) = (tile_instance[blank_index - 4],
                                                    tile_instance[blank_index])
                self.__node_count += 1
            elif move == "right" and blank_index not in (3, 7, 11, 15):
                (tile_instance[blank_index],
                 tile_instance[blank_index + 1]) = (tile_instance[blank_index + 1],
                                                    tile_instance[blank_index])
                self.__node_count += 1
            elif move == "down" and blank_index not in (12, 13, 14, 15):
                (tile_instance[blank_index],
                 tile_instance[blank_index + 4]) = (tile_instance[blank_index + 4],
                                                    tile_instance[blank_index])
                self.__node_count += 1
            elif move == "left" and blank_index not in (0, 4, 8, 12):
                (tile_instance[blank_index],
                 tile_instance[blank_index - 1]) = (tile_instance[blank_index - 1],
                                                    tile_instance[blank_index])
                self.__node_count += 1
            else:
                continue

            cost = self.__calculate_cost(tile_instance, depth)
            heapq.heappush(self.__moves, (cost, depth, tile_instance))

        next_instance = heapq.heappop(self.__moves)
        self.__solution_stack.append(next_instance)
        if tuple(next_instance[2]) == self.__SOLUTION:
            tree_leaves = copy.deepcopy(self.__moves)
            for instance in tree_leaves:
                if instance[0] > next_instance[0]:
                    self.__moves.remove(instance)
            if len(self.__moves) > 1:
                next_instance = heapq.heappop(self.__moves)
                depth -= next_instance[1]
                for _ in range(depth):
                    self.__solution_stack.pop()
                self.__build_tree(next_instance[2], depth)
        else:
            self.__build_tree(next_instance[2], depth + 1)

    @staticmethod
    def __calculate_cost(instance, depth):
        incorrect_position = 0

        for i in range(len(instance)):
            if instance[i] == "-":
                continue
            elif instance[i] != str(i + 1):
                incorrect_position += 1

        return incorrect_position + depth

    def print_solution(self):
        if self.__solution_stack:
            print("Solution steps:\n")
            self.display_mystic_square()
            for i in range(len(self.__solution_stack)):
                self.display_mystic_square(self.__solution_stack[i][2])

            print(f"Execution time: {self.__time} s")
            print(f"Nodes generated: {self.__node_count}")
