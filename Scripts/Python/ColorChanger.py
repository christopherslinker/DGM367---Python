import maya.cmds as cmds

def changeColor():
    cmds.colorEditor()
    if cmds.colorEditor(query=True, result=True):
        values=cmds.colorEdiotr(query=True, rgb=True)
    else:
        cmds.warning("Color Editor Closed")
    sels = cmds.ls(selection=True)
    for selection in sels:
        selectionShape = cmds.listRelatives(selection, s=True)
        cmds.setAttr(selectionShape[0] + ".overrideEnabled", True)
        cmds.setAttr(selectionShape[0] + ".overrideRGBColors", True)
        cmds.setAttr(selectionShape[0] + ".overrideColorR", values[0])
        cmds.setAttr(selectionShape[0] + ".overrideColorG", values[1])
        cmds.setAttr(selectionShape[0] + ".overrideColorB", values[2])


changeColor()

