#!/usr/bin/python3
"""A method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """This function will take a list of lists and the content
       of a list will unlock other lists
    """

    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    return len(keys) == len(boxes)  # More concise check

# Remove the blank line with whitespace (if your editor adds it)
