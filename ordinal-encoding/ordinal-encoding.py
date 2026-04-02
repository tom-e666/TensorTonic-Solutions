def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """
    # Write code here
    import numpy as np
    mapping={type:idx for idx,type in enumerate(ordering)}
    return [mapping[v] for v in values]