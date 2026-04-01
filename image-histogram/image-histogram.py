def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    import numpy as np 
    hist=np.zeros(256)
    image=np.array(image)
    pixels=image.flatten()
    for p in pixels:
        hist[int(p)]+=1
    return hist.tolist()
    
    