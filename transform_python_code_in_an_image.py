from pytoimage import PyImage

# Replace the 'tic_tac_toe_2.py' file name with your
code = PyImage('tic_tac_toe_2.py', background=(255, 255, 255))
palette = {'line': (255, 0, 255),
           'normal': (0, 0, 0)}
code.set_color_palette(palette=palette)
code.generate_image()
code.show_image()
code.save_image('codeImage.png')
