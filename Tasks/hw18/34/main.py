from module import Checker


msg_ok = Checker.msg_ok
msg_err = Checker.msg_err

triangle1 = Checker(3, 4, 5)
assert triangle1.is_triangle() == msg_ok

triangle2 = Checker(77, 3, 4)
assert triangle2.is_triangle() == msg_err

triangle3 = Checker(77, 3, 101)
assert triangle3.is_triangle() == msg_err