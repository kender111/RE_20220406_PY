def external_func(var1):
        def internal_func(var2):
                nonlocal var1
                var1 += 1
                return var1 + var2
        return internal_func
func = external_func(15)
print(func(10))
