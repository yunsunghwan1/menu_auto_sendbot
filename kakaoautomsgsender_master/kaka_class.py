import pyautogui
import time
import pyperclip
import os

class KakaoTalk:
    def __init__(self, id, password):
        self.img_path = os.path.dirname(os.path.realpath(__file__)) + '/kaka_img/'
        self.id = id
        self.password = password
        self.conf = 0.8
        self.time_run = 0.3
        self.kill_kakao()
    def kill_kakao(self):
        os.system("TASKKILL /F /IM KakaoTalk.exe")  # this will kill KakaoTalk    
    
    def open_folder(self):
        folder_path = r"C:\Users\admin\Desktop\peronal\crawling"
        os.startfile(folder_path)
        time.sleep(1.0)
        pyautogui.hotkey('winright', 'right')
        time.sleep(1.0)
        
    def open_kakao(self):
        try:
            # 카카오톡오픈 
            location = pyautogui.locateCenterOnScreen(self.img_path+'kakao.png',confidence = self.conf)
            if location == None:
                location = pyautogui.locateCenterOnScreen(self.img_path+'kakao4.png',confidence = self.conf)
            pyautogui.click(location)
            time.sleep(10)
            # 비밀번호 입력하는 칸 클릭 후 초기화(내용이 있으면 삭제)
            location = pyautogui.locateCenterOnScreen(self.img_path+'kakao_lock.png',confidence = self.conf)
            pyautogui.doubleClick(location)
            pyautogui.hotkey('backspace')
            # 비번 복사 붙여넣기
            pyperclip.copy(self.password)
            time.sleep(self.time_run)
            pyautogui.hotkey('ctrl', 'v')
            
            # 확인
            location = pyautogui.locateCenterOnScreen(self.img_path+'log_in_confirm.png',confidence = 0.8)
            pyautogui.click(location)
        except:
            pass     
    def open_person(self, kakao_search):
        location = pyautogui.locateCenterOnScreen(self.img_path+'person_icon.png',confidence = self.conf)
        if location == None:
            location = pyautogui.locateCenterOnScreen(self.img_path+'person_icon2.png',confidence = self.conf)
        pyautogui.click(location)
    # 2초 대기 
        time.sleep(1.0)
        pyautogui.hotkey('winleft', 'left')

        location = pyautogui.locateCenterOnScreen(self.img_path+'search_icon.png',confidence = self.conf)
        pyautogui.click(location)

        # 2초 대기 
        time.sleep(self.time_run)
        pyperclip.copy(kakao_search)
        # 붙여넣기
        time.sleep(self.time_run)
        pyautogui.hotkey('ctrl', 'v')
        # 엔터
        time.sleep(self.time_run)
        pyautogui.press('enter')

        time.sleep(2)
        pyautogui.hotkey('winleft', 'left')
        time.sleep(self.time_run)
        
    def open_chatroom(self, kakao_search):
        location = pyautogui.locateCenterOnScreen(self.img_path+'chat_room.png',confidence = self.conf)
        pyautogui.click(location)
    # 2초 대기 
        time.sleep(1.0)
        pyautogui.hotkey('winleft', 'left')

        location = pyautogui.locateCenterOnScreen(self.img_path+'search_icon.png',confidence = self.conf)
        pyautogui.click(location)

        # 2초 대기 
        time.sleep(self.time_run)
        pyperclip.copy(kakao_search)
        # 붙여넣기
        time.sleep(self.time_run)
        pyautogui.hotkey('ctrl', 'v')
        # 엔터
        time.sleep(self.time_run)
        pyautogui.press('enter')

        time.sleep(2)
        pyautogui.hotkey('winleft', 'left')
        time.sleep(self.time_run)   
    def drag(self):
        location_file = pyautogui.locateCenterOnScreen(self.img_path+'table.png',confidence = self.conf)
        location_kakao = pyautogui.locateCenterOnScreen(self.img_path+'message_window.png',confidence = self.conf)
        pyautogui.moveTo(location_file)
        time.sleep(self.time_run)
        pyautogui.mouseDown()
        pyautogui.moveTo(location_kakao)
        pyautogui.mouseUp()
        time.sleep(self.time_run)
        location = pyautogui.locateCenterOnScreen(self.img_path+'OK_Button.png',confidence = self.conf)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        