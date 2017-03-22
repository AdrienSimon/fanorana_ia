# -*- coding:Utf-8 -*-
import copy
import sys
from math import *
MAX_LIGNE=4
MAX_COLONNE=8
__CANTAKE__=0
ERASE=0

#             0                    1                  2                    3                    4
#TABLEAU = [[1,1,1,1,0,1,1,1,1],[1,1,1,1,0,1,1,1,1],[1,-1,1,-1,-1,1,-1,1,-1],[-1,-1,-1,-1,0,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1]]
player=-1
ia=1

def csvToTab(csv):

        tab = list(csv)
        for i in range(len(tab)):
                
                if i < len(tab):
                        if tab[i]=="," or tab[i]==";":
                                tab.remove(tab[i])
                                i=i-1

                        
        #print tab
        for i in range(len(tab)):
                if i < len(tab):
                        
                        if tab[i]=="-":
                                #print i
                                tab[i+1]="-1"
                                tab.remove(tab[i])
                                #print "removed:", i+1
                                i=i-1
                                
        tab2=[]
        tableau_intermediaire=[]
        for i in range(len(tab)):
                tableau_intermediaire.append(tab[i])
                if len(tableau_intermediaire)==9:
                        tab2.append(tableau_intermediaire)
                        tableau_intermediaire=[]
                
        #print tab
        #print len(tab)
        #print "expected:",5*9
        
        for k in range(len(tab2)):
        	for l in range(len(tab2[k])):
        		tab2[k][l] = int(tab2[k][l])
        
        return tab2

#test = "0,0,0,0,0,0,0,0,0;0,0,1,0,-1,-1,-1,0,0;0,0,0,0,0,-1,0,0,0;0,0,0,-1,0,0,0,0,0;0,0,0,0,0,0,0,0,0"
#test = "0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,1,0,-1;0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0"
#test = "1,0,0,0,0,0,0,0,0;-1,0,0,0,0,0,0,0,0;-1,0,0,0,0,0,0,0,0;-1,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0"
#test = "-1,0,0,0,0,0,0,0,0;0,-1,0,0,0,0,0,0,0;0,0,-1,0,0,0,0,0,0;0,0,0,1,0,0,0,0,0;0,0,0,0,0,0,0,0,0"
#test="1,1,1,1,0,1,1,1,1;1,1,1,1,0,1,1,1,1;1,-1,1,-1,-1,1,-1,1,-1;-1,-1,-1,-1,0,-1,-1,-1,-1;-1,-1,-1,-1,-1,-1,-1,-1,-1"
#test="1,1,1,1,0,1,1,1,1;1,1,1,1,1,0,1,1,1;1,-1,1,-1,0,1,0,1,-1;-1,-1,-1,-1,0,-1,-1,0,-1;-1,-1,-1,-1,-1,-1,-1,-1,0"
#print test
TABLEAU = csvToTab(sys.argv[1])
#TABLEAU = csvToTab(test)
#print ("======")
#print TABLEAU[0]
#print TABLEAU[1]
#print TABLEAU[2]
#print TABLEAU[3]
#print TABLEAU[4]
#print ("======")


class Etat_jeu:
        def __init__(self,tableau_jeu, profondeur, joueur, value):
            self.tableau_jeu = list(tableau_jeu)
            self.value = value
            self.fils = []
            self.profondeur = profondeur
            self.joueur = joueur


def creer_fils(x_depart, y_depart, x_arrive, y_arrive, ennemi, joueur, tableau, etat_courant,niveau):
    tempo=copy.deepcopy(tableau)
    
    tempo2=copy.deepcopy(tempo)
    global __CANTAKE__
    prendre=0
    prendre2=0
  
    
    if(x_depart-x_arrive == 1):##############################
        if(y_depart-y_arrive == -1):
            x_courant=x_arrive-1
            y_courant=y_arrive+1
            
            x_courant2=x_depart+1
            y_courant2=y_depart-1
            if  y_courant <=8 and x_courant <=4 and y_courant >=0 and x_courant >=0:
                    if tempo[x_courant][y_courant]==ennemi:
                            __CANTAKE__=1
                            prendre=1
                
                            while (y_courant <=8 and x_courant <=4 and y_courant >=0 and x_courant >=0 and tempo[x_courant][y_courant]==ennemi):
                                
                                tempo[x_courant][y_courant]=0
                                x_courant=x_courant-1
                                y_courant=y_courant+1
            if y_courant2<=8 and x_courant2 <=4 and y_courant2 >=0 and x_courant2 >=0:
                    if tempo2[x_courant2][y_courant2]==ennemi:
                            __CANTAKE__=1
                            prendre2=1
                            
                            while(y_courant2<=8 and x_courant2 <=4 and y_courant2 >=0 and x_courant2 >=0 and tempo2[x_courant2][y_courant2]==ennemi):

                                tempo2[x_courant2][y_courant2]=0
                                x_courant2=x_courant2+1
                                y_courant2=y_courant2+1
                  
            

        elif(y_depart-y_arrive == 0):
            x_courant=x_arrive-1
            y_courant=y_arrive

            x_courant2=x_depart+1
            y_courant2=y_depart

            if y_courant2<=8 and x_courant2 <=4 and y_courant2 >=0 and x_courant2 >=0:
                    if tempo2[x_courant2][y_courant2]==ennemi:
                            __CANTAKE__=1
                            prendre2=1
                            
                            while(y_courant2<=8 and x_courant2 <=4 and y_courant2 >=0 and x_courant2 >=0 and tempo2[x_courant2][y_courant2]==ennemi):

                                tempo2[x_courant2][y_courant2]=0
                                x_courant2=x_courant2+1
                                y_courant2=y_courant2
            
            if  y_courant <=8 and x_courant <=4 and y_courant >=0 and x_courant >=0:
                    if tempo[x_courant][y_courant]==ennemi:
                            __CANTAKE__=1
                            prendre=1
                            while (y_courant <=8 and x_courant <=4 and y_courant >=0 and x_courant >=0 and tempo[x_courant][y_courant]==ennemi):
                                tempo[x_courant][y_courant]=0
                                x_courant=x_courant-1
                                y_courant=y_courant

                

        elif (y_depart-y_arrive == 1):
            x_courant=x_arrive-1
            y_courant=y_arrive-1

            x_courant2=x_depart+1
            y_courant2=y_depart+1

            if y_courant2<=8 and x_courant2 <=4 and y_courant2 >=0 and x_courant2 >=0:
                    if tempo2[x_courant2][y_courant2]==ennemi:
                            __CANTAKE__=1
                            prendre2=1
                            
                            while(y_courant2<=8 and x_courant2 <=4 and y_courant2 >=0 and x_courant2 >=0 and tempo2[x_courant2][y_courant2]==ennemi):

                                tempo2[x_courant2][y_courant2]=0
                                x_courant2=x_courant2+1
                                y_courant2=y_courant2+1
            
                            if  y_courant <=8 and x_courant <=4 and y_courant >=0 and x_courant >=0:
                                    if tempo[x_courant][y_courant]==ennemi:
                                            __CANTAKE__=1
                                            prendre=1
                            while (y_courant <=8 and x_courant <=4 and y_courant >=0 and x_courant >=0 and tempo[x_courant][y_courant]==ennemi):
                                tempo[x_courant][y_courant]=0
                                x_courant=x_courant-1
                                y_courant=y_courant-1
            
    elif (x_depart-x_arrive == -1):#######################

        if(y_depart-y_arrive == -1):
                
            x_courant=x_arrive+1
            y_courant=y_arrive+1

            x_courant2=x_depart-1
            y_courant2=y_depart-1

            if y_courant2<=8 and x_courant2 <=4 and y_courant2 >=0 and x_courant2 >=0:
                    if tempo2[x_courant2][y_courant2]==ennemi:
                            __CANTAKE__=1
                            prendre2=1
                            
                            while(y_courant2<=8 and x_courant2 <=4 and y_courant2 >=0 and x_courant2 >=0 and tempo2[x_courant2][y_courant2]==ennemi):

                                tempo2[x_courant2][y_courant2]=0
                                x_courant2=x_courant2-1
                                y_courant2=y_courant2-1
            
            if  y_courant <=8 and x_courant <=4 and y_courant >=0 and x_courant >=0:
                    if tempo[x_courant][y_courant]==ennemi:
                            __CANTAKE__=1
                            prendre=1
                            while (y_courant <=8 and x_courant <=4 and y_courant >=0 and x_courant >=0 and tempo[x_courant][y_courant]==ennemi):
                                tempo[x_courant][y_courant]=0
                                x_courant=x_courant+1
                                y_courant=y_courant+1

        elif(y_depart-y_arrive == 0):
            x_courant=x_arrive+1
            y_courant=y_arrive

            x_courant2=x_depart-1
            y_courant2=y_depart

            if y_courant2<=8 and x_courant2 <=4 and y_courant2 >=0 and x_courant2 >=0:
                    if tempo2[x_courant2][y_courant2]==ennemi:
                            __CANTAKE__=1
                            prendre2=1
                            
                            while(y_courant2<=8 and x_courant2 <=4 and y_courant2 >=0 and x_courant2 >=0 and tempo2[x_courant2][y_courant2]==ennemi):

                                tempo2[x_courant2][y_courant2]=0
                                x_courant2=x_courant2-1
                                y_courant2=y_courant2
            if  y_courant <=8 and x_courant <=4 and y_courant >=0 and x_courant >=0:
                    if tempo[x_courant][y_courant]==ennemi:
                            __CANTAKE__=1
                            prendre=1
                    while (y_courant <=8 and x_courant <=4 and y_courant >=0 and x_courant >=0 and tempo[x_courant][y_courant]==ennemi):
                        tempo[x_courant][y_courant]=0
                        x_courant=x_courant+1
                        y_courant=y_courant

        elif (y_depart-y_arrive == 1):
            x_courant=x_arrive+1
            y_courant=y_arrive-1

            x_courant2=x_depart-1
            y_courant2=y_depart+1

            if y_courant2<=8 and x_courant2 <=4 and y_courant2 >=0 and x_courant2 >=0:
                    if tempo2[x_courant2][y_courant2]==ennemi:
                            __CANTAKE__=1
                            prendre2=1
                            
                            while(y_courant2<=8 and x_courant2 <=4 and y_courant2 >=0 and x_courant2 >=0 and tempo2[x_courant2][y_courant2]==ennemi):

                                tempo2[x_courant2][y_courant2]=0
                                x_courant2=x_courant2-1
                                y_courant2=y_courant2+1
            if  y_courant <=8 and x_courant <=4 and y_courant >=0 and x_courant >=0:
                    if tempo[x_courant][y_courant]==ennemi:
                            __CANTAKE__=1
                            prendre=1
                            while (y_courant <=8 and x_courant <=4 and y_courant >=0 and x_courant >=0 and tempo[x_courant][y_courant]==ennemi):
                                tempo[x_courant][y_courant]=0
                                x_courant=x_courant+1
                                y_courant=y_courant-1


    elif (x_depart-x_arrive == 0):#########################
        if(y_depart-y_arrive == -1):
            x_courant=x_arrive
            y_courant=y_arrive+1

            x_courant2=x_depart
            y_courant2=y_depart-1

            if y_courant2<=8 and x_courant2 <=4 and y_courant2 >=0 and x_courant2 >=0:
                    if tempo2[x_courant2][y_courant2]==ennemi:
                            
                            __CANTAKE__=1
                            prendre2=1
                            
                            while(y_courant2<=8 and x_courant2 <=4 and y_courant2 >=0 and x_courant2 >=0 and tempo2[x_courant2][y_courant2]==ennemi):
                           
                                tempo2[x_courant2][y_courant2]=0
                                x_courant2=x_courant2
                                y_courant2=y_courant2-1
            if  y_courant <=8 and x_courant <=4 and y_courant >=0 and x_courant >=0:
                    if tempo[x_courant][y_courant]==ennemi:
                            
                            __CANTAKE__=1
                            prendre=1
                          
                            while (y_courant <=8 and x_courant <=4 and y_courant >=0 and x_courant >=0 and tempo[x_courant][y_courant]==ennemi):
                                
                                tempo[x_courant][y_courant]=0
                                x_courant=x_courant
                                y_courant=y_courant+1
                
        elif(y_depart-y_arrive == 1):
            x_courant=x_arrive
            y_courant=y_arrive-1

            x_courant2=x_depart
            y_courant2=y_depart+1

            if y_courant2<=8 and x_courant2 <=4 and y_courant2 >=0 and x_courant2 >=0:
                    if tempo2[x_courant2][y_courant2]==ennemi:
                            __CANTAKE__=1
                            prendre2=1
                            
                            while(y_courant2<=8 and x_courant2 <=4 and y_courant2 >=0 and x_courant2 >=0 and tempo2[x_courant2][y_courant2]==ennemi):
                                
                                tempo2[x_courant2][y_courant2]=0
                                x_courant2=x_courant2
                                y_courant2=y_courant2+1
                                
            if  y_courant <=8 and x_courant <=4 and y_courant >=0 and x_courant >=0:
                    if tempo[x_courant][y_courant]==ennemi:
                            __CANTAKE__=1
                            prendre=1
                            while (y_courant <=8 and x_courant <=4 and y_courant >=0 and x_courant >=0 and tempo[x_courant][y_courant]==ennemi):
                                tempo[x_courant][y_courant]=0
                                x_courant=x_courant
                                y_courant=y_courant-1
   # print x_depart, y_depart
    #print x_arrive, y_arrive
    tempo[x_depart][y_depart]=0
    tempo2[x_depart][y_depart]=0
    tempo2[x_arrive][y_arrive]=joueur
    tempo[x_arrive][y_arrive]=joueur
    
    if  prendre==1 and __CANTAKE__==1:
            etat_courant.fils.append(Etat_jeu(tempo,(etat_courant.profondeur)+1, joueur, None))
            
            verif_reprendre(tempo,x_arrive,y_arrive,ennemi,joueur,etat_courant,niveau)
    if prendre2==1 and __CANTAKE__==1:            
            etat_courant.fils.append(Etat_jeu(tempo2,(etat_courant.profondeur)+1,joueur, None))
            
            verif_reprendre(tempo2,x_arrive,y_arrive,ennemi,joueur,etat_courant,niveau)
            #verif_reprendre(tempo,x_arrive,y_arrive,ennemi,joueur,etat_courant)
            #verif_reprendre(tempo2,x_arrive,y_arrive,ennemi,joueur,etat_courant)
                
            
                
            
    if prendre==0 and __CANTAKE__==0:
           etat_courant.fils.append(Etat_jeu(tempo,(etat_courant.profondeur)+1, joueur, 666))
    if prendre2==0 and __CANTAKE__==0:
           etat_courant.fils.append(Etat_jeu(tempo2,(etat_courant.profondeur)+1,joueur, 666))


        

def verif_reprendre(liste,ligne,colonne,ennemi,joueur,etat_courant,niveau):
        
           
        if niveau == 0:
                niveau = niveau +1
                if ligne>=1 and colonne>=1 and colonne<=7 and ligne<=3:
                        
                        for i in range(ligne-1,ligne+2):
                                for j in range(colonne-1,colonne+2):
                                        if liste[i][j]==0:
                                                directionx=ligne-i
                                                directiony=colonne-j
                                                if (ligne+colonne)%2==0 or (i+j)%2==0:
                                                        creer_fils(ligne,colonne,i,j,ennemi,joueur,liste,etat_courant,niveau)
                                                        
                
                else:
                            if ligne==0:
                                if colonne==0:     ####### COIN HAUT GAUCHE
                                    if liste[ligne+1][colonne+1]==0:
                                       # print ("Déplacement possible!=====")
                             
                                        if (ligne+colonne)%2==0 or (ligne+1+colonne+1)%2==0:
                                                
                                                creer_fils(ligne, colonne, ligne+1, colonne+1, ennemi, joueur, liste, etat_courant,niveau)
                                    if liste[ligne+1][colonne]==0:
                                        #print ("Déplacement possible!=====")
                                    
                                        if (ligne+colonne)%2==0 or (ligne+1+colonne)%2==0:
                                                creer_fils(ligne, colonne, ligne+1, colonne, ennemi, joueur, liste, etat_courant,niveau)
                                    if liste[ligne][colonne+1]==0:
                                       # print ("Déplacement possible!=====")
                                 
                                        if (ligne+colonne)%2==0 or (ligne+colonne+1)%2==0:
                                                creer_fils(ligne, colonne, ligne, colonne+1, ennemi, joueur, liste, etat_courant,niveau)
                                elif colonne ==MAX_COLONNE:######## COIN HAUT DROIT
                                    if liste[ligne+1][colonne-1]==0:
                                        #print ("Déplacement possible!=====")
                                  
                                        if (ligne+colonne)%2==0 or (ligne+1+colonne-1)%2==0:
                                                creer_fils(ligne, colonne, ligne+1, colonne-1, ennemi, joueur, liste, etat_courant,niveau)
                                    if liste[ligne+1][colonne]==0:
                                       # print ("Déplacement possible!=====")

                                        if (ligne+colonne)%2==0 or (ligne+1+colonne+1)%2==0:
                                                creer_fils(ligne, colonne, ligne+1, colonne, ennemi, joueur, liste, etat_courant,niveau)
                                    if liste[ligne][colonne-1]==0:
                                        #print ("Déplacement possible!=====")
                         
                                        if (ligne+colonne)%2==0 or (ligne+colonne-1)%2==0:
                                                creer_fils(ligne, colonne, ligne, colonne-1, ennemi, joueur, liste, etat_courant,niveau)
                                else:
                                    for ligne_entourage in range(ligne,ligne+2):
                                        for colonne_entourage in range(colonne-1, colonne+2):
                                            if liste[ligne_entourage][colonne_entourage]==0:
                                                #print ("Déplacement possible!====")
                                      
                                                if (ligne+colonne)%2==0 or (ligne_entourage+colonne_entourage)%2==0:
                                                        creer_fils(ligne, colonne, ligne_entourage, colonne_entourage, ennemi, joueur, liste, etat_courant,niveau)
                                    
                            elif ligne==MAX_LIGNE:
                                if colonne==0:     ####### COIN BAS GAUCHE
                                    
                                    if liste[ligne-1][colonne]==0:
                                        #print ("Déplacement possible!=====")
                       
                                        if (ligne+colonne)%2==0 or (ligne-1+colonne)%2==0:
                                                creer_fils(ligne, colonne, ligne-1, colonne, ennemi, joueur, liste, etat_courant,niveau)
                                    if liste[ligne][colonne+1]==0:
                                        #print ("Déplacement possible!=====") 
                       
                                        if (ligne+colonne)%2==0 or (ligne+colonne+1)%2==0:
                                                creer_fils(ligne, colonne, ligne, colonne+1, ennemi, joueur, liste, etat_courant,niveau)
                                    if liste[ligne-1][colonne+1]==0:
                                        #print ("Déplacement possible!=====")
                                   
                                        if (ligne+colonne)%2==0 or (ligne-1+colonne+1)%2==0:
                                                creer_fils(ligne, colonne, ligne-1, colonne+1, ennemi, joueur, liste, etat_courant,niveau)
                                elif colonne ==MAX_COLONNE:######## COIN BAS DROIT
                                    if liste[ligne-1][colonne]==0:
                                        #print ("Déplacement possible!=====")
               
                                        if (ligne+colonne)%2==0 or (ligne-1+colonne)%2==0:
                                                creer_fils(ligne, colonne, ligne-1, colonne, ennemi, joueur, liste, etat_courant,niveau)
                                    
                                    if liste[ligne][colonne-1]==0:
                                        #print ("Déplacement possible!=====")
                     
                                        if (ligne+colonne)%2==0 or (ligne+colonne-1)%2==0:
                                                creer_fils(ligne, colonne, ligne, colonne-1, ennemi, joueur, liste, etat_courant,niveau)
                                    
                                    if liste[ligne-1][colonne-1]==0:
                                        #print ("Déplacement possible!=====")
                       
                                        if (ligne+colonne)%2==0 or (ligne-1+colonne-1)%2==0:
                                                creer_fils(ligne, colonne, ligne-1, colonne-1, ennemi, joueur, liste, etat_courant,niveau)
                                

                                                    
                                
                            else:
                                if colonne==0:
                                    for ligne_entourage in range(ligne-1,ligne+2):
                                        for colonne_entourage in range(colonne, colonne+2):
                                            if liste[ligne_entourage][colonne_entourage]==0:
                                                #print ("Déplacement possible!====")
                                              
                                                if (ligne+colonne)%2==0 or (ligne_entourage+colonne_entourage)%2==0:
                                                        creer_fils(ligne, colonne, ligne_entourage, colonne_entourage, ennemi, joueur, liste, etat_courant,niveau)
                                                


                                
                                if colonne==MAX_COLONNE:
                                    for ligne_entourage in range(ligne-1,ligne+2):
                                        for colonne_entourage in range(colonne-1, colonne+1):
                                            if liste[ligne_entourage][colonne_entourage]==0:
                                           
                                                if (ligne+colonne)%2==0 or (ligne_entourage+colonne_entourage)%2==0:
                                                        creer_fils(ligne, colonne, ligne_entourage, colonne_entourage, ennemi, joueur, liste, etat_courant,niveau)
                                                  
                        
def lister_cas(liste, etat_courant, joueur, ennemi, suppr):
    global __CANTAKE__
    
  
    for ligne in range(MAX_LIGNE+1):
  
        for colonne in range(MAX_COLONNE+1):
            if liste[ligne][colonne]==joueur:
                    
            
                
                #print ("===============PION IA TROUVEE===================")
                #print ("coordonnée:")
                #print ligne, colonne
               # print ("====")
                if colonne >= 1 and ligne >= 1 and colonne <= 7 and ligne <= 3:
                    
                    for ligne_entourage in range(ligne-1,ligne+2):          # ON PARCOURS LE SOUS TABLEAU QUI REPRESENTE LE POINT ET SON ENTOURAGE
                        for colonne_entourage in range(colonne-1,colonne+2):
                            if liste[ligne_entourage][colonne_entourage]==0: #// Déplacement possible
                               # print ("Déplacement possible!=====")
                               # print ligne, colonne
                               # print ("vers")
                               # print ligne_entourage, colonne_entourage
                           
                                if (ligne+colonne)%2==0 or (ligne_entourage+colonne_entourage)%2==0:
                                        creer_fils(ligne, colonne, ligne_entourage, colonne_entourage, ennemi, joueur, etat_courant.tableau_jeu, etat_courant,0)
                            
                else:
                    if ligne==0:
                        if colonne==0:     ####### COIN HAUT GAUCHE
                            if liste[ligne+1][colonne+1]==0:
                               # print ("Déplacement possible!=====")
                            
                                if (ligne+colonne)%2==0 or (ligne+1+colonne+1)%2==0:
                                        
                                        creer_fils(ligne, colonne, ligne+1, colonne+1, ennemi, joueur, liste, etat_courant,0)
                            if liste[ligne+1][colonne]==0:
                                #print ("Déplacement possible!=====")
                          
                                if (ligne+colonne)%2==0 or (ligne+1+colonne)%2==0:
                                        creer_fils(ligne, colonne, ligne+1, colonne, ennemi, joueur, liste, etat_courant,0)
                            if liste[ligne][colonne+1]==0:
                               # print ("Déplacement possible!=====")
                     
                                if (ligne+colonne)%2==0 or (ligne+colonne+1)%2==0:
                                        creer_fils(ligne, colonne, ligne, colonne+1, ennemi, joueur, liste, etat_courant,0)
                        elif colonne ==MAX_COLONNE:######## COIN HAUT DROIT
                            if liste[ligne+1][colonne-1]==0:
                                #print ("Déplacement possible!=====")
      
                                if (ligne+colonne)%2==0 or (ligne+1+colonne-1)%2==0:
                                        creer_fils(ligne, colonne, ligne+1, colonne-1, ennemi, joueur, liste, etat_courant,0)
                            if liste[ligne+1][colonne]==0:
                               # print ("Déplacement possible!=====")
                           
                                if (ligne+colonne)%2==0 or (ligne+1+colonne+1)%2==0:
                                        creer_fils(ligne, colonne, ligne+1, colonne, ennemi, joueur, liste, etat_courant,0)
                            if liste[ligne][colonne-1]==0:
                                #print ("Déplacement possible!=====")
                      
                                if (ligne+colonne)%2==0 or (ligne+colonne-1)%2==0:
                                        creer_fils(ligne, colonne, ligne, colonne-1, ennemi, joueur, liste, etat_courant,0)
                        else:
                            for ligne_entourage in range(ligne,ligne+2):
                                for colonne_entourage in range(colonne-1, colonne+2):
                                    if liste[ligne_entourage][colonne_entourage]==0:
                                        #print ("Déplacement possible!====")
                               
                                        if (ligne+colonne)%2==0 or (ligne_entourage+colonne_entourage)%2==0:
                                                creer_fils(ligne, colonne, ligne_entourage, colonne_entourage, ennemi, joueur, liste, etat_courant,0)
                            
                    elif ligne==MAX_LIGNE:
                        if colonne==0:     ####### COIN BAS GAUCHE
                            
                            if liste[ligne-1][colonne]==0:
                                #print ("Déplacement possible!=====")
                                
                                if (ligne+colonne)%2==0 or (ligne-1+colonne)%2==0:
                                        creer_fils(ligne, colonne, ligne-1, colonne, ennemi, joueur, liste, etat_courant,0)
                            if liste[ligne][colonne+1]==0:
                                #print ("Déplacement possible!=====") 
              
                                if (ligne+colonne)%2==0 or (ligne+colonne+1)%2==0:
                                        creer_fils(ligne, colonne, ligne, colonne+1, ennemi, joueur, liste, etat_courant,0)
                            if liste[ligne-1][colonne+1]==0:
                                #print ("Déplacement possible!=====")
                            
                                if (ligne+colonne)%2==0 or (ligne-1+colonne+1)%2==0:
                                        creer_fils(ligne, colonne, ligne-1, colonne+1, ennemi, joueur, liste, etat_courant,0)
                        elif colonne ==MAX_COLONNE:######## COIN BAS DROIT
                            if liste[ligne-1][colonne]==0:
                                #print ("Déplacement possible!=====")
                              
                                if (ligne+colonne)%2==0 or (ligne-1+colonne)%2==0:
                                        creer_fils(ligne, colonne, ligne-1, colonne, ennemi, joueur, liste, etat_courant,0)
                            
                            if liste[ligne][colonne-1]==0:
                                #print ("Déplacement possible!=====")
                           
                                if (ligne+colonne)%2==0 or (ligne+colonne-1)%2==0:
                                        creer_fils(ligne, colonne, ligne, colonne-1, ennemi, joueur, liste, etat_courant,0)
                            
                            if liste[ligne-1][colonne-1]==0:
                                #print ("Déplacement possible!=====")
                            
                                if (ligne+colonne)%2==0 or (ligne-1+colonne-1)%2==0:
                                        creer_fils(ligne, colonne, ligne-1, colonne-1, ennemi, joueur, liste, etat_courant,0)

                        else:
                            for ligne_entourage in range(ligne-1,ligne+1):
                                for colonne_entourage in range(colonne-1, colonne+2):
                                    if liste[ligne_entourage][colonne_entourage]==0:
                                        #print ("Déplacement possible!====")
                     
                                        if (ligne+colonne)%2==0 or (ligne_entourage+colonne_entourage)%2==0:
                                                creer_fils(ligne, colonne, ligne_entourage, colonne_entourage, ennemi, joueur, liste, etat_courant,0)
                                                				
                        

                                            
                        
                    else:
                        if colonne==0:
                            for ligne_entourage in range(ligne-1,ligne+2):
                                for colonne_entourage in range(colonne, colonne+2):
                                    if liste[ligne_entourage][colonne_entourage]==0:
                                        #print ("Déplacement possible!====")
                             
                                        if (ligne+colonne)%2==0 or (ligne_entourage+colonne_entourage)%2==0:
                                                creer_fils(ligne, colonne, ligne_entourage, colonne_entourage, ennemi, joueur, liste, etat_courant,0)
                                        


                        
                        if colonne==MAX_COLONNE:
                            for ligne_entourage in range(ligne-1,ligne+2):
                                for colonne_entourage in range(colonne-1, colonne+1):
                                    if liste[ligne_entourage][colonne_entourage]==0:
                                        #print ("Déplacement possible!====")
                                      
                                        if (ligne+colonne)%2==0 or (ligne_entourage+colonne_entourage)%2==0:
                                                creer_fils(ligne, colonne, ligne_entourage, colonne_entourage, ennemi, joueur, liste, etat_courant,0)
                                        


                        
                
                    #print ("================FIN PION IA====================")
    #print("==Nombre de pion IA:")
    #print nb_pion_IA
    #print("==Nombre de possibilité IA:")
    #print nb_possibilite
    #print "ANCIEN ETAT"
    #print liste[0]
    #print liste[1]
    #print liste[2]
    #print liste[3]
    #print liste[4]

    if __CANTAKE__==1:
            if __CANTAKE__==1:
                    test=0
                    #print __CANTAKE__
                
                    while test < (len(etat_courant.fils)):
                                  #print test
                                  if etat_courant.fils[test].value==666:
                                      #print "removed"
                                     # print test
                                      #print etat_courant.fils[test].profondeur
                                      etat_courant.fils.remove(etat_courant.fils[test])
                                      test=test-1
                                  test=test+1
                            
    __CANTAKE__=0

    
def tabToCsv(tab):
        csv = ""
        for i in range(len(tab)):
                for j in range(len(tab[i])):
                        csv=csv+str(tab[i][j])
                        if j!=8:
                                csv=csv+","
                if i!=4:        
                        csv=csv+";"
  
        return csv



    
racine = Etat_jeu(list(TABLEAU),0,player,None)                           
lister_cas(list(racine.tableau_jeu), racine, ia , player,1)
for i in range(len(racine.fils)):
    #print "NEW ETAT"
    #print racine.fils[i].tableau_jeu[0]
    #print racine.fils[i].tableau_jeu[1]
    #print racine.fils[i].tableau_jeu[2]
    #print racine.fils[i].tableau_jeu[3]
    #print racine.fils[i].tableau_jeu[4]
    #print "###############################"
    courant=racine.fils[i]
    lister_cas(list(racine.fils[i].tableau_jeu), racine.fils[i], player, ia,1)
    
for i in range(len(racine.fils)):
    for y in range(len(racine.fils[i].fils)):
        #print "####"
        #print racine.fils[i].fils[y].tableau_jeu[0]
        #print racine.fils[i].fils[y].tableau_jeu[1]
        #print racine.fils[i].fils[y].tableau_jeu[2]
        #print racine.fils[i].fils[y].tableau_jeu[3]
        #print racine.fils[i].fils[y].tableau_jeu[4]
        #print "###############################"
        lister_cas(list(racine.fils[i].fils[y].tableau_jeu), racine.fils[i].fils[y], ia, player,1)

compteurun=0
compteurdeux=0
temporaire=-9999
for i in range(len(racine.fils)):
    for y in range(len(racine.fils[i].fils)):
            for z in range(len(racine.fils[i].fils[y].fils)):
                compteurun=0
                compteurdeux=0
                for parcoursX in range(5):
                         
                            for parcoursY in range(9):
                
                                    if racine.fils[i].fils[y].fils[z].tableau_jeu[parcoursX][parcoursY] == ia:
                                            compteurun=compteurun+1
                                    elif racine.fils[i].fils[y].fils[z].tableau_jeu[parcoursX][parcoursY] == player:
                                           compteurdeux=compteurdeux+1
                                           
                if compteurdeux==0:
                        racine.fils[i].fils[y].fils[z].value=9999
                else:
                        racine.fils[i].fils[y].fils[z].value=float(compteurun-compteurdeux)
                

for i in range(len(racine.fils)):
    for y in range(len(racine.fils[i].fils)):
            temporaire=-9999
            for z in range(len(racine.fils[i].fils[y].fils)):
                    
                   # if racine.fils[i].fils[y].fils[z].value==666:
                           # print"alert"
                        
                    if (racine.fils[i].fils[y].fils[z].value)>temporaire:
                            
                            temporaire=racine.fils[i].fils[y].fils[z].value
            racine.fils[i].fils[y].value=temporaire
             
            
for i in range(len(racine.fils)):
    temporaire=9999
    for y in range(len(racine.fils[i].fils)):
          #  if racine.fils[i].fils[y].value==666:
                           # print"alert"
            if racine.fils[i].fils[y].value<temporaire:
                    temporaire=racine.fils[i].fils[y].value
    racine.fils[i].value=temporaire

for i in range(len(racine.fils)):
        if racine.fils[i].value >= temporaire:
                temporaire=racine.fils[i].value
                final=racine.fils[i].tableau_jeu
        #print "============================>",racine.fils[i].value
        #print "============================>Valeur des fils:"
        #for j in range(len(racine.fils[i].fils)):
        #        print"=======>", racine.fils[i].fils[j].value
        #        print"=======>Valeur des fils:"
        #        for y in range(len(racine.fils[i].fils[j].fils)):
        #                print"=>", racine.fils[i].fils[j].fils[y].value
#print TABLEAU[0]
#print TABLEAU[1]
#print TABLEAU[2]
#print TABLEAU[3]
#print TABLEAU[4]
#print("=============")

#print final[0]
#print final[1]
#print final[2]
#print final[3]
#print final[4]

#print ("============")
print tabToCsv(final)

#////////-1-1//-1 0//-1+1   //=8 voisins

#////////0 -1// i j // 0+1

#////////+1-1//+1 0//+1+1


#1,1,1,1,1,1,1,1,1,1,1;0,0,0,0,0,0,0,0,0;1,1,1,1,1,1,1,1,1,1,1;
#LE POINT VIRGULE EST UNE NOUVELLE LIGNE     if (x_depart-x_arrive == 1):
            

        



