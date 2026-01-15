from pxr import Usd, UsdGeom, UsdPhysics, Sdf

usd_context = omni.usd.get_context()
stage = usd_context.get_stage()
selection = usd_context.get_selection()
selected = [Sdf.Path(p) for p in selection.get_selected_prim_paths()][0]
print(selected)

default_prim: Usd.Prim = stage.GetDefaultPrim()
primvars_api = UsdGeom.PrimvarsAPI(default_prim)
accent_color = primvars_api.CreatePrimvar("accentColor", Sdf.ValueTypeNames.Float3, UsdGeom.Tokens.constant)
accent_color.Set((1.0, 0.0, 0.0))
