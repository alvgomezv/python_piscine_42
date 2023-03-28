# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_filter.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/28 17:47:30 by alvgomez          #+#    #+#              #
#    Updated: 2023/03/28 20:45:55 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_filter(function_to_apply, iterable):
    """ Filter the result of function apply to all elements of the iterable. 
        Args:
            function_to_apply: a function taking an iterable.
            iterable: an iterable object (list, tuple, iterator). 
        Return:
            An iterable.
            None if the iterable can not be used by the function. 
    """
    if not callable(function_to_apply):
        raise AttributeError("function_to_apply must be a function")
    try:
        iter(iterable)
    except:
        raise AttributeError("iterable must be an iterable object")
    for item in iterable:
        if function_to_apply(item):
            yield item
    
if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    print(ft_filter(lambda dum: not (dum % 2), x))
    print(list(ft_filter(lambda dum: not (dum % 2), x)))