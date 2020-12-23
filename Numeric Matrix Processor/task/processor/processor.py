from copy import deepcopy


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix
        self.num_of_rows = len(matrix)
        self.num_of_columns = len(matrix[0])

    def __add__(self, matrix_to_add):
        if self.num_of_rows == matrix_to_add.num_of_rows and self.num_of_columns == matrix_to_add.num_of_columns:
            result_matrix = [[self.matrix[row][col] + matrix_to_add.matrix[row][col]
                             for col in range(self.num_of_columns)] for row in range(self.num_of_rows)]
            return Matrix(result_matrix)
        else:
            return "The operation cannot be performed."

    def __mul__(self, multiplier):
        if type(multiplier) == float or type(multiplier) == int:  # multiply by instant
            result_matrix = [[self.matrix[row][col] * multiplier
                              for col in range(self.num_of_columns)] for row in range(self.num_of_rows)]
            return Matrix(result_matrix)
        else:  # multiply two matrices
            if self.num_of_columns == multiplier.num_of_rows:
                result_matrix = []
                for n in range(self.num_of_rows):
                    row = []
                    for k in range(multiplier.num_of_columns):
                        element = 0
                        for m in range(self.num_of_columns):
                            element += self.matrix[n][m] * multiplier.matrix[m][k]
                        row.append(element)
                    result_matrix.append(row)
                return Matrix(result_matrix)
            else:
                return "The operation cannot be performed."

    def transpose(self, transpose_type):
        transposed_matrix = []
        if transpose_type == "1":  # main diagonal
            for i in range(self.num_of_columns):
                t_row = [row[i] for row in self.matrix]
                transposed_matrix.append(t_row)
            return Matrix(transposed_matrix)
        elif transpose_type == "2":  # side diagonal
            for i in reversed(range(self.num_of_columns)):
                t_row = [row[i] for row in self.matrix]
                t_row.reverse()
                transposed_matrix.append(t_row)
            return Matrix(transposed_matrix)
        elif transpose_type == "3":  # vertical diagonal
            for row in self.matrix:
                row.reverse()
                transposed_matrix.append(row)
            return Matrix(transposed_matrix)
        elif transpose_type == "4":  # horizontal diagonal
            for i in reversed(range(self.num_of_rows)):
                transposed_matrix.append(self.matrix[i])
            return Matrix(transposed_matrix)

    def determinant(self, matrix):
        num_of_rows = len(matrix)
        num_of_columns = len(matrix[0])
        if num_of_rows == 1:  # base case matrix 1x1
            return matrix[0][0]
        if num_of_rows == 2:  # base case matrix 2x2
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        else:   # recursive case
            det = 0
            for column in range(num_of_columns):
                minor = deepcopy(matrix[1:])
                for row in minor:
                    del row[column]
                det += self.determinant(minor) * matrix[0][column] * pow(-1, 1 + column + 1)
            return det

    @staticmethod
    def delete_row_column(matrix, row_idx, column_idx):  # matrix is a copy of self.matrix
        num_of_rows = len(matrix)
        num_of_columns = len(matrix[0])
        for row in range(num_of_rows):
            if row == row_idx:
                del matrix[row_idx]
        for row in matrix:
            for column in range(num_of_columns):
                if column == column_idx:
                    del row[column]
        return matrix

    def calculate_matrix_of_cofactors(self):
        list_of_cofactors = deepcopy(self.matrix)
        for row in range(self.num_of_rows):
            for column in range(self.num_of_columns):
                temp_matrix = deepcopy(self.matrix)
                temp_matrix = self.delete_row_column(temp_matrix, row, column)
                if row % 2 == 0:    # sign of the element in matrix of cofactors (sign pattern for cofactors)
                    if column % 2 == 0:
                        list_of_cofactors[row][column] = (self.determinant(temp_matrix))
                    else:
                        list_of_cofactors[row][column] = -(self.determinant(temp_matrix))
                else:
                    if column % 2 == 0:
                        list_of_cofactors[row][column] = -(self.determinant(temp_matrix))
                    else:
                        list_of_cofactors[row][column] = (self.determinant(temp_matrix))
        return Matrix(list_of_cofactors)

    def inverse_matrix(self):
        determinant = self.determinant(self.matrix)
        if determinant == 0:
            print("This matrix doesn't have an inverse.")
        else:
            matrix_of_cofactors = self.calculate_matrix_of_cofactors()
            t_matrix = matrix_of_cofactors.transpose("1")
            inverse_matrix = [[(t_matrix.matrix[row][col] * (1/determinant))
                              for col in range(self.num_of_columns)] for row in range(self.num_of_rows)]
            inverse_matrix = self._truncate_elements(inverse_matrix)
            return Matrix(inverse_matrix)

    @staticmethod
    def _truncate_elements(list_of_rows):
        for i, row in enumerate(list_of_rows):
            for j, num in enumerate(row):
                if type(num) == float:
                    num = int(num * 100) / 100
                    list_of_rows[i][j] = num
        return list_of_rows

    def show_matrix(self):
        matrix = ""
        for row in self.matrix:
            row = [int(num) if num % 1 == 0 else round(float(num), 2) for num in row]
            row = [str(num) for num in row]
            row = " ".join(row)
            matrix += (row + "\n")
        print(matrix)


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
