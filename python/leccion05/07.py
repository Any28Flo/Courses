# Consider we´re develop a game with a alineas as a character
# This aligien got special charactericts
# color , point
alien = {'color' : 'yellow', 'points': 0}
# add new characteristics to our alien x_position, y_position and speed

alien['x_position'] = 0
alien['y_position'] = 0
alien['speed'] = 'slow'

print(alien)

if alien['speed'] == 'slow':
    alien['x_increment'] = 1
elif alien['speed'] == 'medium':
    alien['x_increment'] = 2
else:
    # This must be a fast alien
    alien['x_increment'] = 3

alien['x_position'] = alien['x_position'] + alien['x_increment']

print(f'color: {alien["color"]} point : { alien["points"]} x position: {alien["x_position"]}')