import omni.usd
from pxr import Usd

print("hello world")

usd_context = omni.usd.get_context()
stage = usd_context.get_stage()
selection = usd_context.get_selection()

prim_paths = selection.get_selected_prim_paths()

for path in prim_paths:
    prim = stage.GetPrimAtPath(path)
    if prim:
        print(path, prim.GetTypeName())
