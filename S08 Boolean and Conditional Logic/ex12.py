# NO TOUCHING ======================================

from random import choice, randint

# randomly assigns values to these four variables
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)

# NO TOUCHING ======================================


calling_in_sick = None  # set this to True or False with Boolean Logic and Conditionals!

# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

def am_i_calling_in_sick(actually_sick, kinda_sick, hate_your_job, sick_days):

    rval = False
    if (actually_sick and sick_days):
        rval = True
    if (kinda_sick and hate_your_job and sick_days):
        rval = True

    iam = "I"
    plural = False
    if(actually_sick):
        if(plural):
            iam += " and"
        iam += " am actually sick"
        plural = True
    else:
        if(kinda_sick):
            if(plural):
                iam += " and"
            iam += " am kinda sick"
            plural = True
        
    if(hate_your_job):
        if(plural):
            iam += " and"
        iam += " hate my job"
        plural = True

    if(sick_days):
        if(plural):
            iam += " and"
        iam += " have sick days"
        plural = True
    else:
        if(plural):
            iam += " and"
        iam += " am out of sick days"
        plural = True

    if(plural):
        iam += " and"
    if(rval):
        iam += " am calling in sick"
    else:
        iam += " am not calling in sick"

    print(iam)

    return rval

    
if __name__ == "__main__":
    am_i_calling_in_sick(actually_sick, kinda_sick, hate_your_job, sick_days)
        
        

# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

