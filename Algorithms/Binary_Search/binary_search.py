class BinarySearch:

    @staticmethod
    def binary_search_iterative(data_input, target):
        if len(data_input) == 0:
            return False

        high = len(data_input) - 1
        low = 0

        data_input.sort()

        while low <= high:
            mid = (high + low) // 2
            if target == data_input[mid]:
                return data_input[mid]
            elif (mid - 1 >= 0) and (mid + 1 < len(data_input)):
                closest_low = abs(target - data_input[mid - 1])
                closest_high = abs(target - data_input[mid + 1])
                closest_mid = abs(target - data_input[mid])

                if (closest_mid <= closest_low) and (closest_mid <= closest_high):
                    return data_input[mid]
                elif closest_high < closest_low:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                return data_input[mid]
        return False
