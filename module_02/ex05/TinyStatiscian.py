# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    TinyStatiscian.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/15 16:22:38 by alvgomez          #+#    #+#              #
#    Updated: 2023/06/15 17:02:53 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class TinyStatistician:
    def mean(self, x):
        if not isinstance(x, list) or not x:
            return None
        size = len(x)
        if size == 0:
            return None
        return float(sum(x) / size)

    def median(self, x: list):
        if not isinstance(x, list) or not x:
            return None
        size = len(x)
        if size == 0:
            return None
        return float(sorted(x)[size // 2])
    
    def quartiles(self, x):
        if not isinstance(x, list) or not x:
            return None
        size = len(x)
        if size == 0:
            return None
        x = sorted(x)
        return [float(x[size // 4]), float(x[size * 3 // 4])]

    def var(self, x):
        if not isinstance(x, list) or not x:
            return None
        size = len(x)
        if size == 0:
            return None
        numb = map((lambda n: pow(n - self.mean(x), 2)), x)
        return float(sum(numb) / size)

    def std(self, x):
        if not isinstance(x, list) or not x:
            return None
        return self.var(x) ** 0.5


if __name__ == "__main__":
    tstat = TinyStatistician()
    a = [1, 42, 300, 10, 59]
    print(tstat.mean(a))
    # Expected result: 82.4
    print(tstat.median(a))
    # Expected result: 42.0
    print(tstat.quartiles(a))
    # Expected result: [10.0, 59.0]
    print(tstat.var(a))
    # Expected result: 12279.439999999999
    print(tstat.std(a))
    # Expected result: 110.81263465868862