from pxr import Usd, UsdGeom, UsdShade

asset_stage = omni.usd.get_context().get_stage()

class_prim = asset_stage.CreateClassPrim("/_street_lamp_dbl")
root = asset_stage.GetDefaultPrim()
root.GetInherits().AddInherit(class_prim.GetPath())

