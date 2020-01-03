class FixedPoint:

    @staticmethod
    def fixed_point(input_data):
        # Empty array case
        if len(input_data) == 0:
            return None

        input_data.sort()  # Array sort

        high = len(input_data) - 1
        low = 0

        while low <= high:
            mid = (low + high) // 2
            if input_data[mid] == mid:
                return mid
            elif input_data[mid] < mid:
                low = mid + 1
            else:
                high = mid - 1
        return None
