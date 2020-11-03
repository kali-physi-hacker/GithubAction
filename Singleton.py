"""
This is just a design pattern that ensures that an object is created only once in its life time.
Therefore, printing out the memory address of 2 instances of the object returns the same memory address
"""


class _PublicPrinter:
    def __init__(self):
        print("I am the main one and only instance")
    
    def print_document(self, document):
        """
        :return:
        """
        print("Printing Document\n","="*20)
        print(document)



def PublicPrinter():
    """
    Return an instance of the class
    :return
    """
    instance = None 
    if instance is None:
        instance = _PublicPrinter()
    return instance 



if __name__ == "__main__":
    printer = PublicPrinter
    printer2 = PublicPrinter

    # Print using printer 1
    printer().print_document("My name is Desmond Brown. I love science and mathematics")
    printer2().print_document("I am a scientist")

    print(id(printer))
    print(id(printer2))