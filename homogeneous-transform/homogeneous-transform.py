import numpy as np

def apply_homogeneous_transform(T, points):
    """
    Apply 4x4 homogeneous transform T to 3D point(s).
    """
    # Your code here
    points=np.array(points)
    res=[]
    converted=False
    if points.ndim==1:
        points=points[None,:] #(1,3)
        converted=True
    ones = np.ones((points.shape[0],1))   
    points_h = np.hstack((points,ones)) #(N,4) 
    transforms = (T @ points_h.T).T
    
    transformed = transforms[:,:3]
    if converted:
        return transformed[0]
    return transformed
T=[[1,0,0,1],[0,1,0,2],[0,0,1,3],[0,0,0,1]] 
points=[1,2,3]
print(apply_homogeneous_transform(T, points))
        