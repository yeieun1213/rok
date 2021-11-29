"""
1. 필요한 라이브러리 다운받기
pycharm 프로그램 밑에
TODO-Problems-Terminal-Python Packages-Python Console
메뉴가 있는데 그 중 Terminal을 열어서 아래에 있는 설치 명령어 한줄씩! 입력
pip install pyautogui
pip install clipboard
"""
import pyautogui
import clipboard
import time
import os

today = time.strftime('%m%d', time.localtime(time.time()))
"""
2. 저장 위치 바꾸기!
폴더 만들어서 폴더 경로 입력
"""
root = 'C:/Users/yeieu/Desktop/rok/'

"""
3. 세팅: 랭킹에서 1등의 숫자1에 커서 두기
4. 실행: Shift + F10 
"""

rank, goal = 1, 400
list = []

# to print a current cursor position
def position():
    while(True):
        print(pyautogui.position())
        time.sleep(1)

class autoRok():
    def __init__(self):
        super().__init__()
        #self.test()
        self.setting()

    def Rank(self, rank):
        self.rank = rank

    def test(self):
        # 203, 264, 321, 376
        self.rank1X = 165
        self.rank1Y = 211
        self.rank4X = 165
        self.rank4Y = 378
        self.nicknameX = 379
        self.nicknameY = 210
        self.killpointsX = 626
        self.killpointsY = 251
        self.leftupperX = 120
        self.leftupperY = 100
        self.rightbottomX = 800
        self.rightbottomY = 510
        self.closeX = 755
        self.closeY = 105
        self.nextX = 160
        self.nextY = 380
        self.beforeX = 160
        self.beforeY = 270
        self.X = self.rightbottomX - self.leftupperX
        self.Y = self.rightbottomY - self.leftupperY
        self.testtest = 0


# SETTING of start position
    def setting(self):
        print("please enter rank screen")
        time.sleep(1)

        # 1등 랭킹 그림
        print("1등")
        #print("put your mouse on the rank 1 picture")
        time.sleep(5)
        self.rank1X, self.rank1Y = pyautogui.position()
        print("success:", self.rank1X, self.rank1Y, "\n")

        # 4등 랭킹 그림
        print("4등")
        #print("put your mouse on the rank 4 picture")
        time.sleep(5)
        self.rank4X, self.rank4Y = pyautogui.position()
        print("success:", self.rank4X, self.rank4Y, "\n")
        time.sleep(0.3)
        pyautogui.click(self.rank4X, self.rank4Y)

        # nickname
        print("닉네임")
        #print("put your mouse on the nickname")
        time.sleep(5)
        self.nicknameX, self.nicknameY = pyautogui.position()
        print("success:", self.nicknameX, self.nicknameY, "\n")

        # killpoints
        print("킬포 옆 물음표")
        #print("put your mouse on ? mark for detail of kill points")
        time.sleep(5)
        self.killpointsX, self.killpointsY = pyautogui.position()
        time.sleep(0.3)
        pyautogui.click(self.killpointsX, self.killpointsY)
        print("success:", self.killpointsX, self.killpointsY, "\n")

        # 왼쪽 위 모서리
        print("왼쪽 위 모서리")
        #print("put your mouse on the upper left corner")
        time.sleep(5)
        self.leftupperX, self.leftupperY = pyautogui.position()
        print("success:", self.leftupperX, self.leftupperY, "\n")

        # 오른쪽 아래 모서리
        print("오른쪽 아래 모서리")
        #print("put your mouse on the bottom right corner")
        time.sleep(5)
        self.rightbottomX, self.rightbottomY = pyautogui.position()
        print("success:", self.rightbottomX, self.rightbottomY, "\n")

        # X
        print("닫게 오른쪽 위에 X표시")
        #print("put your mouse on X mark near the upper right corner")
        time.sleep(5)
        self.closeX, self.closeY = pyautogui.position()
        time.sleep(0.3)
        pyautogui.click(self.closeX, self.closeY)
        print("success", self.closeX, self.closeY, "\n")

        # 5등 랭킹 그림
        print("5등")
        #print("put your mouse on the rank 5 picture")
        time.sleep(5)
        self.nextX, self.nextY = pyautogui.position()
        print("success", self.nextX, self.nextY, "\n")

        # 4등 랭킹 그림
        print("4등")
        # print("put your mouse on the rank 5 picture")
        time.sleep(5)
        self.beforeX, self.beforeY = pyautogui.position()
        print("success", self.beforeX, self.beforeY, "\n")

        self.X = self.rightbottomX - self.leftupperX
        self.Y = self.rightbottomY - self.leftupperY

        pyautogui.moveTo(self.closeX, self.closeY)
        time.sleep(0.3)
        pyautogui.click(self.closeX, self.closeY)
        time.sleep(0.3)
        pyautogui.moveTo(self.rank4X, self.rank4Y)
        time.sleep(0.3)
        pyautogui.click(self.rank4X, self.rank4Y)
        time.sleep(0.3)
        print("----------setting done----------\n\n")


    # to find a user in auto-scrolling with 'pyautogui'.
    # it makes the point move, drag and click automatically.
    def find_user(self):
        if self.rank > 4:
            #if self.rank == 6 and self.testtest == 0:
            #    list[-1] = '이 사 부 선장'
            pyautogui.moveTo(self.nextX, self.nextY)
            time.sleep(0.3)
            pyautogui.click(self.nextX, self.nextY)
            time.sleep(0.5)
            pyautogui.moveTo(self.nicknameX, self.nicknameY)
            time.sleep(0.3)
            pyautogui.click(self.nicknameX, self.nicknameY)
            time.sleep(0.3)
            name = clipboard.paste()
            time.sleep(0.3)
            # 순위 변동 있을 시 혹은 복붙이 제 타이밍에 잘 안됐을 경우
	"""
            if name in list:
                #while(True):
                for i in range(5):
                    #self.testtest = 1
                    self.rank -= 1
                    list.pop()
                    pyautogui.moveTo(self.closeX, self.closeY)
                    time.sleep(0.3)
                    pyautogui.click(self.closeX, self.closeY)
                    time.sleep(0.3)
                    pyautogui.moveTo(self.beforeX, self.beforeY)
                    time.sleep(0.3)
                    pyautogui.click(self.beforeX, self.beforeY)
                    time.sleep(0.5)
                    #if name not in list:
                    if i == 4:
                        pyautogui.moveTo(self.nicknameX, self.nicknameY)
                        time.sleep(0.3)
                        pyautogui.click(self.nicknameX, self.nicknameY)
                        time.sleep(0.3)
                        name = clipboard.paste()
                        time.sleep(0.3)
                        break
	"""
            list.append(name)
            pyautogui.moveTo(self.killpointsX, self.killpointsY)
            time.sleep(0.3)
            pyautogui.click(self.killpointsX, self.killpointsY)
            time.sleep(0.3)
            return
        elif self.rank  == 4:
            pyautogui.moveTo(self.rank4X, self.rank4Y)
            time.sleep(0.3)
            pyautogui.click(self.rank4X, self.rank4Y)
            time.sleep(0.5)
            pyautogui.moveTo(self.nicknameX, self.nicknameY)
            time.sleep(0.3)
            pyautogui.click(self.nicknameX, self.nicknameY)
            time.sleep(0.3)
            list.append(clipboard.paste())
            pyautogui.moveTo(self.killpointsX, self.killpointsY)
            time.sleep(0.3)
            pyautogui.click(self.killpointsX, self.killpointsY)
            time.sleep(0.3)
            return
        elif self.rank == 1:
            time.sleep(1)
            pyautogui.moveTo(self.rank1X, self.rank1Y)
            time.sleep(0.3)
            pyautogui.click(self.rank1X, self.rank1Y)
            time.sleep(1)
            pyautogui.moveTo(self.nicknameX, self.nicknameY)
            time.sleep(0.3)
            pyautogui.click(self.nicknameX, self.nicknameY)
            time.sleep(0.3)
            list.append(clipboard.paste())
            pyautogui.moveTo(self.killpointsX, self.killpointsY)
            time.sleep(0.3)
            pyautogui.click(self.killpointsX, self.killpointsY)
            time.sleep(0.3)
            return
        elif self.rank == 2:
            rank2Y = self.rank4Y/3*1 + self.rank1Y/3*2
            pyautogui.moveTo(self.rank1X, rank2Y)
            time.sleep(0.3)
            pyautogui.click(self.rank1X, rank2Y)
            time.sleep(0.5)
            pyautogui.moveTo(self.nicknameX, self.nicknameY)
            time.sleep(0.3)
            pyautogui.click(self.nicknameX, self.nicknameY)
            time.sleep(0.3)
            list.append(clipboard.paste())
            pyautogui.moveTo(self.killpointsX, self.killpointsY)
            time.sleep(0.3)
            pyautogui.click(self.killpointsX, self.killpointsY)
            time.sleep(0.3)
            return
        elif self.rank == 3:
            rank3Y = self.rank4Y/3*2 + self.rank1Y/3*1
            pyautogui.moveTo(self.rank1X, rank3Y)
            time.sleep(0.3)
            pyautogui.click(self.rank1X, rank3Y)
            time.sleep(0.5)
            pyautogui.moveTo(self.nicknameX, self.nicknameY)
            time.sleep(0.3)
            pyautogui.click(self.nicknameX, self.nicknameY)
            time.sleep(0.3)
            list.append(clipboard.paste())
            pyautogui.moveTo(self.killpointsX, self.killpointsY)
            time.sleep(0.3)
            pyautogui.click(self.killpointsX, self.killpointsY)
            time.sleep(0.3)
            return

    def capture(self):
        print("rank: ", self.rank)
        img = root + str(rank) + '_all.png'
        pyautogui.screenshot(img, region=(self.leftupperX, self.leftupperY, self.X, self.Y))
        print("nickname:", list[-1])
        time.sleep(0.5)

    def close(self):
        pyautogui.moveTo(self.closeX, self.closeY)
        time.sleep(0.3)
        pyautogui.click(self.closeX, self.closeY)
        time.sleep(0.3)

    def main(self, goal):
        while(self.rank <= goal):
            time.sleep(0.3)
            self.find_user()
            #time.sleep(0.5)
            self.capture()
            time.sleep(0.5)
            self.close()
            time.sleep(0.5)
            self.rank += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #position()
    auto = autoRok()
    time.sleep(3)
    rank = int(input("start rank:"))
    goal = int(input("goal rank:"))
    #rank = 4
    #goal = 10
    start = rank
    auto.Rank(rank)
    auto.main(goal)
    print(list)

auto = autoRok()
time.sleep(3)
rank = int(input("start rank:"))
goal = int(input("goal rank:"))
#rank = 4
#goal = 10
start = rank
auto.Rank(rank)
auto.main(goal)
print(list)