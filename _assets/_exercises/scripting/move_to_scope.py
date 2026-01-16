def move_into_scope(scope_name: str):
	import omni.usd
	import omni.kit.undo
	import omni.kit.commands
	from pxr import Usd, UsdGeom, UsdPhysics, Sdf

	usd_context = omni.usd.get_context()
	stage = usd_context.get_stage()
	selection = usd_context.get_selection()
	selected = [Sdf.Path(p) for p in selection.get_selected_prim_paths()]
	
	if selected:
		with omni.kit.undo.group():
			# Create the scope next to the selected prims (same parent as the first selected prim)
			target_parent = selected[0].GetParentPath()
			
			# Create a new scope
			scope_path = get_unique_child_path(target_parent, scope_name)
			UsdGeom.Scope.Define(stage, scope_path)
			
			omni.kit.commands.execute(
					"CreatePrim",
					prim_path=scope_path,
					prim_type="Scope",
					select_new_prim=False,
			)
			
			# Move ALL selected prims into that scope
			ns = Usd.NamespaceEditor(stage)
			
			for old_path in selected:
				prim = stage.GetPrimAtPath(old_path)
				if not prim.IsValid():
					continue
			
				new_path = scope_path.AppendChild(prim.GetName())
			
				omni.kit.commands.execute(
					"MovePrim",
					path_from=str(old_path),
					path_to=new_path,
				)
		
		# Select Scope
		selection.clear_selected_prim_paths()
		selection.set_selected_prim_paths([str(scope_path)], True)

move_into_scope("Colliders")








