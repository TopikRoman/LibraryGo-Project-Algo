def merge_sort(data, key, secondary_key=None):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(left_half, key, secondary_key)
        merge_sort(right_half, key, secondary_key)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i][key] < right_half[j][key]:
                data[k] = left_half[i]
                i += 1
            elif left_half[i][key] > right_half[j][key]:
                data[k] = right_half[j]
                j += 1
            else:  # if primary keys are equal
                if secondary_key is not None:
                    if left_half[i][secondary_key] < right_half[j][secondary_key]:
                        data[k] = left_half[i]
                        i += 1
                    else:
                        data[k] = right_half[j]
                        j += 1
                else:
                    data[k] = left_half[i]
                    i += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1
            
    return data


def binary_search(data, target, key):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if data[mid][key].lower() == target.lower():
            return mid
        elif data[mid][key].lower() < target.lower():
            low = mid + 1
        else:
            high = mid - 1

    return -1

def binary_search_for_id(data, target, key):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if data[mid][key] == target:
            return mid
        elif data[mid][key] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1