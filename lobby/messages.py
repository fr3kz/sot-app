#static messages for notifications

def rep_plus(user):
    return " {0} dodał ci reputacje! ".format(user.profile.name)
    
def rep_down(user):
    return " {0} odjął ci reputacje! ".format(user.profile.name)

def send_invite_to_friends(profile):
    return "{0} wysłał ci zaproszenie".format(profile.name)

def accept_invite_to_friends(profile):
    return "{0} Zakakceptował twoje zaproszenie do znajomych".format(profile.name)

def reject_invite_to_friends(profile):
    return "{0} Odrzucił twoje zaproszenie do znajomych".format(profile.name)