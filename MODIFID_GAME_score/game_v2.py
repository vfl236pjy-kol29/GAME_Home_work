"""Комп сам генерит и угадывает число"""
import numpy as np
def random_predict(number:int=1) -> int:
      count=0
      left,right=1,100
      while left<=right:
            count+=1
            predict=(left+right)//2  #берём середину диапазона
            if predict<number:
               left=predict+1        # если число больше, то отбрасывае левую половину диапазона чисел
            if predict>number:
                right=predict-1
            else:
                 return count
                
      return(count)
print(f'Количество попыток{random_predict()}')
def score_game(random_predict) -> int:
      count_ls=[]
      np.random.seed(1)
      random_array=np.random.randint(1,101,size=(1000))
      for number in random_array:
            count_ls.append(random_predict(number))
      score=int(np.mean(count_ls))
      print(f"ваш алгоритм угадывает число всреднем за {score} попыток")
      return(score)
# RUN
score_game(random_predict)