def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here
    step= chunk_size-overlap
    chunks=[]
    idx=0
    if not tokens:
        return []
    
    chunks.append(tokens[idx:idx+chunk_size])
    idx+=step
    while idx + chunk_size -1 < len(tokens):
        chunks.append(tokens[idx:idx+chunk_size])
        idx+=step
        
            
        
    return chunks