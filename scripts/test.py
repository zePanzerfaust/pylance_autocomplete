import mylib
from mylib import submodule1, submodule2

print(submodule1.app1_dummy.get_app1_dummy_1())  # suggested and works when run with python
#print(submodule1.app1_1.app1_1_dummy.get_some_value_app1_1())  # suggested but doesn't work when run with python

print(submodule2.get_some_other_value_sub1_1())  # suggested and works with python (submodule2.sub1_1.get_some_other_value_sub1_1())

print(mylib.submodule2.sub1_1.get_some_value_sub1_1())  # not suggested but works with python
print(submodule2.sub1_1.get_some_value_sub1_1())  # not suggested but works with python
