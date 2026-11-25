radius=param("button_radius",10.0)
cap_t=param("button_cap_thickness",1.6)
stem_r=param("button_stem_radius",1.6)
flange_r=param("button_flange_radius",11.0)
stroke=param("release_stroke",1.8)
cap=Pos(0,-33.4-cap_t/2,34)*Rot(90,0,0)*Cylinder(radius,cap_t)
cap=fillet(cap.edges().filter_by(GeomType.CIRCLE),0.35)
stem=Pos(0,-31.0,31)*Rot(90,0,0)*Cylinder(stem_r,4.9)
flange=Pos(0,-30.9,34)*Rot(90,0,0)*Cylinder(flange_r,0.8)
flange=flange-Pos(0,-30.9,44)*Box(30,4,22)
button=cap+stem+flange
button.color=srgb("#969a9e")
assert len(button.solids())==1
publish("button",button,"灰色释放按钮",material="petg")
