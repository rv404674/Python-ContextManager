
#with statement ensures that the file is closed automatically
#once the write operation is closed

with open('test.txt', 'w') as f:
	f.write('hello world')

#finally - finally block will always be executed, no matter if try block raises an error or not.
#The 'with' basically does this
f = open('test.txt', 'w')
try:
	f.write("Hwllo WOrld")
finally:
		f.close()

#Context Manager
#THis context Manager emulates what does the 'open' did above
#execcuted on CLI

class ContextManager(): 
    def __init__(self): 
        print('init method called') 
          
    def __enter__(self): 
        print('enter method called') 
        return self
      
    def __exit__(self, exc_type, exc_value, exc_traceback): 
        print('exit method called') 
  
  
with ContextManager() as manager: 
    print('with statement block') 