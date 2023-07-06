def secure_name(name) :
    new_name=name[0:1]+("*"*len(name[1:]))
    return new_name

def secure_no(no):
    star=len(no[8::1])
    new_no = no[0:8]+(star*"*")
    return new_no

def secure_phone(phone):
    star=len(phone[4:8])
    new_phone=phone[0:4]+star*"*"+phone[8::1]
    return new_phone

