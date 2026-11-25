width=param("latch_width",10.0)
thick=param("latch_thickness",1.2)
root_z=param("latch_root_z",11.2)
hook_z=param("latch_hook_z",36.3)
leaf_y=param("leaf_y",-27.8)
hook_reach=param("hook_reach",2.0)
leaf=Pos(0,leaf_y,(root_z+hook_z)/2)*Box(width,thick,hook_z-root_z)
# sloping top cams the leaf inward during closing
profile=Plane.YZ*Polygon((leaf_y-thick/2-hook_reach,hook_z),(leaf_y+thick/2,hook_z),(leaf_y+thick/2,hook_z+1.7),(leaf_y-thick/2-0.9,hook_z+1.7),(leaf_y-thick/2-hook_reach,hook_z+0.6),align=None)
hook=Pos(-width/2,0,0)*extrude(profile,amount=width)
leaf=leaf+hook
leaf.color=srgb("#17191c")
assert len(leaf.solids())==1
publish("latch",leaf,"黑色弹性锁舌",material="petg")