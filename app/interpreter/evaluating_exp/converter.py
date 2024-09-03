def objToString(obj):
    if obj == None: return "nil"
    
    if isinstance(obj, float):
        text = str(obj)
        if text.endswith(".0"): return text[:len(text) - 2]
        if text.endswith(".00"): return text[:len(text) - 3]
        return text
    
    if isinstance(obj, bool): return str(obj).lower()
    
    return str(obj)