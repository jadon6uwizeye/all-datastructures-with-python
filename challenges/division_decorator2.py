def smart_div(func):
    
    def inner(a,b):
        if a<b:
            return func(b,a)
        return(func(a,b))
    return inner
    
@smart_div 
def div(a,b):
    '''
    definning with this syntax is the same as this from the previous example
    '''
    print (a/b)
   
    
div(2,4)