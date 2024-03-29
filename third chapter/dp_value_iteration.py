import random
import time
# from yuanyang_env import YuanYangEnv
from CatMouseGame import CatMouseGame
import os
class DP_Value_Iter:
    def __init__(self, CMGame):
        self.states = CMGame.states
        self.actions = CMGame.actions
        self.v  = [ 0.0 for i in range(len(self.states) + 1)]
        self.pi = dict()
        self.cmgame = CMGame
        self.gamma = CMGame.gamma
        for state in self.states:
            flag1 = 0
            flag2 = 0
            flag1 = CMGame.collide(CMGame.state_to_position(state))
            flag2 = CMGame.find(CMGame.state_to_position(state))
            if flag1 == 1 or flag2 == 1: continue
            self.pi[state] = self.actions[int(random.random() * len(self.actions))]
    def reveseA(self,action):
        if action == 'e':
            return 'w'
        if action == 's':
            return 'n'
        if action == 'w':
            return 'e'
        if action == 'n':
            return 's'
    def value_iteration(self):
        for i in range(1000):

            if i % 2 == 0:
                CMGame.Move(action='e')
            else:
                CMGame.Move(action='s')

            delta = 0.0
            for state in self.states:
                flag1 = 0
                flag2 = 0
                flag1 = CMGame.collide(CMGame.state_to_position(state))
                flag2 = CMGame.find(CMGame.state_to_position(state))
                if flag1 == 1 or flag2 == 1: continue

                a1= self.actions[int(random.random()*4)]


                s, r, t = CMGame.transform(state, a1)
                #策略评估
                v1 = r + self.gamma * self.v[s]
                #策略改进
                for action in self.actions:
                    s, r, t = CMGame.transform(state, action)
                    if v1 < r + self.gamma * self.v[s]:
                        a1 = action
                        v1 = r + self.gamma * self.v[s]
                delta+= abs(v1 - self.v[state])
                self.pi[state] = a1
                self.v[state]  = v1
            if delta <  1e-7:
                print("迭代次数为",i)
                break
if __name__ == "__main__":
    CMGame = CatMouseGame()
    policy_value = DP_Value_Iter(CMGame)
    policy_value.value_iteration()
    # 将v值打印出来
    s = 0
    path = []
    for state in range(100):
        i = int(state / 10)
        j = state % 10
        CMGame.value[j, i] = policy_value.v[state]
    flag = 1
    step_num = 0
    # 将最优路径打印出来
    while flag:
        #渲染路径点
        path.append(s)
        CMGame.path = path
        a = policy_value.pi[s]
        print('%d->%s\t' % (s, a))
        CMGame.cat_position = CMGame.state_to_position(s)
        CMGame.mouse_position=CMGame.runway[int(step_num / 2)]
        CMGame.render()
        time.sleep(0.2)
        # os.system("pause")
        step_num += 1
        s_, r, t = CMGame.transform(s, a)
        if t == True or step_num > 20:
            flag = 0
        s = s_
    #渲染最后的路径点
    CMGame.cat_position = CMGame.state_to_position(s)
    path.append(s)
    CMGame.render()
    while True:
        CMGame.render()

        
