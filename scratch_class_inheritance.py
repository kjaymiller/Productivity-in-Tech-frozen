class Foo:
    a = "Foo"


class Bar(Foo):
    a = 'Bar'
    b = 'Bar'


class Boo:

    class Foo(Foo):
        a = 'Boo'

    class Bar(Foo, Bar):
        pass

print(Bar().a)
print(Boo().Bar().a)
print(Boo().Bar().b)
print(Bar().a)

