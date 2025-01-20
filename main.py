#import necessary modules
from project_lib import *
def main():
    print("This is a simple password generator, make sure to follow the instructions to get the best results.")
    print("To exit the program hit ctrl+c, the program will show the `KeyboardInterrupt` error which is normal.")
    print("\nEnjoy the program!\t\t\t\t\t created by:\tMohamed Laribi (A script kiddie)\n")
    def passwd():
        mode= input("Do you want to get a random password(random) or Custom (custom) password? >> ")
        while mode.lower() != "random" and mode.lower() != "custom":
            print("invalid input")
            mode= input("Type `custom` or `random` to choose the genrerating mode>> ")
        mode= mode.lower()

        output=generate(mode)
        print(f"\n>>>\t{output}\t<<<\n")
        return output

    passwd_history=[]
    passwd_history.append(passwd())


    while True:
        another_passwd= input("Do you want to get another passwd ? [Y/n]: ")
        while not (another_passwd.upper()=="Y" or another_passwd.lower()=="n"):
            print("invalid entry, please retry")
            another_passwd= input("Do you want to get another passwd ? [Y/n]: ")
        if another_passwd.upper()=="Y":
                passwd_history.append(passwd())
        else:
            break

    while True:
        see_passwd_history= input("Do you want to check the history of generated passwords? [Y/n]: ")
        while not (see_passwd_history.upper()=="Y" or see_passwd_history.lower()=="n"):
            print("invalid entry, please retry")
            see_passwd_history= input("Do you want to check the history of generated passwords ? [Y/n]: ")
        i=1
        if see_passwd_history.upper()=="Y":
                if len(passwd_history)==1:
                    print(len("    >>>    "+passwd_history[len(passwd_history)-1]+"    <<<")*'-')
                    print(f">>>\t{passwd_history[len(passwd_history)-1]}\t<<<")
                    print(len("    >>>    "+passwd_history[len(passwd_history)-1]+"    <<<")*'-')
                    print()
                else:
                    max_len= 0
                    i=0
                    for passwd in passwd_history:
                        if i<1:
                            max_len= len(passwd)
                            i+=1
                        else:
                            if len(passwd)> max_len:
                                max_len= len(passwd)
                    i=1
                    hr= "-"*(max_len+14)
                    print()
                    for passwd in passwd_history:
                        dynamic_space= max_len-len(passwd)+10
                        print(f"{i}){hr}")
                        print(f">>>{' '*(dynamic_space//2)}{passwd}{' '*(dynamic_space//2)}<<<")
                        i+=1
                    print(hr+"--","\n")
                break
        else: break

#####################################################################################################
print()
print("                                  (-)--(|)--(-)        ")
print("                               (-)      |      (-)     ")
print("                              (-)       |       (-)    ")
print("                             (-)        |        (-)   ")
print("                             (-)        |        (-)   ")
print("                             [][-][-][-]|[-][-][-][]   ")
print("                            [-]--------(|)--------[-]  ")
print("                            [-]-------(°|°)-------[-]  ")
print("                            [-]-------(°|°)-------[-]  ")
print("                            [-]--------(|)--------[-]  ")
print("                             [][-][-][-]|[-][-][-][]   ")
print()
print("PPPPPPP     AAAA     SSSSS      SSSSS   WW         WW   OOOOOOO   RRRRRRRR   DDDDDDD")
print("PP    PP   AA  AA   SSS   SS  SSS   SS  WW         WW  OO     OO  RR     RR  DD    DD")
print("PP    PP  AAA  AAA  SS        SS        WW    W    WW  OO     OO  RR     RR  DD     DD")
print("PPPPPP    AAAAAAAA   SSSSS     SSSSS    WW   WWW   WW  OO     OO  RRRRRRR    DD     DD")
print("PP        AA    AA       SSS       SSS  WW  WWWWW  WW  OO     OO  RR   RR    DD     DD")
print("PP        AA    AA   SS   SS   SS   SS  WWWWW   WWWWW  OO     OO  RR    RR   DD    DD")
print("PP        AA    AA    SSSSS     SSSSS   WWW       WWW   OOOOOOO   RR     RR  DDDDDDD")
print()
print("GGGGGGG   EEEEEEEE  NN     NN  EEEEEEEE  RRRRRRRR     AAAA    TTTTTTTTTTTTT   OOOOOOO   RRRRRRRR")
print("GG    G   EEEEEEEE  NNN    NN  EEEEEEEE  RR     RR   AA  AA   TTTTTTTTTTTTT  OO     OO  RR     RR")
print("GG        EEE       NNNN   NN  EEE       RR     RR  AAA  AAA       TTT       OO     OO  RR     RR")
print("GG  GGG   EEEEEEEE  NN NN  NN  EEEEEEEE  RRRRRRR    AAAAAAAA       TTT       OO     OO  RRRRRRR")
print("GG  GGG   EEE       NN  NN NN  EEE       RR   RR    AA    AA       TTT       OO     OO  RR   RR")
print("GG   GG   EEEEEEEE  NN   NNNN  EEEEEEEE  RR    RR   AA    AA       TTT       OO     OO  RR    RR")
print("GGGGGGG   EEEEEEEE  NN     NN  EEEEEEEE  RR     RR  AA    AA       TTT        OOOOOOO   RR     RR")
print()
########################################################################################################
main()