class PokerController:
    def __init__(self,joueur):
        self.joueur=[]
        
    def Personaliser_joueur(self,joueur):
        self.nom=nom
   
    
    def Nbr_joueur(self):
        self.joueur=[0,0,0,0]
    
    def Choix_joueur(joueur):
        print("lancer partie=1,creer joueur=n'importe quelle nombre"))
        for i in range(0,4):
           a=int(input("lancer partie=1,creer joueur=0"))
           if a!=1:
               joueur.append(joueur)
           else:
               partie=1
               
    def Lancer_partie():
        if partie=1:
            


            
    def Nbr_joueur(self):
        self.joueur=[Bob,Alice,Carl,Dan]
        
        
    


            
            
class ControllerBase:
    def __init__(self):
        self.joueur = []
        
    def inscrire(self, joueur):
        self.joueur.append(joueur)
        
    def Nbr_joueur(self,joueur):
        return (joueur) 
    
            
        
class ControllerBase:
    def __init__(self):
        self.clients = []
        
    def inscrire(self, client):
        self.clients.append(client)
        
    def avertir(self):
        for client in self.clients:
            client.rafraichir()

class ElementVue(QWidget):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.controller.inscrire(self)
    
    def rafraichir(self):
        print 
