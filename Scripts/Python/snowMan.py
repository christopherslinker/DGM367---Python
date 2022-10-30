import maya.cmds as cmds

cmds.polySphere(r = 1)
cmds.polySphere(r = .75)
cmds.move(0, 1.5, 0)
cmds.polySphere(r = .5)
cmds.move(0, 2.5, 0)

cmds.select(all=True)
cmds.polyUnite()

cmds.DeleteHistory()
cmds.rename("snowman_body_geo")

cmds.polyCylinder(r = .07)
cmds.scale(1,0.25,1)
cmds.move(0,2.5,0.5)
cmds.rotate(90.0,0)

cmds.rename("nose_geo")
cmds.select('nose_geo.f[21]')
cmds.scale(0.25,0.25,0.25)
cmds.move(0,2.5,1)

cmds.polySphere(r=0.05)
cmds.scale(1, .25, 1)
cmds.move(-0.067, 2.572, 0.489)
cmds.rotate(90, 0, 0)
cmds.rename("right_eye_geo")

cmds.polySphere(r=0.05)
cmds.scale(1, .25, 1)
cmds.move(0.067, 2.572, 0.489)
cmds.rotate(90, 0, 0)
cmds.rename("left_eye_geo")

cmds.select('left_eye_geo', 'right_eye_geo')
cmds.group()
cmds.rename("eye_grp")

cmds.select(all=True)
cmds.group(name="snowman_geo_grp")