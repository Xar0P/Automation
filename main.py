import pyautogui as pygui
import time
import pyperclip as pyclip
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


class Vivaldi:

    def __init__(self) -> None:
        self._open()
        self.actions = ActionChains(self.driver)
    
    def _open(self) -> None:
        options = Options()
        options.add_argument('start-maximized')
        options.binary_location = r"C:\Users\pietr\AppData\Local\Vivaldi\Application\vivaldi.exe"
        self.driver = webdriver.Chrome(executable_path=r'chromedriver.exe', options=options)

    def site(self, url) -> None:
        self.driver.get(url)

    def get_element_class(self, cl) -> None:
        search = self.driver.find_element_by_class_name(cl)

        self.actions.move_to_element(search)
        self.actions.double_click()
        
        self.actions.perform()


vivaldi = Vivaldi()
vivaldi.site('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
vivaldi.get_element_class('bSmy5')



# pygui.moveTo(x=72, y=229)

# scr_width, scr_height = pygui.size()
# cur_mousex, cur_mousey = pygui.position()


# def open_site(url = 'https://www.google.com') -> None:
#     pyclip.copy(url)
#     pygui.hotkey('ctrl','t')
#     pygui.hotkey('ctrl', 'v')
#     pygui.press('enter')
#     time.sleep(10)

# def move_mouse():
#     pygui.moveTo(scr_width/2,scr_height/2)

# pygui.PAUSE = 1 # A cada execução, pausa 1 segundo

# pygui.alert('O programa vai iniciar, clique em OK e não mexa em nada!')
# open_app('vivaldi')
# open_site('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
# move_mouse()
