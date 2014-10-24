
def is_triangle(s1, s2, s3):
    tri = True
    
    if(s1 > s2 + s3 or s2 > s1 + s3 or s3 > s1 + s2):
        tri = False
    else:
        tri = True
    
    if(tri):
        print "Yes, it's a triangle"
    else:
        print "No, it's not a triangle"
        
def prompt_user():
    l1 = raw_input("Enter length of first stick: ")
    l2 = raw_input("Enter length of second stick: ")
    l3 = raw_input("Enter length of third stick: ")
    
    is_triangle(int(l1), int(l2), int(l3))
    
prompt_user()