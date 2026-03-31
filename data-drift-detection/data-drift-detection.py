def detect_drift(reference_counts, production_counts, threshold):
    """
    Compare reference and production distributions to detect data drift.
    """
    # Write code here
    import numpy as np
    reference_counts/=np.sum(reference_counts)
    production_counts/=np.sum(production_counts)
    tvd=1/2*np.sum(np.abs(reference_counts-production_counts))
    return {
        "score":tvd,
        "drift_detected": bool(tvd>threshold)
    }
    