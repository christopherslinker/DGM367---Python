import maya.cmds as cmds


def duplicateRename():
    sels = cmds.ls(selection=True)

    cmds.duplicate()
    cmds.rename(input())


duplicateRename()