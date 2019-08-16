

# https://tools.ietf.org/id/draft-struik-lwip-curve-representations-00.html

# Montgomery Curve    B*v^2 = u^3  + A*u^2   +  u          ---  M{A,B}

# ShortWeiestrass Curve    y^2   = x^3   +   a*x  + b      ---- W{a,b)

# Mapping from Montgomery to  ShortWeiestrass form 


#  W{a,b} =


#     a   =  (3 - A^2) /  (3B^2) 


#     b   =  (2A^3 - 9A) / ( 27B^3)


#     {x,y}  = { (u/B  +  A/3B),  v/B)


#     {u,v}  = { x - A/3,  y)
