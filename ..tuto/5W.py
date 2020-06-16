def login(userid, userpw):
    id = 'aaa'
    pw = '1234'

    if id == userid and pw == userpw:
        return True
    else:
        return False

id = input("아이디: ")
pw = input("패스워드: ")

if login(id, pw):
    print("로그인 성공")
else:
    print("정보를 확인하세요.")