def feature_store_lookup(feature_store, requests, defaults):
    """
    Join offline user features with online request-time features.
    """
    result = []
    for request in requests:
        user = request["user_id"]
        # offline features (dict) or defaults
        offline = feature_store.get(user, defaults)
        # online features (dict) or empty
        online = request.get("online_features", {})
        # merge dicts
        merged = {**offline, **online}
        result.append(merged)
    return result
