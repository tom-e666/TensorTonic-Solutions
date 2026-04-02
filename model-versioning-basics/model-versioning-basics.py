def promote_model(models):
    """
    Decide which model version to promote to production.
    """
    def comparator(ma,mb):
        if ma["accuracy"]!=mb["accuracy"]:
            return ma["accuracy"]<mb["accuracy"]
        if ma["latency"]!=mb["latency"]:
            return ma["latency"]<mb["latency"]
        return ma["timestamp"]<mb["timestamp"]
    
    # from functools import cmp_to_key
    # models.sort(key=cmp_to_key(comparator))
    return max(models,
              key=lambda m:(
                  m["accuracy"],
                  -m["latency"],
                  m["timestamp"]
              ))["name"]
    
    