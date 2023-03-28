# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_reduce.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/28 17:47:47 by alvgomez          #+#    #+#              #
#    Updated: 2023/03/28 20:59:22 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_reduce(function_to_apply, iterable):
    """ Apply function of two arguments cumulatively. 
        Args:
            function_to_apply: a function taking an iterable.
            iterable: an iterable object (list, tuple, iterator). 
        Return:
            A value, of same type of elements in the iterable parameter.
            None if the iterable can not be used by the function. 
    """
    if not callable(function_to_apply):
        raise AttributeError("function_to_apply must be a function")
    try:
        iter(iterable)
    except:
        raise AttributeError("iterable must be an iterable object")
    temp = iterable[0]
    for i in range(1, len(iterable)):
            temp = function_to_apply(temp, iterable[i])
    yield temp
        
        
if __name__ == "__main__":
    lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'] 
    print(list(ft_reduce(lambda u, v: u + v, lst)))