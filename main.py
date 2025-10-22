#import necessary modules
from project_lib import *
def main():
    print("This is a simple password generator, make sure to follow the instructions to get the best results.")
    print("To exit the program hit ctrl+c, the program will show the `KeyboardInterrupt` error which is normal.")
    print("\nEnjoy the program!\t\t\t\t\t created by:\tMohamed Laribi\n")
    def passwd():
        while True:
            mode= input("\nDo you want to get a random password(random) or Custom (custom) password? >> ").strip().lower()
            if mode in ("custom", "random"):
                break
            print("Invalid input")

        output=generate(mode)
        print(f"\n>>>\t{output}\t<<<\n")
        return output


    try:
        passwd_history=[]
        gen_passwd=passwd()
        passwd_history.append(gen_passwd)


        if(len(passwd_history) > 0):
            while True:
                another_passwd = input("\nDo you want to get another passwd ? [Y/n]: ").strip().lower()
                while another_passwd not in ("y", "n"):
                    print("Invalid entry, please retry")
                    another_passwd = input("\nDo you want to get another passwd ? [Y/n]: ").strip().lower()
                if another_passwd == "y":
                    gen_passwd = passwd()
                    passwd_history.append(gen_passwd)
                else:
                    break

            while True:
                see_passwd_history= input("\nDo you want to check the history of generated passwords? [Y/n]: ").strip().lower()
                if see_passwd_history in ("y", "n"):
                    if(see_passwd_history == "y"):
                        if len(passwd_history)==1:
                            gen_passwd= passwd_history[0]
                            print(len("    >>>    "+gen_passwd+"    <<<")*'-')
                            print(f">>>\t{gen_passwd}\t<<<")
                            print(len("    >>>    "+gen_passwd+"    <<<")*'-')
                            print()
                            while True:
                                copy_passwd= input("\nCopy this password to clipboard? [Y/n]>> ").strip().lower()
                                if copy_passwd in ("y", "n"):
                                    if copy_passwd== "n":
                                        msg="No password has been copied"
                                        break
                                    else:
                                        pyperclip.copy(gen_passwd)
                                        msg="Password copied to clipboard! Check it out"
                                    print("\n")
                                    print(" / \\")
                                    print("/_!_\ "+msg)
                                    break
                                print("Invalid input, please retry")
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
                            print("If you want to copy a password to your clipboard type its number, if you want none just type 0")
                            passwd_num_to_copy=""
                            passwd_num_to_copy_int=0
                            while True:
                                passwd_num_to_copy= input("Pick a password to copy to your clipboard>> ").strip().lower()
                                if passwd_num_to_copy.isdigit():
                                    passwd_num_to_copy_int= int(passwd_num_to_copy)
                                    if(passwd_num_to_copy_int > len(passwd_history) or passwd_num_to_copy_int <0):
                                        print("\nPlease pick a number from the list")
                                    else:
                                        break
                                else:
                                    print("\nPlease enter a numeric input, not a string")
                            if(0==passwd_num_to_copy_int):
                                msg="No password has been copied"
                            else:
                                pyperclip.copy(passwd_history[passwd_num_to_copy_int-1])
                                msg="Password copied to clipboard! Check it out"
                            print("\n")
                            print(" / \\")
                            print("/_!_\ "+msg)
                    break
                else:
                    print("Invalid entry, please retry")
    except KeyboardInterrupt:
        print("\n\n!!! Script interrupted by the user.. !!!\n")

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
print()