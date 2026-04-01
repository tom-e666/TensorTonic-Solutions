def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    # Write code here
    import numpy as np
    points= np.array(points)
    assignments=np.array(assignments)
    centroids=[]
    for i in range(k):
        cluster= points[assignments==i]
        if len(cluster)>0:
            centroids.append(np.mean(cluster, axis = 0))
        else:
            centroids.append(np.zeros(points.shape[1]))
    return np.array(centroids).tolist()
    
    
    