#definicao das bibliotecas e configuracao de escala e cores da interface

import PySimpleGUI as sg
import numpy as np
#------------------------------------------------------------------------------

def get_scaling():
    # called before window created
    root = sg.tk.Tk()
    scaling = root.winfo_fpixels('1i')/72
    root.destroy()
    return scaling

# Find the number in original screen when GUI designed.
my_scaling = 1.33333333333      # call get_scaling()
my_width, my_height = 1920, 1080     # call sg.Window.get_screen_size()

# Get the number for new screen
scaling_old = get_scaling()
width, height = sg.Window.get_screen_size()

scaling = scaling_old * min(width / my_width, height / my_height)

sg.set_options(scaling=scaling)
# -------------------------------------------------------------------------
sg.theme('reddit')
backgroundc='white'

#definicao da matriz do tabuleiro  
MAX_ROWS = MAX_COL = 6
state=np.full((MAX_ROWS,MAX_COL), False)
linha=[]
l=10

#configuracao dos botoes habilitados e desabilitados e posicionamento dos botoes na interface
for i in range(MAX_ROWS):
    dado=[]
    for j in range(MAX_COL):
        dado.append(sg.pin(sg.Button('', size=(l, int(l/2)), key=(i,j), pad=(0,0),disabled=True,button_color='black',expand_x=True, expand_y=True)))
    linha.append([
                sg.pin(sg.Button('', size=(l, int(l/2)), key=(i,-1), pad=(75,0),disabled=False)),*dado
                ])
base=[]
dado2=[]
for j in range(MAX_COL):
        dado2.append(sg.pin(sg.Button('', size=(l, int(l/2)), key=(-1,j), pad=(0,75),disabled=False)))
base.append([
    sg.pin(sg.Button('', size=(l, int(l/2)), key=(-1,-1), pad=((75,75),0),disabled=True,border_width=0,button_color=backgroundc)),*dado2
]    
)

layout =  [
linha,base,
           ]

#Logica utilizada para finalizar o programa.
window = sg.Window('Tabuleiro de Lâmpadas', layout,auto_size_text=True,
                   auto_size_buttons=True, resizable=True, grab_anywhere=False, border_depth=5,
                   default_element_size=(15, 1), finalize=True,background_color=backgroundc).Finalize()

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

#Logica utilizada para alterar as cores das casas selecionadas do tabuleiro.
    if event[0]==-1:
        state[:,event[1]]=np.invert(state[:,event[1]])
        for n in range(MAX_COL):
            if state[n,event[1]]:
                color='red'
            else:
                color='black'
            window[(n,event[1])].update(button_color=('white',color))
    if event[1]==-1:
        state[event[0],:]=np.invert(state[event[0],:])
        for n in range(MAX_ROWS):
            if state[event[0],n]:
                color='red'
            else:
                color='black'
            window[(event[0],n)].update(button_color=('white',color))
window.close()

