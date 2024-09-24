# hello.py
def my_function1():
    print("Hello, world! Testing 111")
    # Your function code here
    pass

def my_function2():
    print("Hello, world! Testing 222")
    # Your function code here
    pass

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        func_name = sys.argv[1]
        globals()[func_name]()
    else:
        my_function1()
        my_function2()

