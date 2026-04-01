def deduplicate(records, key_columns, strategy):
    result ={}
    for record in records:
        key = tuple(record[col] for col in key_columns)
        if key not in result:
            result[key]=record
        else:
            if strategy=="last":
                result[key]=record
            if strategy=="most_complete":
                old_record=result[key]
                old_quality= sum(v is not None for v in old_record.values())
                new_quality= sum(v is not None for v in record.values())
                if new_quality > old_quality:
                    result[key]= record
    return list(result.values())
                    
        
                
            
            