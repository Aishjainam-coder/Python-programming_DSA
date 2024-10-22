def vowel(n):
    v="aeiou"
    count=0
    
    
    for char in n :
        
        if char in v:
            
         count = count+1
    return count
print(vowel('aishwarya'))
        
