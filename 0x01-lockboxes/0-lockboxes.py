#!/usr/bin/python3
def canUnlockAll(boxes):
    opened_boxes = {0}
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < len(boxes) and key not in opened_boxes:
                opened_boxes.add(key)
                stack.append(key)

    return len(opened_boxes) == len(boxes)

