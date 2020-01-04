class IntSquareRoot:

    @staticmethod
    def calc_root(k):
        if k < 0:
            return None

        low = 0
        high = k // 2
        mid = 1

        while low <= high:
            mid = (low + high) // 2
            mid_square_root = mid * mid
            print("mid square root: " + str(mid_square_root))
            print("mid: " + str(mid))

            if mid_square_root > k:
                high = mid - 1
            elif mid_square_root < k:
                low = mid + 1

        return mid
