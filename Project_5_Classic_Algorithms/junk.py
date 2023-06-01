class X:
    x = 1

    def __repr__(self) -> str:
        return 4


x = X()

print(type(x))