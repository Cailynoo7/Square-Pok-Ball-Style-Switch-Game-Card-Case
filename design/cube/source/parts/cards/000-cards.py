b=part("lower_core")
width=param("card_envelope_width",21.2)
thick=param("card_envelope_thickness",3.3)
height=param("card_envelope_height",31.2)
cards=[Pos(x,y,b.floor_z+height/2)*Box(width,thick,height) for x in b.xs for y in b.ys]
for c in cards: c.color=srgb("#52565a")
publish("cards",cards,"14张游戏卡包络",role="reference")