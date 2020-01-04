class FirstEntry:

    @staticmethod
    def entry_of(input_data, target):
        if len(input_data) == 0:
            return None

        input_data.sort()

        low = 0
        high = len(input_data) - 1

        while low <= high:
            mid = (low + high) // 2
            if input_data[mid] < target:
                low = mid + 1
            elif input_data[mid] > target:
                high = mid - 1
            else:
                if (mid - 1 < 0) or (mid + 1 > len(input_data) - 1):
                    return mid
                if input_data[mid - 1] != target:
                    return mid
                high = mid - 1
        return None
