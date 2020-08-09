from sys import argv
import urllib3
from os import system as terminal
import requests
from colorama import Fore,Style
import os
import time

URL = "http://google.com"
CMD_CLEAR_TERM = "clear"

def check_proxy(proxy):

    try:
        session = requests.Session()
        session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        session.max_redirects = 300
        proxy = proxy.split('\n',1)[0]
        print(Fore.LIGHTYELLOW_EX + 'Checking ' + proxy)
        session.get(URL, proxies={'http':'http://' + proxy}, timeout=TIMEOUT,allow_redirects=True)
    except requests.exceptions.ConnectionError as e:
        print(Fore.LIGHTRED_EX + 'Error!')
        return e
    except requests.exceptions.ConnectTimeout as e:
        print(Fore.LIGHTRED_EX + 'Error,Timeout!')
        return e
    except requests.exceptions.HTTPError as e:
        print(Fore.LIGHTRED_EX + 'HTTP ERROR!')
        return e
    except requests.exceptions.Timeout as e:
        print(Fore.LIGHTRED_EX + 'Error! Connection Timeout!')
        return e
    except urllib3.exceptions.ProxySchemeUnknown as e:
        print(Fore.LIGHTRED_EX + 'ERROR unkown Proxy Scheme!')
        return e
    except requests.exceptions.TooManyRedirects as e:
        print(Fore.LIGHTRED_EX + 'ERROR! Zu viele weiterleitungen!')
        return e
def print_help():
    terminal(CMD_CLEAR_TERM)
    print(Fore.LIGHTGREEN_EX + 'Proxy Checker by Faultier')
    print(Fore.LIGHTGREEN_EX + 'Author: Faultier')
    print(Fore.LIGHTCYAN_EX)
    print('Verwendung -> prox -f <dateiname> - Proxy Liste Checken')
    print('prox -p <proxy> - Nur eine Proxy Checken')
    print('prox --help - Zeigt dir dieses Menü')

if len(argv) > 1:
    commands = ['--help','-h','-f','-p','/?','--file','-file','--proxy','-proxy']
    if argv[1] in commands:
        if argv[1] in ('--help','-help','/?','--?'):
            print_help()
        elif argv[1] in ('-f','--file','-file'):
            try:
                TIMEOUT = input(Fore.LIGHTGREEN_EX + 'Timeout: ')
                TIMEOUT = int(TIMEOUT)
                file = open(argv[2])
                proxies = list(file)
                goods = 0
                terminal(CMD_CLEAR_TERM)
                print(Fore.LIGHTCYAN_EX + '===========================================')
                for proxy in proxies:
                    try:
                        if check_proxy(proxy):
                            print(Fore.LIGHTRED_EX + 'Böse Proxy: ' + proxy)
                        else:
                            print(Fore.LIGHTGREEN_EX + 'Gute Proxy: ' + proxy)
                            file_with_goods = open('good.txt','a')
                            file_with_goods.write(proxy)
                            goods += 1
                        print(Fore.LIGHTCYAN_EX + '=================================================')
                    except KeyboardInterrupt:
                        print(Fore.LIGHTGREEN_EX + '\nExit.')
                        exit()
                print(Fore.LIGHTGREEN_EX + str(goods) + ' gute Proxys gefunden.')
                print(Fore.LIGHTRED_EX + str(len(proxies) - goods) + ' Böse Proxys gefunden.')
                time.sleep(7)
                print(Fore.WHITE + 'Setze farbe zurück.')
                os.system('clear')
                print()
            except FileNotFoundError:
                print(Fore.LIGHTRED_EX + 'Error!\nDatei nicht gefunden!')
            except IndexError:
                print(Fore.LIGHTRED_EX + 'Error!\nDateiname fehlt!')
        elif argv[1] in ('-p','--proxy','-proxy'):
            try:
                TIMEOUT = input(Fore.LIGHTGREEN_EX + 'Timeout: ')
                TIMEOUT = int(TIMEOUT)
                argv[2] = argv[2].split(' ')[0]
                if check_proxy(argv[2]):
                    print(Fore.LIGHTRED_EX + 'BÖSE PROXY ' + argv[2])
                else:
                    print(Fore.LIGHTGREEN_EX + 'GUTE PROXY ' + argv[2])
            except IndexError:
                print(Fore.LIGHTRED_EX + 'Error! Fehlende Proxy!')
    else:
        print(Fore.LIGHTRED_EX + 'Unknown option \"' + argv[1] + '\"')
else:
    print_help()