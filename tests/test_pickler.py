import io
import cloudpickle_fast._pickle as _pickle
import cloudpickle_fast as cloudpickle
import pickletools

# bio = io.BytesIO()
# p = _pickle.Pickler(bio)


# def callback(pickler, obj):
#     if obj.__name__ == "g":
#         return int, (5,)
#     else:
#         return NotImplementedError

# p.global_hook = callback


def g():
    pass

def h():
    pass

g.h = h
h.g = g

picklestring = cloudpickle.dumps(g)

print('save success')
print(cloudpickle._pickle.loads(picklestring))
