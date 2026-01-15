from pxr import Usd, UsdGeom, Gf
import os

# Define a file path name:
file_path = "_assets/Factory_Layout_Base.usda"
# Create a stage at the given `file_path`:
stage: Usd.Stage = Usd.Stage.CreateNew(file_path)

# Define paths to the USD files
box_path = "Box.usdc"
shelf_path = "Shelf.usdc"

# Reference the Box into the scene
box_prim = stage.DefinePrim("/World/Box", "Xform")
box_prim.GetReferences().AddReference(box_path)
processBlenderAsset(box_prim)

# Reference the Shelf into the scene
shelf_prim = stage.DefinePrim("/World/Shelf", "Xform")
shelf_prim.GetReferences().AddReference(shelf_path)
processBlenderAsset(shelf_prim)

# Save the stage
stage.GetRootLayer().Save()

# Export the stage to a string
stage.ExportToString(addSourceFileComment=False)