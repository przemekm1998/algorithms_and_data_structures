class Intersection:
    @staticmethod
    def check(array1, array2):
        result = list()

        if len(array1) == 0 or len(array2) == 0:
            return result

        i = 0  # Pointer for the first array
        j = 0  # Pointer for the second array
        matches = dict()

        # Sorting the arrays
        array1.sort()
        array2.sort()

        # Traversing the two arrays
        while i < len(array1) and j < len(array2):
            # Intersection found
            if array1[i] == array2[j]:
                value = array1[i]
                if value not in matches:
                    matches[value] = 1
                    result.append(value)
                i += 1
                j += 1
            elif array1[i] < array2[j]:
                i += 1
            else:
                j += 1

        return result
