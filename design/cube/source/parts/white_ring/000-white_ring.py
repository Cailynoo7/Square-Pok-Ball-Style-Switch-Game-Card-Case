b=part("lower_core")
s=part("white_shell")
outer_d=param("white_ring_outer_diameter",23.0)
thickness=param("white_ring_thickness",1.2)
edge=param("white_ring_edge_radius",0.2)
inner_r=b.button_hole_r
front_y=-s.size/2
# attach_panel_v1(method="glue_pad") rejected this exact interface:
# contact is too narrow for a hidden feature. Free implementation:
# flat annular adhesive joint onto the stationary lower black bezel.
ring=Pos(0,front_y+thickness/2,34)*Rot(90,0,0)*(Cylinder(outer_d/2,thickness)-Cylinder(inner_r,thickness+1))
ring=fillet(ring.edges().group_by(Axis.Y)[0],edge)
ring.color=srgb("#f0eee8")
assert len(ring.solids())==1
assert outer_d/2 > inner_r+1.2
publish("white_ring",ring,"白色按钮环",material="pla")
