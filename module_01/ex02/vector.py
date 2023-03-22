# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/21 18:12:02 by alvgomez          #+#    #+#              #
#    Updated: 2023/03/22 13:42:54 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Vector:
    def __init__(self, values):
        if isinstance(values, list):
            self.values = values
            if len(values) == 1:
                a = 1
                b = len(values[0])
            else:
                a = len(values)
                b = 1  
            self.shape = (a,b)
        else:
            print("Vectors must be lists of floats")

    def dot(self, v2):
        if self.shape == v2.shape:
            sum = 0
            if self.shape[0] == 1:
                for a, b in zip(self.values[0], v2.values[0]):
                  sum = sum + (a * b)
            else:
                for a, b in zip(self.values, v2.values):
                  sum = sum + (a[0] * b[0])
            return sum
        else:
            print("Vectors must have the same shape")

    def T(self):
        vect = []
        if self.shape[0] == 1:
            for val in self.values[0]:
                temp = []
                temp.append(val)
                vect.append(temp)
        else:
            temp = []
            for val in self.values:
                 temp.append(val[0])
            vect.append(temp)
        return Vector(vect)
    
    def __str__(self):
        return str(self.values)
    
    def __repr__(self):
        return str(self.values)
    
    def __add__(self, other):
        if isinstance(other, float):
            vector = []
            if self.shape[0] == 1:
                temp = []
                for a in self.values[0]:
                    temp.append(a + other)
                vector.append(temp)  
            else:
                for a in self.values:
                    temp = []
                    temp.append(a[0] + other)
                    vector.append(temp)
            return Vector(vector)
        elif isinstance(other, Vector):
            if self.shape == other.shape:
                vector = []
                if self.shape[0] == 1:
                    temp = []
                    for a, b in zip(self.values[0], other.values[0]):
                      temp.append(a + b)
                    vector.append(temp)
                else:
                    for a, b in zip(self.values, other.values):
                      temp = []
                      temp.append(a[0] + b[0])
                      vector.append(temp)
                return Vector(vector)
            else:
                print("Vectors must have the same shape")
        else:
            print("Values must be Vectors or floats")

    def __radd__(self, other):
        return (self + other)

    def __sub__(self, other):
        if isinstance(other, float):
            vector = []
            if self.shape[0] == 1:
                temp = []
                for a in self.values[0]:
                    temp.append(a - other)
                vector.append(temp)  
            else:
                for a in self.values:
                    temp = []
                    temp.append(a[0] - other)
                    vector.append(temp)
            return Vector(vector)
        elif isinstance(other, Vector):
            if self.shape == other.shape:
                vector = []
                if self.shape[0] == 1:
                    temp = []
                    for a, b in zip(self.values[0], other.values[0]):
                      temp.append(a - b)
                    vector.append(temp)
                else:
                    for a, b in zip(self.values, other.values):
                      temp = []
                      temp.append(a[0] - b[0])
                      vector.append(temp)
                return Vector(vector)
            else:
                print("Vectors must have the same shape")
        else:
            print("Values must be Vectors or floats")

    def __rsub__(self, other):
        print("NotImplementedError: Subtraction of a scalar by a Vector is not defined here")

    def __mul__(self, other):
        if isinstance(other, float):
            if self.shape[0] == 1:
                for i in range(len(self.values[0])):
                    self.values[0][i] *= other
            else:
                for i in range(len(self.values)):
                    self.values[i][0] *= other
            return self
        elif isinstance(other, Vector):
            print("NotImplementedError: Multiplication of Vectors is not defined here")
        else:
            print("Values must be Vectors or floats")
        
    def __rmul__(self, other):
        return (self * other)
    
    def __truediv__(self, other):
        if isinstance(other, float):
            if self.shape[0] == 1:
                for i in range(len(self.values[0])):
                    self.values[0][i] /= other
            else:
                for i in range(len(self.values)):
                    self.values[i][0] /= other
            return self
        elif isinstance(other, Vector):
            print("NotImplementedError: Division of Vectors is not defined here")
        else:
            print("Values must be Vectors or floats")
        
    def __rtruediv__(self, other):
        print("NotImplementedError: Division of sclara by a Vectors is not defined here")