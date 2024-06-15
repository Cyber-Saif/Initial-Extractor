#6th December 2021
def initials_extractor(string):
    result = ' '
    result+=string[0]    
    for letters in range(len(string)):
        if string[letters] == ' ':
            result+=string[letters+1]
            result = result.upper()
            
    return result


def split_s(string):
    split = []
    empty = ''
    for words in string:
        if words == ' ':
            split.append(empty)
            empty = ''
            
        else:
            empty+=words
    if True:
        split.append(empty)
    return split

#main function contains both of the functions split_s and initials_extractor
def main():
    initial = input('Pleasae type your name: ')
    
    if initial == "":
        print('! Can not get initials of an empty string !')
        
    else:
        inti = initials_extractor(initial)
        print(inti)
        print(f'* Welcome to the program {inti}' )
    
    split = input('\nType a sentance: ')
    
    if split == "":
        print('! python was unable to read your sentence ! \ntry again')
    
    else:
        split_func = split_s(split)
        print(split_func)

main()












