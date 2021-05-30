def remove_unavailable(hierarchy: str) -> str:

    # build a new string with the result
    hierarchy_fixed = ''


    # value to count the 'level' of the tree we're on. increment on each open bracket and decrement on each closed bracket
    # "Unavailable" will have an open bracket on level x and its subtree will close on level x-1"
    bracket_cnt = 0


    # parse through the string once
    i = 0
    while i < len(hierarchy):

        # copy the character
        hierarchy_fixed += hierarchy[i]


        if hierarchy[i] == '(':
            bracket_cnt += 1

            # check if the subtree is Unavailable. if it is, then just ignore everything until its subtree is finished
            # (when Unavailable's tree closes when the bracket count gets to one less than the value when it opened)
            if hierarchy[i+1:i+14] == '"Unavailable"':
                opened = bracket_cnt
                ii = i
                while bracket_cnt > opened - 1:
                    ii += 1
                    if hierarchy[ii] == '(':
                        bracket_cnt += 1
                    elif hierarchy[ii] == ')':
                        bracket_cnt -= 1

                # delete extra closed bracket and ", " that were added before
                hierarchy_fixed = hierarchy_fixed[:len(hierarchy_fixed) - 3]

                i = ii
        

        if hierarchy[i] == ')':
            bracket_cnt -= 1
        
        i += 1

    return(hierarchy_fixed)



if __name__ == "__main__":
    hierarchy1 = '("John", ("Jasmine", ("Jay"), ("Unavailable")), ("Unavailable", ("Jack", ("Jeremy"))), ("Johanna"))'
    hierarchy2 = '("John", ("Jasmine", ("Jay"), ("Jackson")), ("Jimmer", ("Jack", ("Jeremy"))), ("Johanna"))'
    hierarchy3 = '("John", ("Unavailable", ("Jay"), ("Jackson")), ("Jimmer", ("Jack", ("Jeremy"))), ("Johanna"))'
    hierarchy4 = '("John", ("Unavailable", ("Jay"), ("Jackson")), ("Jimmer", ("Unavailable", ("Jeremy"))), ("Johanna"))'

    print('1: ', remove_unavailable(hierarchy1))
    print('2: ', remove_unavailable(hierarchy2))
    print('3: ', remove_unavailable(hierarchy3))
    print('4: ', remove_unavailable(hierarchy4))