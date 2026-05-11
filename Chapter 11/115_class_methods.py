class janina:
    a=1
    @classmethod
    def show(cls):
        print(f"The va;ue of class attribute is {cls.a}")


e = janina()

e.a = 55

e.show()