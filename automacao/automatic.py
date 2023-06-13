from pyautogui import alert, press, moveTo, write, hotkey, position, mouseDown, mouseUp, click, PAUSE, KEYBOARD_KEYS
from time import sleep


# Mandando mensagem para alguem na steam

def msgsteam(mensagem, destinatario):
    PAUSE = 0.5
    alert('O código começará. Pare de mexer no computador.')
    # Entrar na steam
    press('winleft')
    write('Steam')
    press('enter')
    sleep(13)

    # Clicar em conversas
    click(1848, 1006)
    sleep(1)

    # clicar em Pesquisar e pesquisar 'Oikawa'
    click(1873, 458)
    sleep(1)
    write(f'{destinatario}')
    sleep(1)
    press('enter')
    sleep(1)

    # Digitar a mensagem
    write(f'{mensagem}')
    sleep(1)

    # Apertar 'enter'
    press('enter')

    alert('O código parou. Pode voltar a mexer no computador.')


def msgwtt(mensagem, destinatario):
    PAUSE = 0.5
    alert('O código começará. Pare de mexer no computador.')

    # Abrir o chrome
    press('winleft')
    write('chrome')
    press('enter')
    sleep(2)

    # Clicar em pesquisar e digitar https://web.whatsapp.com/
    click(279, 52)
    sleep(1)
    write('https://web.whatsapp.com/')
    press('enter')
    sleep(6)

    # Clicar em pesquisar
    click(405, 170)

    # Digitar 1- Mamãe
    write(f'{destinatario}')
    sleep(2)
    # Apertar enter
    press('enter')
    sleep(2)

    # Digitar algo
    write(f'{mensagem}')
    sleep(1)

    # Apertar enter
    press('enter')
    sleep(2)

    alert('O código parou. Pode voltar a mexer no computador.')
