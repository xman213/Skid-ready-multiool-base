import  os
import pystyle
from pystyle import Colorate, Anime, Colors
import pypresence
import time


os.system('title MULTITOOL BASE (made by xman)')
client_id = 972561329141473321 
try:
    rpc = pypresence.Presence(client_id)
    rpc.connect()
    start_time = time.time()
    rpc.update(large_image="img",large_text="Multitool base ", details="A multitool base by xman",
               state="Im alive!", start=start_time)
except pypresence.exceptions.DiscordNotFound:
    pass





menu = """

███████╗░█████╗░██████╗░  ██╗░░░██╗░█████╗░██╗░░░██╗  ░██████╗██╗░░██╗██╗██████╗░░██████╗
██╔════╝██╔══██╗██╔══██╗  ╚██╗░██╔╝██╔══██╗██║░░░██║  ██╔════╝██║░██╔╝██║██╔══██╗██╔════╝
█████╗░░██║░░██║██████╔╝  ░╚████╔╝░██║░░██║██║░░░██║  ╚█████╗░█████═╝░██║██║░░██║╚█████╗░
██╔══╝░░██║░░██║██╔══██╗  ░░╚██╔╝░░██║░░██║██║░░░██║  ░╚═══██╗██╔═██╗░██║██║░░██║░╚═══██╗
██║░░░░░╚█████╔╝██║░░██║  ░░░██║░░░╚█████╔╝╚██████╔╝  ██████╔╝██║░╚██╗██║██████╔╝██████╔╝
╚═╝░░░░░░╚════╝░╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚═════╝░╚═╝░░╚═╝╚═╝╚═════╝░╚═════╝░

1 -- ur thing here
2 -- ur thing here
3 -- ur thing here
 
 
"""

print(Colorate.Horizontal(Colors.red_to_blue, (menu)))

if __name__ == '__main__':
    while (True):
        
        

        
        
         
        option = int(input(Colorate.Horizontal(Colors.blue_to_red,'What tool would you like to use? -->')))

        
        if option == 1:
             print(Colorate.Horizontal(Colors.blue_to_red,'do something'))

        elif option == 2:
             print(Colorate.Horizontal(Colors.blue_to_red,'do something'))
        
        elif option == 3:
             print(Colorate.Horizontal(Colors.blue_to_red,'do something'))
