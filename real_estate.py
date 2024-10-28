import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from PIL import Image, ImageTk

# Classe pour la fenêtre de connexion
class LoginFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # Créer une toile pour l'image de fond
        self.canvas = tk.Canvas(self, width=800, height=533)
        self.canvas.pack(fill="both", expand=True)

        # Charger l'image de fond pour la fenêtre de connexion
        self.load_background_image()

        # Créer les widgets de la fenêtre de connexion
        self.create_widgets()

        # Lier l'événement de redimensionnement à la méthode de redimensionnement de l'image
        self.master.bind("<Configure>", self.resize_background)

    def load_background_image(self):
        try:
            self.original_bg_image = Image.open("maison_exterieur_1.jpg")
            self.bg_photo = ImageTk.PhotoImage(self.original_bg_image)
            self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        except Exception as e:
            print(f"Erreur lors du chargement de l'image : {e}")

    def resize_background(self, event):
        try:
            resized_image = self.original_bg_image.resize((event.width, event.height), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(resized_image)
            self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        except Exception as e:
            print(f"Erreur lors du redimensionnement de l'image : {e}")

    def create_widgets(self):
        title_label = tk.Label(self, text="Connexion", font=("Arial", 24), bg="#2c3e50", fg="white")
        title_label.place(relx=0.5, rely=0.2, anchor="center")

        form_frame = tk.Frame(self, bg="#2c3e50", bd=0)
        form_frame.place(relx=0.5, rely=0.4, anchor="center", relwidth=0.8, relheight=0.5)

        self.username_label = tk.Label(form_frame, text="Identifiant :", bg="#2c3e50", fg="white")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(form_frame, font=("Arial", 14), bg="white", fg="black")
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(form_frame, text="Mot de passe :", bg="#2c3e50", fg="white")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(form_frame, show='*', font=("Arial", 14), bg="white", fg="black")
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(form_frame, text="Se connecter", command=self.login, bg="#5cb85c", fg="white")
        self.login_button.pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":
            self.master.show_main_app()
        else:
            messagebox.showerror("Erreur", "Identifiant ou mot de passe incorrect")


# Classe principale de l'application
class RealEstateManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion de Projet Immobilier")
        self.geometry("800x533")
        self.configure(bg="#f0f0f0")

        self.login_frame = LoginFrame(self)
        self.login_frame.pack(expand=True, fill="both")

        self.frames = {}
        self.properties = []  # Liste pour stocker les propriétés
        self.create_frames()

    def create_frames(self):
        self.frames["Home"] = self.create_dashboard_frame()
        self.frames["PropertyManagement"] = self.create_property_management_frame()
        self.frames["AdvancedSearch"] = self.create_advanced_search_frame()
        self.frames["ManageClients"] = self.create_manage_clients_frame()
        self.frames["ManageDocuments"] = self.create_manage_documents_frame()
        self.frames["ManageFinances"] = self.create_manage_finances_frame()
        self.frames["ManageTasks"] = self.create_manage_tasks_frame()
        self.frames["ManageWorkTypes"] = self.create_manage_work_types_frame()
        self.frames["BudgetManagement"] = self.create_budget_management_frame()
        self.frames["Notifications"] = self.create_notifications_frame()

        for frame in self.frames.values():
            frame.pack_forget()  # Masquer toutes les frames au départ

    def show_main_app(self):
        self.login_frame.pack_forget()
        self.create_sidebar()
        self.show_frame("Home")

    def create_sidebar(self):
        self.sidebar = tk.Frame(self, bg="#2c3e50", width=250)
        self.sidebar.pack(side="left", fill="y")

        sections = [
            ("Accueil", "Home"),
            ("Gestion des Propriétés", "PropertyManagement"),
            ("Recherche Avancée", "AdvancedSearch"),
            ("Gestion des Clients", "ManageClients"),
            ("Gestion des Documents", "ManageDocuments"),
            ("Gestion des Finances", "ManageFinances"),
            ("Gestion des Tâches", "ManageTasks"),
            ("Gestion des Types de Travaux", "ManageWorkTypes"),
            ("Gestion des Budgets", "BudgetManagement"),
            ("Notifications", "Notifications"),
        ]

        for section, frame_name in sections:
            btn = tk.Button(self.sidebar, text=section, bg="#34495e", fg="blue",
                            relief="flat", font=("Arial", 12), padx=10, pady=5, anchor="w",
                            command=lambda frame=frame_name: self.show_frame(frame))
            btn.pack(fill="x", pady=2)

        self.logout_button = tk.Button(self.sidebar, text="Déconnexion", bg="#c0392b", fg="gray",
                                        relief="flat", font=("Arial", 12), padx=10, pady=5, anchor="w",
                                        command=self.logout)
        self.logout_button.pack(fill="x", pady=2)

    def logout(self):
        for frame in self.frames.values():
            frame.pack_forget()
        self.login_frame.pack(expand=True, fill="both")
        self.sidebar.pack_forget()

    def show_frame(self, frame_name):
        for frame in self.frames.values():
            frame.pack_forget()
        self.frames[frame_name].pack(expand=True, fill="both")

    def create_dashboard_frame(self):
        frame = tk.Frame(self, bg="white")
        frame.pack(fill="both", expand=True)

        # Charger l'image de fond pour le tableau de bord
        self.background_image = Image.open("Ophelia Apartments 22.jpg")
        self.bg_photo = ImageTk.PhotoImage(self.background_image)
        background_label = tk.Label(frame, image=self.bg_photo)
        background_label.place(relwidth=1, relheight=1)

        welcome_label = tk.Label(frame, text="Bienvenue sur RealEstateAPP", 
                                 font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#2c3e50")
        welcome_label.pack(pady=20)

        return frame

    def create_property_management_frame(self):
        frame = tk.Frame(self, bg="#f0f0f0")
        frame.pack(fill="both", expand=True)

        label = tk.Label(frame, text="Gestion des Propriétés", font=("Arial", 20), bg="#f0f0f0" , fg="blue")
        label.pack(pady=20)

        # Liste des propriétés
        self.property_listbox = tk.Listbox(frame, font=("Arial", 14), bg="white", selectmode=tk.SINGLE)
        self.property_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        # Boutons pour ajouter, modifier et supprimer des propriétés
        button_frame = tk.Frame(frame, bg="#f0f0f0")
        button_frame.pack(pady=10)

        self.add_property_button = tk.Button(button_frame, text="Ajouter Propriété", command=self.add_property, bg="#5cb85c", fg="white")
        self.add_property_button.pack(side=tk.LEFT, padx=5)

        self.edit_property_button = tk.Button(button_frame, text="Modifier Propriété", command=self.edit_property, bg="#f39c12", fg="white")
        self.edit_property_button.pack(side=tk.LEFT, padx=5)

        self.delete_property_button = tk.Button(button_frame, text="Supprimer Propriété", command=self.delete_property, bg="#c0392b", fg="white")
        self.delete_property_button.pack(side=tk.LEFT, padx=5)

        return frame

    def add_property(self):
        name = simpledialog.askstring("Ajouter Propriété", "Nom de la propriété:")
        if name:
            self.properties.append(name)
            self.property_listbox.insert(tk.END, name)
            messagebox.showinfo("Succès", f"Propriété '{name}' ajoutée avec succès!")

    def edit_property(self):
        selected_index = self.property_listbox.curselection()
        if selected_index:
            current_name = self.property_listbox.get(selected_index)
            new_name = simpledialog.askstring("Modifier Propriété", "Nouveau nom de la propriété:", initialvalue=current_name)
            if new_name:
                self.properties[selected_index[0]] = new_name
                self.property_listbox.delete(selected_index)
                self.property_listbox.insert(selected_index, new_name)
                messagebox.showinfo("Succès", f"Propriété '{current_name}' modifiée en '{new_name}'!")
        else:
            messagebox.showwarning("Avertissement", "Veuillez sélectionner une propriété à modifier.")

    def delete_property(self):
        selected_index = self.property_listbox.curselection()
        if selected_index:
            property_name = self.property_listbox.get(selected_index)
            confirm = messagebox.askyesno("Confirmation", f"Êtes-vous sûr de vouloir supprimer '{property_name}'?")
            if confirm:
                del self.properties[selected_index[0]]
                self.property_listbox.delete(selected_index)
                messagebox.showinfo("Succès", f"Propriété '{property_name}' supprimée avec succès!")
        else:
            messagebox.showwarning("Avertissement", "Veuillez sélectionner une propriété à supprimer.")

    def create_advanced_search_frame(self):
        frame = tk.Frame(self, bg="#f0f0f0")
        label = tk.Label(frame, text="Recherche Avancée", font=("Arial", 20), bg="#f0f0f0" , fg="blue")
        label.pack(pady=20)
        return frame

    def create_manage_clients_frame(self):
        frame = tk.Frame(self, bg="#f0f0f0")
        label = tk.Label(frame, text="Gestion des Clients", font=("Arial", 20), bg="#f0f0f0", fg="blue")
        label.pack(pady=20)
        return frame

    def create_manage_documents_frame(self):
        frame = tk.Frame(self, bg="#f0f0f0")
        label = tk.Label(frame, text="Gestion des Documents", font=("Arial", 20), bg="#f0f0f0" , fg="blue")
        label.pack(pady=20)
        return frame

    def create_manage_finances_frame(self):
        frame = tk.Frame(self, bg="#f0f0f0")
        label = tk.Label(frame, text="Gestion des Finances", font=("Arial", 20), bg="#f0f0f0" , fg="blue")
        label.pack(pady=20)
        return frame

    def create_manage_tasks_frame(self):
        frame = tk.Frame(self, bg="#f0f0f0")
        label = tk.Label(frame, text="Gestion des Tâches", font=("Arial", 20), bg="#f0f0f0" , fg="blue")
        label.pack(pady=20)
        return frame

    def create_manage_work_types_frame(self):
        frame = tk.Frame(self, bg="#f0f0f0")
        label = tk.Label(frame, text="Gestion des Types de Travaux", font=("Arial", 20), bg="#f0f0f0" , fg="blue")
        label.pack(pady=20)
        return frame

    def create_budget_management_frame(self):
        frame = tk.Frame(self, bg="#f0f0f0")
        label = tk.Label(frame, text="Gestion des Budgets", font=("Arial", 20), bg="#f0f0f0" , fg="blue")
        label.pack(pady=20)
        return frame

    def create_notifications_frame(self):
        frame = tk.Frame(self, bg="#f0f0f0")
        label = tk.Label(frame, text="Notifications", font=("Arial", 20), bg="#f0f0f0" , fg="blue")
        label.pack(pady=20)
        return frame


# Lancer l'application
if __name__ == "__main__":
    app = RealEstateManagementApp()
    app.mainloop()
