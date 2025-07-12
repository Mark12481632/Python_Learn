# #######################################
# Examples of creating a Context Manager.
# #######################################

from contextlib import contextmanager

# Class version:
class Create_Generator:
    def __init__(self, ftn, seq):
        """
        Executed when Create_Generator encounteres in the
        "with".
        """
        self.ftn = ftn
        self.seq = seq


    def __enter__(self):
        """
        """
        self.gen = (self.ftn(x) for x in self.seq)
        return self.gen
    
    def __exit__(self, exc_type, exc_val, traceback):
        """
        Exiting the context - so delete the generator
        """
        del self.gen


# Function version
@contextmanager
def Generator(ftn, seq):
    gen = (ftn(x) for x in seq)
    yield gen
    del gen


# ===============================

# Function to apply:
def square(x):
    return x*x

# Sequence to apply function to (could also by generator!)
num_list = list(range(20))

# Silly example - but just to test (class version)
with Create_Generator(square, num_list) as g:
    for x in g:
        print(x)

print("================================")

# Silly example - but just to test (function version)
with Generator(square, num_list) as g:
    for x in g:
        print(x)
