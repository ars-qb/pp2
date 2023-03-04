import os

if not os.path.exists('alphabet'):
    os.mkdir('alphabet')

for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    filename = "%s.txt" % letter
    filepath = os.path.join('alphabet', filename)
    f = open(filepath, 'w')
    f.close()
