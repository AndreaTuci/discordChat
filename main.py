import pyautogui
from datetime import datetime, timedelta
import argparse


def chat(user, autoclick):
    f_in = open("testo.txt", 'r')
    lines = (line.rstrip() for line in f_in)
    rows_list = list(line for line in lines if line)
    can_write = True
    time_check = '16:04:00'
    print(f'Utente: {user}')
    print(f'Autoclick: {autoclick}')
    i = 0
    if user == 'fufunzio':
        i = 1
        time_check = ((datetime.strptime(time_check, '%H:%M:%S') + timedelta(0, 15)).time()).strftime("%H:%M:%S")
    elif user != 'wapto' and user != 'fufunzio':
        print('Launch program with one of those commands \n-----------------------------\n python main.py -u wapto \n python main.py -u fufunzio \n-----------------------------')
        exit()

    print(f'Avvio alle {time_check}')
    if i % 2 == 0:
        print('Leggo le righe dispari')
    else:
        print('Leggo le righe pari')
    print('Testo:')
    for r in rows_list:
        print(r)
    seconds_to_add = timedelta(0, 30)
    pyautogui.PAUSE = 10
    if autoclick == 'y' or autoclick == 'Y':
        screenWidth, screenHeight = pyautogui.size()
        x, y = screenWidth * 0.3294, screenHeight * 0.8463
        pyautogui.moveTo(x, y)
        pyautogui.click()
    while True:
        current_time = datetime.now().time()
        time_string = current_time.strftime("%H:%M:%S")
        if time_string == time_check and can_write == True:
            pyautogui.write(f'{rows_list[i]}', interval=0.01)
            pyautogui.press('enter')
            i+=2
            time_check = ((datetime.strptime(time_check, '%H:%M:%S') + seconds_to_add).time()).strftime("%H:%M:%S")

        elif time_string != time_check and can_write == False:
            can_write = True

        if i >= (len(rows_list)):
            pyautogui.write('*** Applausi ***', interval=0.01)
            pyautogui.press('enter')
            print(f'Il testo è finito, smetto')
            f_in.close()
            break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A Discord chat program.')
    parser.add_argument("-u", "--user", help = "Enter Discord username", default = "tats")
    parser.add_argument("-a", "--autoclick", help = "Autoclick [y/n]", default = "n")
    args = parser.parse_args()
    chat(args.user, args.autoclick)

