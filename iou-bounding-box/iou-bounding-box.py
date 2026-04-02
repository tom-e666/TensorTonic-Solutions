def iou(box_a, box_b):
    x_l=max(box_a[0],box_b[0])
    y_l=max(box_a[1],box_b[1])
    x_r=min(box_a[2],box_b[2])
    y_r=min(box_a[3],box_b[3])
    width=max(0,x_r-x_l)
    height=max(0,y_r-y_l)
    intersection=width*height
    a= (box_a[2]-box_a[0])*(box_a[3]-box_a[1])
    b= (box_b[2]-box_b[0])*(box_b[3]-box_b[1])
    return (intersection)/(a+b-intersection)
    
    
    
    
    
    