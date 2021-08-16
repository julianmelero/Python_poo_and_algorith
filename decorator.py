def deco(function):
    def Hi():
        print('Hi')              
        function()
        print('Goodbye')
    return Hi
    

@deco
def goodbye():
    print('Hi!')    



if __name__ == '__main__':
    goodbye()

