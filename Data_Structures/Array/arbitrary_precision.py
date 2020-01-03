class ArbitraryPrecision:
    @staticmethod
    def increment_digit(array):
        index = len(array) - 1
        carry = 0
        array[index] = array[index] + 1  # Adding 1 to the last digit in array

        while carry >= 0 and index >= 0:
            # Adding carry for every element of array
            array[index] = array[index] + carry
            carry = 0

            # Element of array is greater than 9
            if array[index] > 9:
                carry = int(array[index] / 10)  # Calculating new carry
                array[index] = array[index] - (carry * 10)  # Calculating the proper digit

            # There is a carry after the last digit, ex. 999 + 1
            if index == 0 and carry > 0:
                array.insert(0, carry)
            index -= 1

        return array
