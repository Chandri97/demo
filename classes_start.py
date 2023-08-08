#
# Example file for working with classes
#

class myClass():
    def method1(self):
        print(" this is method 1")
    def method2(self, somearg):
        print(" this is method 2 " + somearg)


def main():
    c = myClass()
    c.method1()
    c.method2("this is something")


if __name__ == "__main__":
    main()
