import argparse

import mystic

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source",
                        help="text file containing your mystic square",
                        type=str)

    source_file = parser.parse_args()
    mystic_square = mystic.MysticSquare(source_file.source)
    mystic_square.build_mystic_square()
    mystic_square.display_mystic_square()
    mystic_square.solvable_check()
    mystic_square.solve_mystic()
    mystic_square.print_solution()
