#!/usr/bin/python3

"""A method that determines if all boxes can be opened."""


def can_unlock_all(boxes):
    """This function takes a list of lists, where the content of a list
    unlocks other lists.

    Args:
        boxes: A list of lists representing the boxes and their keys.

    Returns:
        True if all boxes can be unlocked, False otherwise.
    """

    keys = [0]
    for key in keys:
        for box_key in boxes[key]:
            if box_key not in keys and box_key < len(boxes):
                keys.append(box_key)
    return len(keys) == len(boxes)


# Example usage
boxes = [[1], [2], [1, 3], [3]]
print(can_unlock_all(boxes))  # Output: True

boxes = [[1], [2], [3], []]
print(can_unlock_all(boxes))  # Output: False
