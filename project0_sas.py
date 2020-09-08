#!/usr/bin/env python
# coding: utf-8

# In[99]:


import numpy as np

def game_core_v3(number):
    '''На каждом шаге принимаем к рассмотрению целую часть от среднего арифметического 
       первого и последнего числа диапазона. Это число сравниваем больше оно или меньше нужного.
       Сокращаем диапазон по результатам сравнения. Для включения в условия проверки number=100
       первоночально устанавливаем конец диапазона number_end = 101. Функция возвращает число попыток'''
    count = 0
    number1 = 1
    number_end = 101
    while True:
        predict = (number1 + number_end)//2
        count += 1
        if number == predict: break
        elif number > predict: number1 = predict
        elif number < predict: number_end = predict
    return(count)


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
            count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    return(score)


print(f"Ваш алгоритм угадывает число в среднем за {score_game(game_core_v3)} попыток")


# In[ ]:




