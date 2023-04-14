# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/20 12:39:07 by alvgomez          #+#    #+#              #
#    Updated: 2023/04/14 11:50:29 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time

bar = {
	0  : "[                    ]",
	1  : "[>                   ]",
	2  : "[=>                  ]",
	3  : "[==>                 ]",
	4  : "[===>                ]",
	5  : "[====>               ]",
	6  : "[=====>              ]",
	7  : "[======>             ]",
	8  : "[=======>            ]",
	9  : "[========>           ]",
	10 : "[=========>          ]",
	11 : "[==========>         ]",
	12 : "[===========>        ]",
	13 : "[============>       ]",
	14 : "[=============>      ]",
	15 : "[==============>     ]",
	16 : "[===============>    ]",
	17 : "[================>   ]",
	18 : "[=================>  ]",
	19 : "[==================> ]",
	20 : "[===================>]",
	21 : "[====================]",
}

def change_numb(listy):
	numbers = list(listy)
	n = len(numbers)
	new = []
	for i in range(n):
		new.append(i)
	return new

def ft_progress(listy):
	numbers = change_numb(listy)
	n = len(numbers)
	t_start = time.time()
	eta = 0
	i = 0
	while i <= numbers[n - 1]:
		level = int(numbers[i]*20/n)
		print(f" ETA: {eta:5.2f}s [{int(numbers[i]*100/n):3d}%] {bar[level]} {numbers[i]:4d}/{n:4d} | elapsed time {time.time() - t_start:5.2f}s", end= "\r")
		yield numbers[i]
		if i == 0:							
			t = time.time() - t_start
		eta = t * (n - i)
		i += 1
	print (f" ETA:  0.00s [100%] {bar[21]} {(numbers[i - 1] + 1):4d}/{n:4d} | elapsed time {(time.time() - t_start):5.2f}s", end= "\r")

if __name__ == "__main__":
	listy = range(-100,200)
	ret = 0
	for elem in ft_progress(listy): 
		ret += (elem + 3) % 5
		time.sleep(0.01) 
	print()
	print(ret)