import math
from unittest import result

def roi_pool(feature_map, rois, output_size):
    """
    Apply ROI Pooling to extract fixed-size features.
    """
    # Write code here
    import numpy as np
    result=[]                                      
    feature_map=np.array(feature_map)
    for roi in rois:
        x1,y1,x2,y2= roi
        roi_h=y2-y1
        roi_w= x2-x1
        roi_map= np.zeros((output_size,output_size))

        for i in range(output_size):
            for j in range(output_size):
                h_start= int(y1 + np.floor((i*roi_h)/output_size))
                h_end= int(y1+ np.floor( (i+1)*roi_h/output_size))
                w_start= int(x1 + np.floor(j*roi_w/output_size))
                w_end= int(x1 + np.floor((j+1)*roi_w/output_size))
                if h_end==h_start:
                    h_end+=1
                if w_end==w_start:
                    w_end+=1
                bin_val=np.max(feature_map[h_start:h_end,w_start:w_end])
                roi_map[i,j]=bin_val
        result.append(roi_map.tolist())
    return result
        
feature_map=  [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
rois= [[0,0,2,2],[1,1,3,3]]
output_size=2
print(roi_pool(feature_map, rois, output_size))
