def my_functions_with_args (username, greeting):
    print ("Hello, %s, From my  function!, I wish you %s" %(username, greeting))

my_functions_with_args("Vitya", "Happy holidays")

def sum_two_numbers(a, b):
    return a + b
sum_two_numbers(4,5)

###########################

def list_benefist ():
    return "More organized code",\
           "More readable code",\
           "Easier code reuse",\
           "Allowing programmers to share and connect code together"

def build_sentence (info):
    return "%s is a benefit of functions!" %info

def name_of_the_benefits_of_functions():
    list_of_benefits = list_benefist()
    for info in list_of_benefits:
        print (build_sentence(info))

name_of_the_benefits_of_functions()
