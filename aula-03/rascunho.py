def foo(valor):
    if valor:
        print("Valor é verdadeiro")
    else:
        print("Valor é falso")

foo("")
foo(None)
foo("Teste")
print(bool(""))
print(bool("abcdef"))