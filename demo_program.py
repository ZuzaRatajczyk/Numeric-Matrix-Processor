from matrix import Matrix


def get_list_of_rows(dimension):
    rows = []
    for _ in range(int(dimension[0])):
        row = input().split()
        row = [float(num) for num in row]
        rows.append(row)
    return rows


def get_data(ordinal=" "):
    dimension = input(f"Enter size of{ordinal}matrix: ").split()
    list_of_rows = get_list_of_rows(dimension)
    matrix = Matrix(list_of_rows)
    return matrix


def main():
    operation = "start"
    while operation:
        print("1. Add matrices\n2. Multiply matrix by a constant\n"
              "3. Multiply matrices\n4. Transpose matrix\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit")
        operation = input("Your choice: ")
        if operation == "1":
            matrix1 = get_data(ordinal=" first ")
            matrix2 = get_data(ordinal=" second ")
            result_matrix = matrix1 + matrix2
            print("The result is:")
            result_matrix.show_matrix()
        elif operation == "2":
            matrix = get_data()
            constant = float(input("Enter constant: "))
            if constant % 1 == 0:
                constant = int(constant)
            result_matrix = matrix * constant
            print("The result is:")
            result_matrix.show_matrix()
        elif operation == "3":
            matrix1 = get_data(ordinal=" first ")
            matrix2 = get_data(ordinal=" second ")
            result_matrix = matrix1 * matrix2
            print("The result is:")
            result_matrix.show_matrix()
        elif operation == "4":
            print("1. Main diagonal\n2. Side diagonal\n3.Vertical diagonal\n4.Horizontal diagonal")
            transpose_type = input()
            matrix = get_data()
            t_matrix = matrix.transpose(transpose_type)
            print("The result is:")
            t_matrix.show_matrix()
        elif operation == "5":
            matrix = get_data()
            determinant = matrix.determinant(matrix.matrix)
            print("The result is:")
            print(determinant)
        elif operation == "6":
            matrix = get_data()
            inverse_matrix = matrix.inverse_matrix()
            print("The result is:")
            inverse_matrix.show_matrix()
        else:
            operation = 0


if __name__ == "__main__":
    main()