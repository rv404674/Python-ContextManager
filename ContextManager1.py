class ManagedFile:
     def __init__(self,name):
            self.name = name
     def __enter__(self):
            self.file = open(self.name, 'w')
            return self.file
     def __exit__(self, exc_type, exc_val, exc_tb):
            if self.file:
                self.file.close()
 
with ManagedFile('hello.txt') as f:
    f.write("hello, world!")

mf = ManagedFile('hello.txt')
#mf
#<__main__.ManagedFile instance at 0x7f726478ef80>
#mf.file
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: ManagedFile instance has no attribute 'file'

with mf as the_file:
    the_file.write('hello.txt')
 
#behind the scenes, this statement 'with mf as the_file'
# will call __enter__() and assign the return value to the_file and 
#then when we leave this context, python will call __exit__ method. 

