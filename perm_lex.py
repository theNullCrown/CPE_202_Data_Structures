# Name: allie blaising

def perm_gen_lex(a): 
    if len(a) == 0: # condition if there is only one item, return empty list 
        return []
    if len(a) == 1: 
        return [a] # base case 
    final_list = []
    for i in a:  # loop through every char in a word 
        for perm in perm_gen_lex(a.replace(i, '', 1)): # generate permutations of the simpler string recursively
            final_list.append(i + perm)  # add the removed character to the front of each permutation of the simpler word, and add the resulting permutation to a list
    return final_list 





 