# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_map.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/28 17:47:08 by alvgomez          #+#    #+#              #
#    Updated: 2023/03/28 20:37:24 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_map(function_to_apply, iterable):
    """ Map the function to all elements of the iterable. 
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
       yield function_to_apply(item)


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    print(ft_map(lambda dum: dum + 1, x))
    print(list(ft_map(lambda dum: dum + 1, x)))