# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/16 17:43:11 by alvgomez          #+#    #+#              #
#    Updated: 2023/04/12 18:14:01 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

n = len(sys.argv)
if n > 1:
    assert n < 4, "too many arguments"
    assert n != 2, "not enough arguments"
    A = sys.argv[1]
    B = sys.argv[2]
    try:
        A = int(A)
        B = int(B)
    except ValueError:
        raise AssertionError("only integers")
    try:
        print("Sum:        ", A + B)
        print("Difference: ", A - B)
        print("Product:    ", A * B)
        print("Quotient:   ", A / B)
        print("Reminder:   ", A % B)
    except ZeroDivisionError:
        print("Quotient:    ERROR (division by zero)")
        print("Reminder:    ERROR (module by zero)")