import omni.usd
from pxr import Usd, UsdPhysics

usd_context = omni.usd.get_context()
stage = usd_context.get_stage()
selection = usd_context.get_selection()

prim_paths = selection.get_selected_prim_paths()

for path in prim_paths:
    prim = stage.GetPrimAtPath(path)
    if not prim or not prim.IsValid():
        continue

    # Apply a collider
    UsdPhysics.CollisionAPI.Apply(prim)
    physx_collision = UsdPhysics.MeshCollisionAPI.Apply(prim)
    physx_collision.CreateApproximationAttr("convexHull")
    print(f"Added convex hull collider to {path}")





