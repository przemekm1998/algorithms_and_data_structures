class ArrayAdvance:
    @staticmethod
    def array_advance(array):
        furthest_reached = 0
        for i in range(0, len(array)):
            if i > furthest_reached:
                return False
            else:
                distance = array[i] + i
                furthest_reached = max(furthest_reached, distance)
                if furthest_reached >= len(array):
                    return True
