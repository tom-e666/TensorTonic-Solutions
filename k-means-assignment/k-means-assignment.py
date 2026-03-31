def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    # Write code here
    import numpy as np
    points = np.array(points)
    centroids = np.array(centroids)

    distances = np.linalg.norm(points[:,None,:] - centroids[None, :, :],axis=2)
    assigment= np.argmin(distances, axis=1)
    return assigment.tolist()
    