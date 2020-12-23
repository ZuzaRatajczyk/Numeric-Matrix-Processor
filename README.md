# Numeric-Matrix-Processor
This is one of my projects realized on JetBrains Academy course. 
The assumption of the project was to create program performing basics operations on matrices.

# Class Matrix 
I've created class Matrix witch instance representes a single matrix. 
Its parameter in constructor is list of rows which represents matrix.
Its attributes are:
* matrix
* num_of_rows
* num_of_columns

# Class methods
To perform addition and multiplication I've used operators overloading. 
Special function `__add__` enables using '+' operator on two instances of the class.
Special function `__mul__` enables using '*' operator on two instances of the class or on instance and number.
They are returning result matrix of operation as the object of the class.

`transpose` function is based on list comprehension. 
It takes tranposition type as argument.
It allows four types of transposition: ```"main diagonal", "side diagonal", "vertical line", "horizontal line"  ```
  
Transposed matrix is returned as class instance.
 
`determinant` is a recursive function. It takes matrix as list of rows as argument. 
Base cases of this function are:
  * matrix 1x1 dimension when determinant is equal to the single element of the matrix
  * matrix 2x2 dimension when determinant  is equal to the difference between the product of elements on the main diagonal 
    and the product of elements on the side diagonal
The recursive case of the function returns determinat of matrix. Its computing the determinant of a matrix by first-row expansion.

`inverse matrix` is based on previous functions and some auxiliary functions.
Inverse matrix is returned as instance object.

Class also has function `show matrix` which shows matrix in rows and columns.

# Demo program
Program enables to perfom basic operations on matrices witch is: 
  * add two matrices 
  * multiply matrice by number 
  * matrix by matrix multilication
  * transpose
  * find determinant 
  * inverse matrix
User can choose one of the options from the menu by writing its corresponding number.
  
  It takes dimemnsion of matrix as two integers separeted by space.
  Then takes each row separated by enter and at the end shows result of the operation (matrix or determinant).
