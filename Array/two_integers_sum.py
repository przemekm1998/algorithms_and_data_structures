class TwoIntegersSum:
    @staticmethod
    def check(array, input_sum):
        array.sort()  # Sorting the array

        # Setting up pointers
        i = 0
        j = len(array) - 1

        while i < j:
            sumed = array[i] + array[j]
            if sumed == input_sum:
                return [array[i], array[j]]
            elif sumed < input_sum:
                i += 1
            else:
                j -= 1
        return None


class ThreeIntegersSum:
    @staticmethod
    def check(array, input_sum):
        array.sort()  # Sorting the array

        for i in range(0, len(array) - 1):
            x = array[i]  # Taking the first element of the sum
            to_find = input_sum - x  # Calculating the sum of the other two integers

            # Setting up pointers
            start_pointer = i + 1
            end_pointer = len(array) - 1

            # Seeking for the required sum of the two integers
            while start_pointer < end_pointer:
                sumed = array[start_pointer] + array[end_pointer]
                if sumed == to_find:
                    return [array[i], array[start_pointer], array[end_pointer]]
                elif sumed < input_sum:
                    start_pointer += 1
                else:
                    end_pointer -= 1

        return None
