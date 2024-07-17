# 1. Positional Arguments


# 2. Default Argument Values


# 3. Keyword Arguments


# 4. Arbitrary Argument Lists


# 5. Arbitrary Keyword Argument Lists


# 인자의 모든 종류를 적용한 예시
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print('pos1:', pos1)
    print('pos2:', pos2)
    print('default_arg:', default_arg)
    print('args:', args)
    print('kwargs:', kwargs)


func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')
