lst=[12321]
lst_cpy=lst
if lst == lst_cpy[::-1]:
    print("The list contains a palindrome.")
else:
    print("The list does not contain a palindrome.")


    #[:] is a slicing operation that means "take the entire list or sequence
#[::-1] means "take the entire sequence, but step backwards one element at a time."The -1 specifies the step size, and when used in the slice operation, it means to traverse the sequence from the end to the beginning, effectively reversing the sequence""".