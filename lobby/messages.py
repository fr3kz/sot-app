#static messages for notifications

def rep_plus(user):
    return " {0} rep plus u ".format(user.profile.name)
    
def rep_down(user):
    return " {0} rep  u ".format(user.profile.name)

def send_invite_to_friends(profile):
    return "{0} send you invite".format(profile.name)

def accept_invite_to_friends(profile):
    return "{0} accept yours inivtation to friedns".format(profile.name)

def reject_invite_to_friends(profile):
    return "{0} reject yours inivtation to friedns".format(profile.name)