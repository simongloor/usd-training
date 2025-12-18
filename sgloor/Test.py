from pxr import Usd
import os

# Define a file path name:
file_path = "_assets/test.usda"
# Create a stage at the given `file_path`:
stage: Usd.Stage = Usd.Stage.CreateNew(file_path)

# Define paths to the USD files
box_path = "Box.usdc"
shelf_path = "Shelf.usdc"

# Reference the Box into the scene
box_prim = stage.DefinePrim("/World/Box", "Xform")
box_prim.GetReferences().AddReference(box_path)

# Rotate the Box 90 degrees around the X axis
box_prim.AddRotateXOp().Set(-90)

# Reference the Shelf into the scene
shelf_prim = stage.DefinePrim("/World/Shelf", "Xform")
shelf_prim.GetReferences().AddReference(shelf_path)
shelf_prim.AddRotateXOp().Set(-90)

# # Add a sphere at the origin
# stage.DefinePrim("/World/Sphere", "Sphere")

# Save the stage
stage.GetRootLayer().Save()

# Export the stage to a string
stage.ExportToString(addSourceFileComment=False)