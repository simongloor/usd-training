import omni.kit.commands

cmds = omni.kit.commands.get_commands()

print(f"{len(cmds)} commands registered:\n")
for name in sorted(cmds.keys()):
    print(name)

