class Accessoire(list):
	pass
class Pic(Accessoire):
    """ Un pic peut embrocher un post-it par-dessus les post-it déjà présents
        et libérer le dernier embroché. """
    def embrocher(self,postit):
        #print(f'[Pic] postit {postit} embroché')
        self.append(postit)
    def liberer(self):
        pass
        #return postit

class Bar(Accessoire):
    """ Un bar peut recevoir des plateaux, et évacuer le dernier reçu """
    def recevoir(self,plateau):
        #print(f'[Bar] {plateau} reçu')
        self.append(plateau)
    def evacuer(self):
        pass
        #print(f'[Bar] {commande} évacuée')
        #return plateau

class Serveur:
    def __init__(self,pic,bar,commandes):
        self.pic = pic
        self.bar = bar
        self.commandes =commandes
        print('[Serveur] Prêt pour le service')

    def prendre_commande(self):
        """ Prend une commande et embroche un post-it. """
        for commande in self.commandes[::-1]:
            print(f'[Serveur] Je prends commande de {commande}')
            self.pic.embrocher(commande)
        print('[Serveur] Il n y a plus de commandes à prendre')
        
    def servir(self):
        """ Prend un plateau sur le bar. """
        commandes = self.bar
        #print(commandes)
        for commande in commandes[::-1]:
            print(f'[Serveur] Je sers {commande}')
            

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
            #print("A")
            print(f'[Barman] Je commence la fabrication de {i}')
            print(f'[Barman] Je termine la fabrication de {i}')
            self.bar.recevoir(i)



#Programme principal
def main_prog():
    #await asyncio.gather(
    serveur.prendre_commande()
    barman.preparer()
    serveur.servir()
    
    
if __name__ == '__main__':
    pic = Pic()
    bar = Bar()
    commandes = ["1 pastis", "2 demis", "1 ti-punch + 1 planteur"]
    #commandes = sys.argv[1:]
    barman = Barman(pic,bar)
    serveur = Serveur(pic,bar,commandes)
    main_prog()

