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


