# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/28 13:23:00 by alvgomez          #+#    #+#              #
#    Updated: 2023/04/13 16:27:16 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class valuator:
    def zip_evaluate(coefs, words):
        if isinstance(coefs, list) and isinstance(words, list) and len(coefs) == len(words):
            result = 0
            zipped = zip(coefs, words)
            for item in zipped:
                result += item[0] * float(len(item[1]))
            return result
        else:
            return -1
    def enumerate_evaluate(coefs, words):
        if isinstance(coefs, list) and isinstance(words, list) and len(coefs) == len(words):
            result = 0
            enum1 = enumerate(words)
            for index, value in enum1:
                result += coefs[index] * float(len(value))
            return result
        else:
            return -1

#if __name__ == "__main__":
#    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
#    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
#    print(evaluator.zip_evaluate(coefs, words))
#    words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
#    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
#    print(evaluator.enumerate_evaluate(coefs, words))