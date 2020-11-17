from user_data import User
from user_data_exceptions import UsernameAlreadyExist, InvalidEmail, UnderAge, NotPositiveInteger


class UserData(object):

    user_tuple_data = [
        ("ANDREW", "andrew@yahoo.com", 25)
        ("MATT", "matt@yahoo.com", 20)
        ("CJAY", "cjay@yahoo.com", 190)
        ("MINNIE", "mini@yahoo.com", 16)
        ("MICKEY", "mickey@yahoo.com", 19)
        ("MAJO", "majo@gmail.com", 14)
        ("MAYA", "maya!gmail.com", 10)
        ("ANDREAS", "andreas@gmail.com", 18)
        ("MIKA", "mika@yahoo.com", 17)
        ("ANDREW", "andrew@gmail.com", 127)
    ]
