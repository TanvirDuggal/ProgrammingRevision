# -*- coding: utf-8 -*-
"""
Created on Thu May 13 21:22:24 2021

@author: Tanvy
"""


def takeStep(robot, final, grid, counter=0):
    print(str(robot) + " " + str(counter))
    if robot == final:
        return counter

    if (robot[0] > grid[0]) or (robot[1] > grid[1]):
        return 0

    return takeStep([robot[0]+1, robot[1]], final, grid, counter+1)
    return takeStep([robot[0], robot[1]+1], final, grid, counter+1)


def main():
    robot = [0, 0]
    final = [1, 1]
    grid = [1, 1]

    print(takeStep(robot, final, grid))


if __name__ == '__main__':
    main()
