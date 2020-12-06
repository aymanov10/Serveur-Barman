# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 13:28:14 2020

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
    async def embrocher(self,commande):
        await asyncio.sleep(0.01)
        print(f'[Pic] postit {commande} embroché')
        self.append(commande)
        #print(self)
        #print('embrocher')
    async def liberer(self, postit):
        await asyncio.sleep(0.01)
        print(f'[Pic] postit {postit} libéré')
        #return(self)
        #print('liberer')
class Bar(Accessoire):
    """ Un bar peut recevoir des plateaux, et évacuer le dernier reçu """
    async def recevoir(self,plateau):
        await asyncio.sleep(0.01)
        print(f'[Bar] {plateau} reçu')
        self.append(plateau)
        #print('recevoir')
    async def evacuer(self,commande):
        await asyncio.sleep(0.01)
        print(f'[Bar] {commande} évacuée')
        #self.append(commande)
        #return(self)
        #print('evacuer')

        
class Serveur:
    def __init__(self,pic,bar,commandes):
        self.pic = pic
        self.bar = bar
        self.commandes = commandes
        print('[Serveur] Prêt pour le service')
    
    async def prendre_commande(self):
        """ Prend une commande et embroche un post-it. """
        for commande in self.commandes[::-1]:
            await asyncio.sleep(0.5)
            print(f'[Serveur] Je prends commande de {commande}')
            await self.pic.embrocher(commande)
        print("[Serveur] Il n'y a plus de commandes à prendre")
        print("plus de commande à prendre")
        #print('prendrecommande')
        #for commande in self.commandes:
        #    await self.pic.liberer(commande)
       

    async def servir(self):
        """ Prend un plateau sur le bar. """
        commandes = self.bar
        await asyncio.sleep(3)
        #print(commandes)
        for commande in commandes[::-1]:
            await asyncio.sleep(0.01)
            await self.bar.evacuer(commande)
            await asyncio.sleep(0.01)
            print(f'[Serveur] Je sers {commande}')
            #print('servir')
        await asyncio.sleep(1)
        print("Bar est vide")
        
        
class Barman:
    def __init__(self,pic,bar):
        self.pic = pic
        self.bar = bar
        print('[Barman] Prêt pour le service !')
    async def preparer(self):
        """ Prend un post-it, prépare la commande et la dépose sur le bar. """
        await asyncio.sleep(2)
        plateau = self.pic
        #print(plateau)
        
        for i in plateau[::-1] :
            await self.pic.liberer(i)
            print(f'[Barman] Je commence la fabrication de {i}')
            await asyncio.sleep(0.2)
            print(f'[Barman] Je termine la fabrication de {i}')
            await self.bar.recevoir(i)
        #print('preparer')
        print("Pic est vide")
        #await self.bar.evacuer(i)

  
#Programme principal
async def main_prog():
    await asyncio.gather(
    serveur.prendre_commande(),
    barman.preparer(),
    serveur.servir()
    )
        

if __name__ == '__main__':
    pic = Pic()
    bar = Bar()
    commandes = ["6 piña colada", "3 gin fizz"]
    #commandes = sys.argv[1:]
    barman = Barman(pic,bar)
    serveur = Serveur(pic,bar,commandes)
    asyncio.run(main_prog())