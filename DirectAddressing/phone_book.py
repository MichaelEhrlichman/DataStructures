# python3

class PhoneBook:
    def __init__(self,size):
        self.data = [None]*size

    def add(self,number,name):
        self.data[number] = name
        return None

    def delete(self,number):
        self.data[number] = None
        return None

    def find(self,number):
        if self.data[number] == None:
            return 'not found'
        else:
            return self.data[number]

    def Query(self,query,number=-1,name=''):
        number_index = number 
        if query == 'add':
            return self.add(number_index,name)
        elif query == 'del':
            return self.delete(number_index)
        elif query == 'find':
            return self.find(number_index)

    @staticmethod
    def ProcessInput(Input):
        if len(Input) == 2:
            return Input[0], int(Input[1])
        else:
            return Input[0], int(Input[1]), Input[2]
        
if __name__ == '__main__':
    myPhoneBook = PhoneBook(10**7)
    n = int(input())
    results = [myPhoneBook.Query(*myPhoneBook.ProcessInput(input().split())) for _ in range(n)]
    print('\n'.join([x for x in results if x != None]))

