set breakpoint pending on
dir ~/repos/cloudpickle_fast
break cloudpickle_fast/_pickle.c:6255

break cloudpickle_fast/_pickle.c:3972

run -m pdb tests/test_pickler.py

