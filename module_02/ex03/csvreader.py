# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    csvreader.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/29 17:18:51 by alvgomez          #+#    #+#              #
#    Updated: 2023/03/29 20:47:38 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.is_there_a_header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.ret = True
        self.file = open(self.filename, 'r')
        for i in range(skip_top):
            self.file.readline()
        if header:
            self.header = self.file.readline().rstrip().split(sep)
            header_len = len(self.header)
        data = []
        while True:
            line = self.file.readline().rstrip()
            if not line:
                break
            data.append(line)
        if skip_bottom:
            data = data[:-skip_bottom]
        self.data = []
        for line in data:
            line = line.split(sep)
            if '' in line:
                self.ret = False
                break
            if len(line) != header_len:
                self.ret = False
                break
            self.data.append(line)
        
    def __enter__(self):
        return self if self.ret else None

    def __exit__(self, exc_type, exc_val, traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print(f"An exception of type {exc_type} occurred: {exc_val}")
        return True

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom. 
        Return:
                nested list (list(list, list, ...)) representing the data.
        """
        return self.data if self.ret else None
            
    def getheader(self):
        ''' Retrieves the header from csv file. 
        Returns:
                list: representing the data (when self.header is True). 
                None: (when self.header is False).
        '''
        return self.header if self.header else None

if __name__ == "__main__":
    with CsvReader('good.csv',',',True, 1, 2) as file:
        if not file:
            print("File is corrupted")
        else:
            data = file.getdata()
            print(data)
            print("--------")
            header = file.getheader()
            print(header)