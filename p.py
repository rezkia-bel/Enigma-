import colorama
from colorama import Fore
from colorama import Style
import numpy as np


"""colorama.init()
print(Fore.BLUE + Style.BRIGHT + "This is the color of the sky" + Style.RESET_ALL)
print(Fore.GREEN + "This is the color of grass" + Style.RESET_ALL)
print(Fore.BLUE + Style.DIM + "This is a dimmer version of the sky" + Style.RESET_ALL)
print(Fore.YELLOW + "This is the color of the sun" + Style.RESET_ALL)
quit()"""
#le vecteur d'alphabet
alpha = ["A","B","C","D","E","F","J","H","I","G","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
colorama.init()
print(Fore.BLUE + Style.BRIGHT , alpha , Style.RESET_ALL)
#R1
R1L1 = [+10,+21,+5,-17,+21,-4,+12,+16,+6,-3,+7,-7,+4,+2,+5,-7,-11,-17,-9,-6,-9,-19,+2,-3,-21,-4]
R1L2 = [+17,+4,+19,+21,+7,+11,+3,-5,+7,+9,-10,+9,+17,+6,-6,-2,-4,-7,-12,-5,+3,+4,-21,-16,-2,-21]
R2L1 = [+3,+17,+22,+18,+16,+7,+5,+1,-7,+16,-3,+8,+2,+9,+2,-5,-1,-13,-12,-17,-11,-4,+1,-10,-19,-25]
R2L2 = [+25,+7,+17,-3,+13,+19,+12,+3,-1,+11,+5,-5,-7,+10,-2,+1,-2,+4,-17,-8,-16,-18,-9,-1,-22,-16]
R3L1 = [+1,+16,+5,+17,+20,+8,-2,+2,+14,+6,+2,-5,-12,-10,+9,+10,+5,-9,+1,-14,-2,-10,-6,+13,-10,-23]
R3L2 = [+12,-1,+23,+10,+2,+14,+5,-5,+9,-2,-13,+10,-2,-8,+10,-6,+6,-16,+2,-1,-17,-5,-14,-9,-20,-10]
reflecteur = [+25,+23,+21,+19,+17,+15,+13,+11,+9,+7,+5,+3,+1,-1,-3,-5,-7,-9,-11,-13,-15,-17,-19,-21,-23,-25]

print("entrer la clé sous fomre de trois triples: \n")

key1 = input("1er triple: ")
# 1 er tuple de la clé
if len(key1) == 9 or len(key1) == 10: 
   key1 = key1.split(",")
   print(key1)
   for x in range(len(key1)):
      r = key1[x]
      r = r.replace("(","") 
      r = r.replace(")","")
      key1[x] = r
      if x == 2:
         try:
            key1[x] = int(key1[x])
         except:
            print("vous n\'avez pas entrer la valeur de décalage initial")
            quit() 
   #for x in range(len(key1)):
   if (key1[0] == "R1"or key1[0] =="R2" or key1[0] =="R3") and (key1[1] == "D" or key1[1] =="G"):
        rotor1 = key1[0] # sauvgarder le 1 er rotors à comencer à tourner
        print("voici le premier triple : ", key1, "\n")
   else:
        print("le premier triple est erroné!!")
        quit() 

   # deuxième triple de la clé
   key2 = input("2 ème triple: ")
   if len(key2) == 9 or len(key2) == 10: 
        key2 = key2.split(",")
        print(key2)
        for x in range(len(key2)):
            r = key2[x]
            r = r.replace("(","") 
            r = r.replace(")","")
            key2[x] = r
            if x == 2:
                try:
                    key2[x] = int(key2[x])
                except:
                    print("vous n\'avez pas entrer la valeur de décalage initial")
                    quit() 
   
        if (key2[0] == "R1" or key2[0] =="R2" or key2[0] =="R3") and (key2[0] != rotor1) and (key2[1] == "D" or key2[1] =="G"):
            rotor2 = key2[0] #sauvgarder la valeur de 2 ème rotor
            print("voici le 2 ème triple: ",key2, "\n")
        else:
            print("le deuxième triple est erroné")
            quit()

        # 3 ème triple de la clé
        key3 = input("3 ème triple: ")
        if len(key3) == 9 or len(key3) == 10: 
            key3 = key3.split(",")
            print(key3)
            for x in range(len(key3)):
                r = key3[x]
                r = r.replace("(","") 
                r = r.replace(")","")
                key3[x] = r
                if x == 2:
                    try:
                        key3[x] = int(key3[x])
                    except:
                        print("vous n\'avez pas entrer la valeur de décalage initial")
                        quit() 
                #for x in range(len(key2)):
            if (key3[0] == "R1" or key3[0] =="R2" or key3[0] =="R3") and (key3[0] != rotor2) and (key3[0] != rotor1) and (key3[1] == "D" or key3[1] =="G"):
                rotor3 = key3[0] #sauvgarder la valeur de 2 ème rotor
                print("voici le 3 ème triple: ",key3, "\n")
            else:
                print("le troixième triple est erroné") #erreur
                quit()
        else:
            print("le format est erroné")   
   else:
       print("Le format est erroné")        
else:
    print("le format de la clé est erroné")

print("la clé est :" , key1, key2, key3)

######################################################### Le message à encrypter#####################################################
def config(l1,l2):
    rotor = np.array(l2)
    l2 = np.roll(rotor,l1[2])
    return l2

"""def encodage (msg,alpha,R1,R2,R3,ref, R1R,R2R,R3R):
    s = ""
    for x in range(len(msg)):
        for y in range(len(alpha)):
            if msg[x] == alpha[y]:
                v = R1[y]
                print(v)
                if(v >= 0):
                    v = (v+R2[v]) % 26
                    print(v)
                else:
                    v = (v+R2[-v]) % 26
                    print(v)
                if (v >= 0):
                    v = (v + R3[v]) % 26
                    print(v)
                else:
                    v = (v + R3[-v]) % 26
                    print(v)

                if (v >= 0):
                    v = (v + ref[v]) % 26
                    print(v)
                else:
                    v = (v + ref[-v]) % 26
                    print(v)

                if(v >= 0):
                    v = (v + R3R[v]) % 26
                    print("ddd",v)
                else:
                    v = (v + R3R[-v]) % 26
                    print(v)
                
                if(v >= 0):
                    v = (v + R2R[v]) % 26
                    print(v)
                else:
                    v = (v + R2R[-v]) % 26
                    print(v)

                if(v >= 0):
                    v = (v + R1R[v]) % 26
                    print(v)
                else:
                    v = (v + R1R[-v]) % 26
                    print(v)
                
                if (v >= 0):
                    s = s + alpha[v]
                    print(v)
                else:
                    s = s + alpha[-v]
                    
        return s"""

def encodage (msg,alpha,R1,R2,R3,ref, R1R,R2R,R3R):
    global alpha, ref, R1L1,R1L2,R2L1,R2L2,R3L1,R3L2
    R1 = R1L1
    R1R = R1L2
    R2 = R2L1
    R2R = R2L2
    R3 = R3L1
    R3R = R3L2
    s = ""
    #for x in range(len(msg)):
        for y in range(len(alpha)):
            if msg == alpha[y]:
                v = R1[y]
                print(v)
                if(v >= 0):
                    v = (v+R2[v]) % 26
                    print(v)
                else:
                    v = (v+R2[-v]) % 26
                    print(v)
                if (v >= 0):
                    v = (v + R3[v]) % 26
                    print(v)
                else:
                    v = (v + R3[-v]) % 26
                    print(v)

                if (v >= 0):
                    v = (v + ref[v]) % 26
                    print(v)
                else:
                    v = (v + ref[-v]) % 26
                    print(v)

                if(v >= 0):
                    v = (v + R3R[v]) % 26
                    print("ddd",v)
                else:
                    v = (v + R3R[-v]) % 26
                    print(v)
                
                if(v >= 0):
                    v = (v + R2R[v]) % 26
                    print(v)
                else:
                    v = (v + R2R[-v]) % 26
                    print(v)

                if(v >= 0):
                    v = (v + R1R[v]) % 26
                    print(v)
                else:
                    v = (v + R1R[-v]) % 26
                    print(v)
                
                if (v >= 0):
                    s = alpha[v]
                    print(v)
                else:
                    s = alpha[-v]
        return s
#configuration de rotor après l'encréption d'une lettre

def configRotor (key, R):
    rotor = np.array(R)
    if(key[1] == "G"):
        R = np.roll(rotor, -1)
    else:
        R = np.roll(rotor, +1)
    return R

msgclaire = input("entrer le message à encrypter: ")
msgclaire = msgclaire.replace(" ","") #transformer le msg en msg sans espaces
print("le msg en claire est: ",msgclaire)

#s = encodage(msgclaire, alpha, R1L1, R2L1, R3L1, reflecteur, R1L2, R2L2, R3L2)
#print(s)
if (str.isalpha(msgclaire)): # vérifier que le msg contient que des lettres
    if(key1[0] == "R1"):
        R1L1 = config(key1,R1L1)
        R1L2 = config(key1,R1L2)
    elif(key1[0] == "R2"):
        R2L1 = config(key1,R2L1)
        R2L2 = config(key1,R2L2)
    else:
        R3L1 = config(key1,R3L1)
        R3L2 = config(key1,R3L2)

    if(key2[0] == "R1"):
        R1L1 = config(key2,R1L1)
        R1L2 = config(key2,R1L2)
    elif(key2[0] == "R2"):
        R2L1 = config(key2,R2L1)
        R2L2 = config(key2,R2L2)
    else:
        R3L1 = config(key2,R3L1)
        R3L2 = config(key2,R3L2)

    if(key3[0] == "R1"):
        R1L1 = config(key3,R1L1)
        R1L2 = config(key3,R1L2)
    elif(key3[0] == "R2"):
        R2L1 = config(key3,R2L1)
        R2L2 = config(key3,R2L2)
    else:
        R3L1 = config(key3,R3L1)
        R3L2 = config(key3,R3L2)
    print(R1L1,"\n",R1L2,"\n\n",R2L1,"\n",R2L2, "\n\n", R3L1,"\n",R3L2)
    configEnitEnd = True
    print("la configuration initial est téreminé")


else:
    print("votre message doit contenir que des lettre")
    quit()

K1 = 0
K2 = 0
K3 = 0

if ( configEnitEnd == True):
    print(configEnitEnd)
    msgDecrypte = ""
    for x in range(len(msgclaire)):
        msgDecrypte = msgDecrypte + encodage(msgclaire[x],alpha,R1L1,R2L1,R3L1,reflecteur,R1L2,R2L2,R3L2)
        print(msgDecrypte)
        if (K3 == 26):
            K1 = 0
            K2 = 0
            K3 = 0
        if(K1 <= 25):
            print("oui k1 <= 25")
            if(key1[0] == "R1"):
                R1L1 = configRotor(key1,R1L1)
                R1L2 = configRotor(key1,R1L2)
                K1 = K1 + 1
            elif(key1[0] == "R2"):
                R2L1 = configRotor(key1,R2L1)
                R2L2 = configRotor(key1,R2L2)
                K1 = K1 + 1
            else:
                R3L1 = configRotor(key1,R3L1)
                R3L2 = configRotor(key1,R3L2)
                K1 = K1 + 1
        else:
            if( K2 <= 25):
                if(key2[0] == "R1"):
                    R1L1 = configRotor(key2,R1L1)
                    R1L2 = configRotor(key2,R1L2)
                    K2 = K2 + 1
                elif(key2[0] == "R2"):
                    R2L1 = configRotor(key2,R2L1)
                    R2L2 = configRotor(key2,R2L2)
                    K2 = K2 + 1
                else:
                    R3L1 = configRotor(key2,R3L1)
                    R3L2 = configRotor(key2,R3L2)
                    K2 = K2 + 1
            else:
                if( K3 <= 25):
                    if(key3[0] == "R1"):
                        R1L1 = configRotor(key3,R1L1)
                        R1L2 = configRotor(key3,R1L2)
                        K3 = K3 + 1
                    elif(key3[0] == "R2"):
                        R2L1 = configRotor(key3,R2L1)
                        R2L2 = configRotor(key3,R2L2)
                        K3 = K3 + 1
                    else:
                        R3L1 = configRotor(key3,R3L1)
                        R1L2 = configRotor(key3,R3L2)
                        K3 = K3 + 1  
        print("voici le msg décrypté",msgDecrypte)









"""s = ""
for x in range(len(msgclaire)): 
    s = s + encodage(msgclaire[x],alpha,R1L1,R2L1,R3L1,reflecteur,R1L2,R2L2,R3L2)
print(s)"""









"""import tkinter as tk
#from fonctions import *
def envoi(event, lst_entry):
    for entry in lst_entry:
        print(entry.get())
 
 
root = tk.Tk()
root.title("test")
tk.Label(root, text="nom: ").grid(row=0, column=0)
tk.Label(root, text="prenom: ").grid(row=1, column=0)
entries = []
for i in range(2):
    entree = tk.Entry(root)
    entree.grid(row=i, column=1)
    entries.append(entree)
root.bind("<Return>", lambda event: envoi(event, entries))
root.mainloop()"""

