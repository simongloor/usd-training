import carb
from pxr import Usd, UsdGeom, UsdShade

stage = omni.usd.get_context().get_stage()
material_prim = UsdShade.Material.Define(stage, "/Metal")
material_prim.GetPrim().GetReferences().AddReference("./Ref.usd", "/Looks/Metal")



