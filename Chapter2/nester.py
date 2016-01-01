"""This scode prints on the shell the items of the list,
if there is nested item"""

def print_lol(the_list):
    for item in the_list:
        if isinstance(item, list):
            print_lol(item)
        else:
            print(item)
            
print_lol(movies)
