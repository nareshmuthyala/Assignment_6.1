"""
function to generate Vandermonde matrix
Steps:
1)Iterate the input array
2)for each item in array generate the list
3)append the generated list to matrix
4)return the matrix
"""
def generate_list(num, len):
    """
    This function generates each of the row of matrix
    :param num:
    :param len:
    :return: list
    """
    my_list = [1, num]
    i = 1
    temp_int = num
    while (i < len):
        temp_int = num * temp_int
        my_list.append(temp_int)
        i += 1
    return my_list


def generate_matrix(array, row_length, incresing=False):
    """
    function to generate Vandermonde matrix
    :param array:
    :param row_length:
    :param incresing:
    :return: list
    """
    my_list = list()
    for item in array:
        temp_list = generate_list(item, n - 1)
        if incresing==False:
            temp_list = temp_list[::-1]
        my_list.append(temp_list)
    return my_list

arr = [4, 3, 5, 6]
n = 6
print(generate_matrix(arr, n, True))
