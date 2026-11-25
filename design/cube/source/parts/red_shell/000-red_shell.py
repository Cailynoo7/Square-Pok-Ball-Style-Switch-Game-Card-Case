base=part("white_shell")
wall=base.wall
cap_h=param("red_height",30.0)
outer=extrude(RectangleRounded(base.size,base.size,base.corner),cap_h)
outer=fillet(outer.edges().group_by(Axis.Z)[-1],base.edge)
outer=fillet(outer.edges().group_by(Axis.Z)[0],0.6)
inner=Pos(0,0,-wall)*extrude(RectangleRounded(base.size-2*wall,base.size-2*wall,base.corner-wall),cap_h)
if base.edge > wall:
    inner=fillet(inner.edges().group_by(Axis.Z)[-1],base.edge-wall)
shell=outer-inner
shell=shell-Pos(0,-33,-4)*Rot(90,0,0)*Cylinder(base.notch_r,9)
shell.color=srgb("#ed202c")
publish("red",shell,"红色上外壳",material="pla")
