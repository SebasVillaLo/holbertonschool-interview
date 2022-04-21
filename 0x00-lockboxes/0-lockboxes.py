#!/usr/bin/python3
def canUnlockAll(boxes):
    unlocked = [0]
    for index_box, value_box in enumerate(boxes):
        # if not value_box:
        #     continue
        for key in value_box:
            if key < len(boxes) and key not in unlocked and key != index_box:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
