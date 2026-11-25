s=part("white_shell")
carrier=param("carrier_width",62.6)
floor_z=param("slot_floor_z",14.0)
slot_w=param("slot_width",21.8)
slot_t=param("slot_thickness",3.8)
pitch=param("slot_pitch",6.4)
column=param("column_offset",13.0)
top_z=param("base_top_z",33.8)
band_z=param("band_bottom_z",30.0)
hinge_y=param("hinge_y",31.0)
hinge_z=param("hinge_z",34.0)
hinge_r=param("hinge_radius",3.0)
bore=param("hinge_bore",2.15)
bezel_r=param("bezel_radius",12.5)
button_hole_r=param("button_hole_radius",10.3)
waist_inset=param("black_band_inset",0.8)
body=Pos(0,0,2.7)*extrude(RectangleRounded(carrier,carrier,4.3),top_z-2.7)
hidden_edge=max(s.edge-s.wall-0.3,0.0)
if hidden_edge>0:
    body=fillet(body.edges().group_by(Axis.Z)[0],hidden_edge)
belt=Pos(0,0,band_z)*extrude(RectangleRounded(s.size-2*waist_inset,s.size-2*waist_inset,s.corner-waist_inset),top_z-band_z)
body=body+belt
body=body-Pos(0,0,2.6)*extrude(RectangleRounded(carrier-2*max(2.5,hidden_edge+1.2),carrier-2*max(2.5,hidden_edge+1.2),2),9.0)
xs=[-column,column]
slot_shift=param("slots_rearward_shift",1.5)
ys=[(i-3)*pitch+slot_shift for i in range(7)]
for x in xs:
    for y in ys:
        body=body-Pos(x,y,(floor_z+34.5)/2)*Box(slot_w,slot_t,34.5-floor_z)
# leave the elastic latch and button a clear central front bay
body=body-Pos(0,-28.5,24.5)*Box(12.0,7.0,31.0)
# recess rear edge around the hinge swing
body=body-Pos(0,31.85,33.5)*Box(70,8.3,7)
for x in [-22,22]:
    lug=Pos(x,hinge_y,hinge_z)*Rot(0,90,0)*Cylinder(hinge_r,9.5)
    web=Pos(x,28.6,30.8)*Box(9.5,3.0,4.0)
    body=body+lug+web
    body=body-Pos(x,hinge_y,hinge_z)*Rot(0,90,0)*Cylinder(bore/2,11)
# Front bezel is coplanar with the recessed black band.
bezel_depth=param("bezel_depth",2.3)
ring_seat_depth=param("white_ring_seat_depth",0.4)
ring_seat_radius=param("white_ring_seat_radius",11.7)
bezel_front_y=-s.size/2+waist_inset
bezel_y=bezel_front_y+bezel_depth/2
bezel=Pos(0,bezel_y,34)*Rot(90,0,0)*Cylinder(bezel_r,bezel_depth)
bezel=bezel-Pos(0,bezel_y,34)*Rot(90,0,0)*Cylinder(button_hole_r,bezel_depth+2)
body=body+bezel
body=body-Pos(0,-33,34)*Rot(90,0,0)*Cylinder(button_hole_r,8)
# full flange clearance behind bezel
body=body-Pos(0,-29.7,34)*Rot(90,0,0)*Cylinder(11.3,3.6)
# Shallow annular registration pocket keeps the 1.2 mm white ring flush.
body=body-Pos(0,bezel_front_y+ring_seat_depth/2-0.05,34)*Rot(90,0,0)*Cylinder(ring_seat_radius,ring_seat_depth+0.1)
# adhesive root socket for removable latch
body=body+Pos(0,-28,12.5)*Box(14,5,3)
body=body-Pos(0,-27.8,12.5)*Box(10.4,1.6,3.4)
body.color=srgb("#17191c")
assert len(body.solids())==1
print("slots",len(xs)*len(ys),"pitch",pitch,"lower_depth",34-floor_z,"red_white_height",s.height)
publish("lower",body,"黑色下内胆",material="petg")
