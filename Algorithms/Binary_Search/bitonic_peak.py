class BitonicPeak:

    @staticmethod
    def bitonic_search(input_data):
        # Bitonic search need at least 3 elements in array
        if len(input_data) < 3:
            return None

        low = 0
        high = len(input_data) - 1

        while low <= high:
            mid = (low + high) // 2

            mid_left = input_data[mid - 1] if mid - 1 > 0 else float("-inf")
            mid_right = input_data[mid + 1] if mid + 1 < len(input_data) else float("inf")

            # if (input_data[mid] > mid_left) and (input_data[mid] < mid_right):

