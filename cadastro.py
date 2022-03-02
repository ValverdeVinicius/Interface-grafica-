from PySimpleGUI import PySimpleGUI as sg

sg.theme('Black')

layout = [
    [sg.Text('Usuário'),sg.Input(key = 'Usuário')],
    [sg.Text('Senha'),sg.Input(key = 'Senha', password_char = '*')],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('Entrar')]
]

janela = sg.Window('Tela de Login', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['Usuário'] == 'Vinícius' and valores ['Senha'] == '1234':
            print('Bem vindo!')