from typing import List, Dict

def fun(L:List[int]) -> Dict[int,List]:
    M= list(dict.fromkeys(L)) # we remove the duplicates from list L
    M.sort() # we sort me list M and now we have the unique elements of L, in M sorted
    K  = []
   
    for x in M: # we run all the elements one by one in list M
        K.append([index for (index, item1) in enumerate(L) if item1 == x]) # we find and add in list K all the positions of the unique elements of list M.

    zipped = zip(M,K) # with zip order we manage to create a 1:1 ratio in M and K elemets
    dict.update(zipped) 
    return dict
    
dict = {}
L:list[int] = [1,2,3,2,3,1,]
print(fun(L))
