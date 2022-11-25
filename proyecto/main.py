import library.triqui
import library.ahorcado 
import library.adivina_el_numero
import library.figura
import library.figura2
print("""




█▄▄ █ █▀▀ █▄░█ █░█ █▀▀ █▄░█ █ █▀▄ █▀█    ▄▀█    █▀█ ▄▀█ █▀█ ▄▀█ █▀▄ █ █▀
█▄█ █ ██▄ █░▀█ ▀▄▀ ██▄ █░▀█ █ █▄▀ █▄█    █▀█    █▀▀ █▀█ █▀▄ █▀█ █▄▀ █ ▄█

""")
opcion = "1"
while opcion!="0":
    
    print("selecciona la opcion")
    opcion = input()
    if opcion == "1":
   		library.triqui.main_triqui()
    if opcion == "2":
   		library.ahorcado.main_ahorcado()
    if opcion == "3":
        library.adivina_el_numero.main_adivina_el_numero()
    if opcion == "4":
        library.figura.main_figura()
    if opcion == "5":
        library.figura2.main_figura2()
           