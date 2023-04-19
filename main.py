from kakaoautomsgsender_master.kaka_class import KakaoTalk


from gwangju_menu_class import menudownload

# 외부파일에서 아이디 비번 가지고 오기 
with open('login.txt', 'r') as f:
    credentials = f.read().split(',')
    id = credentials[0]
    password = credentials[1]
with open('login_kakao.txt', 'r') as f:
            credentials = f.read().split(',')
            kakao_id = credentials[0]
            kakao_password = credentials[1]
kakao_login = menudownload(id, password)
kakao_login.login()

# kakao 
kakao = KakaoTalk(kakao_id, kakao_password)
kakao.open_folder()
kakao.open_kakao()
kakao.open_chatroom('동생')
# kakao.open_person('동생')
# 추후 드래그 주석 풀어야함
kakao.drag()


