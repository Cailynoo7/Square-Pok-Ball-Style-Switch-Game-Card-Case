b=part("lower_core")
s=part("white_shell")
roof=param("upper_sleeve_height",31.3)
pocket_h=param("upper_pocket_height",11.6)
deck=param("upper_deck_thickness",2.4)
seam_offset=b.hinge_z-b.top_z
body=Pos(0,0,seam_offset)*extrude(RectangleRounded(b.carrier,b.carrier,4.3),roof-seam_offset)
hidden_edge=max(s.edge-s.wall-0.3,0.0)
if hidden_edge>0:
    body=fillet(body.edges().group_by(Axis.Z)[-1],hidden_edge)
belt=Pos(0,0,seam_offset)*extrude(RectangleRounded(s.size-2*b.waist_inset,s.size-2*b.waist_inset,s.corner-b.waist_inset),4.0-seam_offset)
body=body+belt
body=body-Pos(0,0,pocket_h+deck)*extrude(RectangleRounded(b.carrier-2*max(2.5,hidden_edge+1.2),b.carrier-2*max(2.5,hidden_edge+1.2),2),roof)
# Straight upper column pockets: front fixed, rear follows shifted lower slots.
column_y_min=-3*b.pitch-b.slot_t/2
column_y_max=max(b.ys)+b.slot_t/2
column_length=column_y_max-column_y_min
for x in b.xs:
    body=body-Pos(x,(column_y_min+column_y_max)/2,pocket_h/2)*Box(b.slot_w,column_length,pocket_h)
print("straight pocket width/length:",b.slot_w,column_length)
# rear hinge relief, then the middle moving knuckle
body=body-Pos(0,31.85,0.5)*Box(56,8.3,6)
body=body+Pos(0,b.hinge_y,0)*Rot(0,90,0)*Cylinder(b.hinge_r,32)
body=body+Pos(0,28.6,3.2)*Box(32,3,4)
body=body-Pos(0,b.hinge_y,0)*Rot(0,90,0)*Cylinder(b.bore/2,34)
# clear the stationary front bezel through the whole opening path
body=body-Pos(0,-32.2,0)*Rot(90,0,0)*Cylinder(s.notch_r,6.2)
# latch keeper supported from the inner front bridge
body=body-Pos(0,-27.8,1.4)*Box(12.8,3.2,3.0)
keeper=Pos(0,-29.7,1.2)*Box(14.8,1.4,1.6)
side1=Pos(-7.0,-27.3,2.4)*Box(1.6,6.0,4.4)
side2=Pos(7.0,-27.3,2.4)*Box(1.6,6.0,4.4)
body=body+keeper+side1+side2
body=body-Pos(0,-27.2,3.9)*Box(12,6.6,3.5)
body=body-Pos(0,-26.1,2.95)*Box(12,5.4,5.7)
body.color=srgb("#17191c")
assert len(body.solids())==1
publish("upper",body,"黑色上内胆",material="petg")
