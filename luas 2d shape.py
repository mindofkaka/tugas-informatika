shape = input('Choose one of 2D-Shape to count the area (circle, triangle, rectangle) : ' )

if shape == 'Circle' or 'circle' :
    r = int(input('Input the radius : ' ))
    ans = 22*r/7
    print(ans)
elif shape == 'Triangle' or 'triangle' :
    base = int(input('Input the base : ' ))
    height = int(input('Input the height : ' ))
    ans = base*height/2
    print(ans)
elif shape == 'Rectangle' or 'rectangle' :
    width = int(input('Input the width : ' ))
    length = int(input('Input the length : ' ))
    ans = width*length
    print(ans)
