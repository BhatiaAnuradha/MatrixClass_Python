import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if len(self.g) == 1:
            det = self[0][0]
        else:
            det = (self[0][0] * self[1][1]) - (self[0][1] * self[1][0])
        return det

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        n = len(self.g)
        tr = 0
        for i in range(n):
            tr = tr + self[i][i]
        return tr

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        n = len(self.g)
        inv_self = zeroes(self.h, self.w)
        Iden = identity(n)
        trace = self.trace()
        det = self.determinant()
        #if isinstance(self, numbers.Number):
            #inv_self = 1./self
        if n == 1:
            inv_self[0][0] = (1./self[0][0])
            
        
        else:
            #det = self.determinant()
            #inv_self = (1./det) * (self.trace()*identity(n) - self)
            for i in range(self.h):
                for j in range(self.w):
                    inv_self[i][j] = (trace*Iden[i][j] - self[i][j])/det
        
        return inv_self

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        tran_self = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                tran_self[i][j] = self[j][i]
        return tran_self

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        n = self.h
        m = self.w
        mat_add = zeroes(n,m)
        for i in range(n):
            for j in range(m):
                mat_add[i][j] = self[i][j] + other[i][j]
        return mat_add

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        ng = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                ng[i][j] = -1 * self[i][j]
        return ng

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        n = self.h
        m = self.w
        mat_sub = zeroes(n,m)
        for i in range(n):
            for j in range(m):
                mat_sub[i][j] = self[i][j] - other[i][j]
        return mat_sub
    
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        n = self.h
        m = self.w
        p = other.w
        
        mat_mul = zeroes(n,p)
        for i in range(n):
            for j in range(p):
                mat_mul[i][j] = 0
                for k in range(m):
                    mat_mul[i][j] += self[i][k] * other[k][j]
        return mat_mul
    
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            r_mat = zeroes(self.h, self.w)
            for i in range(self.h):
                for j in range(self.w):
                    r_mat[i][j] = other * self[i][j]
            return r_mat
            