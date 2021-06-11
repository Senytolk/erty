def check_passwd(username, password, min_length=8, check_username=True):
    if len(password) < min_length:
        return False
    elif check_username and username in password:
        return False
    else:
        return True


def test_check_passwd():
    assert check_passwd('user', '12345678') == True, 'для пользователя user ошибка пароля'
    assert check_passwd('user', '12345678', min_length=10) == False
    assert check_passwd('user', '12345678user', min_length=10) == False

print('jklp')
print('jy')