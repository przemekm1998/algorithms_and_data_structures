class CyclicShift:

    @staticmethod
    def find(input_data):
        if len(input_data) == 0:
            return None

        low = 0
        high = len(input_data) - 1

        while low < high:
            mid = (low + high) // 2

            if input_data[mid] > input_data[high]:
                low = mid + 1
            elif input_data[mid] <= input_data[high]:
                high = mid

        return low
