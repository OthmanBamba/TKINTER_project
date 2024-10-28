import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Classe pour la fenêtre de connexion
class LoginFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # Créer une toile pour l'image de fond
        self.canvas = tk.Canvas(self, width=800, height=533)
        self.canvas.pack(fill="both", expand=True)

        # Charger l'image de fond
        self.load_background_image()

        # Créer les widgets de la fenêtre de connexion
        self.create_widgets()

        # Lier l'événement de redimensionnement à la méthode de redimensionnement de l'image
        self.master.bind("<Configure>", self.resize_background)

    def load_background_image(self):
        try:
            # Remplacez le chemin par le chemin de votre image
            self.original_bg_image = Image.open("/Users/benothmane/Desktop/TKINTER_Project/maison_exterieur_1.jpg")
            self.bg_photo = ImageTk.PhotoImage(self.original_bg_image)

            # Afficher l'image de fond sur le canvas
            self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        except Exception as e:
            print(f"Erreur lors du chargement de l'image : {e}")

    def resize_background(self, event):
        try:
            # Redimensionner l'image de fond pour qu'elle couvre toute la fenêtre
            resized_image = self.original_bg_image.resize((event.width, event.height), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(resized_image)
            self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        except Exception as e:
            print(f"Erreur lors du redimensionnement de l'image : {e}")

    def create_widgets(self):
        # Titre de la fenêtre de connexion
        title_label = tk.Label(self, text="Connexion", font=("Arial", 24), bg="#2c3e50", fg="white")  
        title_label.place(relx=0.5, rely=0.2, anchor="center")

        # Créer un cadre pour les champs de connexion
        form_frame = tk.Frame(self, bg="#2c3e50", bd=0)  
        form_frame.place(relx=0.5, rely=0.4, anchor="center", relwidth=0.8, relheight=0.5)

        # Champ Identifiant
        self.username_label = tk.Label(form_frame, text="Identifiant :", bg="#2c3e50", fg="white")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(form_frame, font=("Arial", 14), bg="white", fg="black")
        self.username_entry.pack(pady=5)

        # Champ Mot de passe
        self.password_label = tk.Label(form_frame, text="Mot de passe :", bg="#2c3e50", fg="white")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(form_frame, show='*', font=("Arial", 14), bg="white", fg="black")
        self.password_entry.pack(pady=5)

        # Bouton de connexion
        self.login_button = tk.Button(form_frame, text="Se connecter", command=self.login, bg="#5cb85c", fg="white")
        self.login_button.pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Logique d'authentification (exemple simple)
        if username == "admin" and password == "password":  
            self.master.show_main_app()  # Accéder à l'application principale
        else:
            messagebox.showerror("Erreur", "Identifiant ou mot de passe incorrect")


# Classe principale de l'application
class RealEstateManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion de Projet Immobilier")
        self.geometry("800x533")
        self.configure(bg="#f0f0f0")

        # Créer la fenêtre de connexion
        self.login_frame = LoginFrame(self)
        self.login_frame.pack(expand=True, fill="both")

        # Créer les frames pour chaque section
        self.frames = {}
        self.create_frames()

    def create_frames(self):
        # Création des autres frames
        self.frames["Home"] = self.create_dashboard_frame()
        self.frames["Properties"] = self.create_properties_frame()
        self.frames["Documents"] = self.create_documents_frame()
        self.frames["Finances"] = self.create_finances_frame()
        self.frames["Tasks"] = self.create_tasks_frame()
        self.frames["Reports"] = self.create_reports_frame()
        self.frames["Settings"] = self.create_settings_frame()

        # Ajouter les frames à la zone de contenu
        for frame in self.frames.values():
            frame.pack_forget()  # Masquer toutes les frames au départ

    def show_main_app(self):
        # Masquer la fenêtre de connexion
        self.login_frame.pack_forget()

        # Créer et afficher la barre latérale
        self.create_sidebar()

        # Afficher le tableau de bord par défaut
        self.show_frame("Home")

    def create_sidebar(self):
        # Création de la barre latérale
        self.sidebar = tk.Frame(self, bg="#2c3e50", width=250)
        self.sidebar.pack(side="left", fill="y")

        # Boutons de la barre latérale
        sections = [
            ("Accueil", "Home"),
            ("Propriétés", "Properties"),
            ("Documents", "Documents"),
            ("Finances", "Finances"),
            ("Tâches", "Tasks"),
            ("Rapports", "Reports"),
            ("Paramètres", "Settings")
        ]
        
        for section, frame_name in sections:
            btn = tk.Button(self.sidebar, text=section, bg="#34495e", fg="blue", 
                            relief="flat", font=("Arial", 12), padx=10, pady=5, anchor="w",
                            command=lambda frame=frame_name: self.show_frame(frame))
            btn.pack(fill="x", pady=2)

        # Bouton de déconnexion
        self.logout_button = tk.Button(self.sidebar, text="Déconnexion", bg="#c0392b", fg="gray",
                                        relief="flat", font=("Arial", 12), padx=10, pady=5, anchor="w",
                                        command=self.logout)
        self.logout_button.pack(fill="x", pady=2)

    def logout(self):
        # Masquer toutes les frames de l'application principale
        for frame in self.frames.values():
            frame.pack_forget()
        # Afficher à nouveau la fenêtre de connexion
        self.login_frame.pack(expand=True, fill="both")
        self.sidebar.pack_forget()  # Assurez-vous que la sidebar est masquée

    def show_frame(self, frame_name):
        # Afficher la frame demandée et masquer les autres
        for frame in self.frames.values():
            frame.pack_forget()  # Masquer toutes les frames
        self.frames[frame_name].pack(expand=True, fill="both")  # Afficher la frame demandée

    def create_dashboard_frame(self):
        # Frame pour le tableau de bord
        frame = tk.Frame(self, bg="white")
        frame.pack(fill="both", expand=True)  # Remplir toute la zone de la fenêtre principale

        # Charger l'image de fond pour le tableau de bord
        self.background_image = Image.open("/Users/benothmane/Desktop/TKINTER_Project/Ophelia Apartments 22.jpg")
        self.bg_photo = ImageTk.PhotoImage(self.background_image)
        background_label = tk.Label(frame, image=self.bg_photo)
        background_label.place(relwidth=1, relheight=1)

        # Message de bienvenue sans fond (ou avec une couleur spécifique)
        welcome_label = tk.Label(frame, text="Bienvenue sur votre tableau de bord", 
                                 font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#2c3e50")  # Changement ici
        welcome_label.pack(pady=20)

        # Créer les cartes de tableau de bord
        card_frame = tk.Frame(frame, bg="#f0f0f0")
        card_frame.pack(pady=20)

        recent_card = self.create_card(card_frame, "Récent", "Vos éléments récemment ouverts apparaîtront ici.")
        docs_card = self.create_card(card_frame, "Documents", "Vous n'avez ajouté aucun document.")
        bookmarks_card = self.create_card(card_frame, "Favoris", "Ajoutez vos liens favoris ici.")
        folder_card = self.create_card(card_frame, "Dossiers", "Projets")

        # Placement des cartes
        recent_card.pack(side="left", padx=10)
        docs_card.pack(side="left", padx=10)
        bookmarks_card.pack(side="left", padx=10)
        folder_card.pack(side="left", padx=10)

        return frame

    def create_properties_frame(self):
        # Frame pour les propriétés
        frame = tk.Frame(self, bg="#f0f0f0")
        label = tk.Label(frame, text="Gestion des Propriétés", font=("Arial", 20), bg="#f0f0f0")
        label.pack(pady=20)
        return frame

    def create_documents_frame(self):
        # Frame pour les documents
        frame = tk.Frame(self, bg="#f0f0f0")
        label = tk.Label(frame, text="Gestion des Documents", font=("Arial", 20), bg="#f0f0f0")
        label.pack(pady=20)
        return frame

    def create_finances_frame(self):
        # Frame pour les finances
        frame = tk.Frame(self, bg="#f0f0f0")
        label = tk.Label(frame, text="Gestion des Finances", font=("Arial", 20), bg="#f0f0f0")
        label.pack(pady=20)
        return frame

    def create_tasks_frame(self):
        # Frame pour les tâches
        frame = tk.Frame(self, bg="#f0f0f0")
        label = tk.Label(frame, text="Gestion des Tâches", font=("Arial", 20), bg="#f0f0f0")
        label.pack(pady=20)
        return frame

    def create_reports_frame(self):
        # Frame pour les rapports
        frame = tk.Frame(self, bg="#f0f0f0")
        label = tk.Label(frame, text="Gestion des Rapports", font=("Arial", 20), bg="#f0f0f0")
        label.pack(pady=20)
        return frame

    def create_settings_frame(self):
        # Frame pour les paramètres
        frame = tk.Frame(self, bg="#f0f0f0")
        label = tk.Label(frame, text="Paramètres", font=("Arial", 20), bg="#f0f0f0")
        label.pack(pady=20)
        return frame

    def create_card(self, parent, title, content):
        # Créer une carte pour le tableau de bord
        card = tk.Frame(parent, bg="white", bd=2, relief="groove", width=200, height=150)
        title_label = tk.Label(card, text=title, font=("Arial", 14), bg="white", fg="blue")  # Couleur du texte bleue
        title_label.pack(pady=5)
        content_label = tk.Label(card, text=content, font=("Arial", 12), bg="white", fg="blue")  # Couleur du texte bleue
        content_label.pack(pady=5)
        return card


# Exécution de l'application
if __name__ == "__main__":
    app = RealEstateManagementApp()
    app.mainloop()
