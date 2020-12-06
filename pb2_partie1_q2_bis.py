# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 14:21:57 2020

@author: ua
"""

import sys
import asyncio
class Accessoire(list):
    pass
class Pic(Accessoire):
    """ Un pic peut embrocher un post-it par-dessus les post-it déjà présents
        et libérer le dernier embroché. (le postit représentant une commande à chaque fois contrairement 
        à la question précédente) """
    def embrocher(self,commande):
        print(f'[Pic] postit {commande} embroché')
        self.append(commande)
        print(f'[Pic] Etat = {self}' )
        #print('embrocher')
    def liberer(self, postit):
        print(f'[Pic] Etat = {self}')
        print(f'[Pic] postit {postit} libéré')
        self.pop()
        #return(self)
        #print('liberer')
class Bar(Accessoire):
    """ Un bar peut recevoir des plateaux, et évacuer le dernier reçu """
    def recevoir(self,plateau):
        print(f'[Bar] {plateau} reçu')
        self.append(plateau)
        print(f'[Bar] Etat = {self}' )
        #print('recevoir')
    def evacuer(self,commande):
        
        print(f'[Bar] Etat = {self}')
        print(f'[Bar] {commande} évacuée')
        self.pop()
        #self.append(commande)
        #return(self)
        #print('evacuer')

        
class Serveur:
    def __init__(self,pic,bar,commandes):
        self.pic = pic
        self.bar = bar
        self.commandes = commandes
        print('[Serveur] Prêt pour le service')
    
    def prendre_commande(self):
        """ Prend une commande et embroche un post-it. """
        for commande in self.commandes[::-1]:
            print(f'[Serveur] Je prends commande de {commande}')
            self.pic.embrocher(commande)
        print("[Serveur] Il n'y a plus de commandes à prendre")
        print("plus de commande à prendre")
        #print('prendrecommande')
        #for commande in self.commandes:
        #    await self.pic.liberer(commande)
       

    def servir(self):
        """ Prend un plateau sur le bar. """
        commandes = self.bar
        #print(commandes)
        for commande in commandes[::-1]:
            self.bar.evacuer(commande)
            print(f'[Serveur] Je sers {commande}')
            #print('servir')
        print("[Bar] Etat = []")
        print("Bar est vide")
        
        
class Barman:
    def __init__(self,pic,bar):
        self.pic = pic
        self.bar = bar
        print('[Barman] Prêt pour le service !')
    def preparer(self):
        """ Prend un post-it, prépare la commande et la dépose sur le bar. """
        plateau = self.pic
        #print(plateau)
        
        for i in plateau[::-1] :
            self.pic.liberer(i)
            print(f'[Barman] Je commence la fabrication de {i}')
            print(f'[Barman] Je termine la fabrication de {i}')
            self.bar.recevoir(i)
        #print('preparer')
        print("[Pic] Etat = []")
        print("Pic est vide")
        #await self.bar.evacuer(i)

  
#Programme principal
def main_prog():
    serveur.prendre_commande(),
    barman.preparer(),
    serveur.servir()
    
        

if __name__ == '__main__':
    pic = Pic()
    bar = Bar()
    commandes = ["4 mojito","2 tequila sunrise" ]
    #commandes = sys.argv[1:]
    barman = Barman(pic,bar)
    serveur = Serveur(pic,bar,commandes)
    main_prog()