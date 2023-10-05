#!/usr/bin/python3
"""Write a method that determines if all the
boxes can be opened."""


def canUnlockAll(boxes):
    """Check if all of boxes can be open"""
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0]

    while stack:
        box_index = stack.pop()

        for key in boxes[box_index]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
