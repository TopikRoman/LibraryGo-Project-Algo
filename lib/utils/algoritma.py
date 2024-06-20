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
    
def dynamic_binary_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:

        mid = (low + high) // 2

        data_search = data[mid][0]
        target_search = target
        
        if type(target) != int :
            data_search = data[mid][1].lower()
            target_search = target.lower()


        if data_search == target_search:
            return mid
        elif data_search < target_search:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def linear_search(data, search_term, key_index):
    results = []
    for row in data:
        if row[key_index].lower() == search_term.lower():
            results.append(row)
    return results