# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    banking_test3.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 18:15:37 by alvgomez          #+#    #+#              #
#    Updated: 2023/04/13 18:27:00 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from the_bank import Account, Bank

if __name__ == "__main__":
    bank = Bank()
    acc_valid_1 = Account('Sherlock Holmes',
                          zip='NW1 6XE',
                          addr='221B Baker street',
                          value=1000.0)
    
    acc_valid_2 = Account('James Watson',
                          zip='NW1 6XE',
                          addr='221B Baker street',
                          value=25000.0,
                          info=None)
    
    acc_invalid_4 = Account("Douglass",
                            zip='42',
                            addr='boulevard bessieres',
                            value=42)
    acc_invalid_1 = Account("Adam",
                            value=42,
                            zip='0',
                            addr='Somewhere')
    acc_invalid_2 = Account("Bender Bending RodrÃ­guez",
                            zip='1',
                            addr='Mexico',
                            value=42)
    acc_invalid_3 = Account("Charlotte",
                            zip='2',
                            addr='Somewhere in the Milky Way',
                            value=42)
    acc_invalid_5 = Account("Edouard",
                            zip='3',
                            addr='France',
                            value=42)
    
    bank.add(acc_valid_1)
    bank.add(acc_valid_2)
    bank.add(acc_invalid_1)
    bank.add(acc_invalid_2)
    bank.add(acc_invalid_3)
    bank.add(acc_invalid_4)