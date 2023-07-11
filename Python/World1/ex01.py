#Colors

#U'll use \033[m and if u want close write again \033[m
#Between the '[' 'm' write the codes of colors
print('\033[33mOlá, Mundo!\033[m')

name = 'Lucas'
print('Hello, {}{}{}!'.format('\033[4;34m', name, '\033[m'))

colors = {'clean':'\033[m', 
          'blue':'\033[34m', 
          'yellow':'\033[33m', 
          'blacknwhite':'\033[7;30m'}
print('I think this color for your name is cool: {}{}{}.'.format(colors['blacknwhite'], name, colors['clean']))
