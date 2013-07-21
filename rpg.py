def get_yes_no(question):
    print question
    
    answer = raw_input()
    
    if answer.upper() == 'Y' or answer.upper() == "YES":
        return True
    elif answer.upper() == 'N' or answer.upper() == "NO":
        return False
    else:
        print "Please enter either 'Y(es)' or 'N(o)'"
        return get_yes_no(question)

def get_positive_whole_number_from_user(question):
    print question
    
    answer = raw_input()
    
    if answer.isdigit():
        return int(answer)
    else:
        print "Please enter a positive, whole number"
        return get_positive_whole_number_from_user(question)
