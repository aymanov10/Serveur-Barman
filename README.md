# Serveur-Barman

Objectif :
Le but est de simuler le fonctionnement d’un bar à cocktails au travers des activités de son serveur et de son barman.
Le contexte
Fonctionnement du bar à cocktails

Le serveur

    Le serveur assure 2 fonctions : prendre les commandes auprès des clients et les transmettre au barman d’une part, apporter les cocktails aux clients d’autre part.
Le barman

    La fonction du barman consiste à préparer les cocktails.

Interactions serveur/barman

Barman et serveur interagissent via 2 accessoires :

    un pic, sur lequel pic le serveur embroche, pour chaque commande, un post-it indiquant une commande, et duquel le barman retire un post-it lorsqu’il est prêt à préparer,

    un bar, bar sur lequel le barman dépose, sur un plateau, les verres préparés, qui sont pris par le serveur à destination des clients.

On considère que pic et bar sont 2 files LIFO.
Attendus

On souhaite disposer d’un programme à qui l’on donne en argument une liste de commandes (une liste de strings), et qui écrit à l’écran les actions réalisées par le barman et le serveur pour les traiter.

