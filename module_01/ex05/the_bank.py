# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    the_bank.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/28 15:05:28 by alvgomez          #+#    #+#              #
#    Updated: 2023/04/13 17:39:41 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Account(object): 
    
    ID_COUNT = 1
    
    def __init__(self, name, **kwargs): 
        self.__dict__.update(kwargs)
        
        self.id = self.ID_COUNT 
        Account.ID_COUNT += 1 
        self.name = name
        if not hasattr(self, "value"):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
    
    def transfer(self, amount): 
        self.value += amount

class Bank(object):
    '''The bank'''
    def __init__(self):
        self.accounts = []
        
    def check_account(self, new_account):
        #if not isinstance(new_account, Account):
        #    print("New account is not class Account")
        #    return False
        account = None
        for item in self.accounts:
            if item.name == new_account:
                account = item
        if account == None:
            #print("Account does not exist")
            return(False)
        if len(account.__dict__) % 2 == 0:
            #print("Number of attributes in new account is an even number")
            return False
        for key, value in account.__dict__.items():
            if key[0] == 'b':
                #print("Attribute in new account starts with 'b'")
                return False
        if account.__dict__.get("zip") == None:
            #print("New account must have zip")
            return False
        if account.__dict__.get("addr") == None:
            #print("New account must have addr")
            return False
        if account.__dict__.get("name") == None or account.__dict__.get("id") == None or account.__dict__.get("value") == None:
            #print("New account must have name, id and value")
            return False
        if not isinstance(account.name, str):
            #print("Name of new account must be a str")
            return False
        if not isinstance(account.id, int):
            #print("Id of new account must be an int")
            return False
        if not isinstance(account.value, int) and not isinstance(account.value, float):
            #print("Value of new account must be int or float")
            return False
        return True
    
    def add(self, new_account):
        """ Add new_account in the Bank
            @new_account: Account() new account to append
            @return   True if success, False if an error occured
        """
        if new_account in self.accounts:
            #print("New account already exists")
            return False
        #if not self.check_account(new_account):
        #    #print("New account cannot be added")
        #    return False
        self.accounts.append(new_account)
        #print("Success")
        return True
    
    def transfer(self, origin, dest, amount):
        """ Perform the fund transfer
            @origin:  str(name) of the first account
            @dest:    str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return   True if success, False if an error occured
        """
        acc_o = None
        for item in self.accounts:
            if item.name == origin:
                acc_o = item
        if acc_o == None:
            #print("Account origin does not exist")
            return(False)
        acc_d = None
        for item in self.accounts:
            if item.name == dest:
                acc_d = item
        if acc_d == None:
            #print("Account origin does not exist")
            return(False)
        if not self.check_account(origin):
            #print("Account oringin is not valid")
            return False
        if not self.check_account(dest):
            #print("Account dest is not valid")
            return False
        if amount < 0:
            #print("Amount must be a positive number")
            return False
        if acc_o.value < amount:
            #print("Not enough balance in origin account")
            return False
        if acc_o != acc_d:
            acc_o.value -= amount
            acc_d.value += amount
        #print("Success")
        return True

    def fix_account(self, name):
        """ fix account associated to name if corrupted
            @name:   str(name) of the account
            @return  True if success, False if an error occured
        """
        if not isinstance(name, str):
            #print("Name is not a str")
            return False
        account = None
        for item in self.accounts:
            if item.name == name:
                account = item
                
        if account == None:
            #print("Account does not exist in the bank")
            return False
        #Here we fix some values
        for key, value in account.__dict__.items():
            if key[0] == 'b':
                account.__delattr__(key)
                #print(f"Deleted the attibute {key}")
        if account.__dict__.get("zip") == None:
            account.__setattr__("zip", 0)
        if account.__dict__.get("addr") == None:
            account.__setattr__("addr", 0)
        if len(account.__dict__) % 2 == 0:
            account.__setattr__("extra", 0)
        return True

#if __name__ == "__main__":
#    account_1 = Account("Pepe", value=2000, pepa=3, zip=9)
#    account_2 = Account("caca", value=2000, pepa=3, zip=9)
#    bank = Bank()
#    bank.add(account_1)
#    account_1.__setattr__("bola", 2)
#    bank.transfer(account_1, account_2, 300)
#    print(account_1.value)
#    bank.fix_account("Pepe")
#    print(account_1.bola)
    
    
    