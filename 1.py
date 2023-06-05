number = int(input('Введите произвольное число: '))
border=11
if number < border:
    print('Ваше число меньше пограничного')
elif number > border:
    print('Ваше число больше пограничного')
if number > border * 3:
    print('Ваше число больше пограничного более, чем в 3 раза')

     
