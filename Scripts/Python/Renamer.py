import maya.cmds as cmds

def renameTool():
    selectionInput = input()
    selection = cmds.ls(sl=True)
    count = selectionInput.count('#')
    selectionPartition = selectionInput.partition(count * "#")
    if len(selection) <= 0:
        print("You Suck")
    else:
        for i in range(len(selection)):
            new_name = selectionPartition[0] + str(i+1).zfill(count) + selectionPartition[2]
            cmds.rename(selection[i],new_name)

renameTool()
