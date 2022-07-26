# -*- coding: utf-8 -*-

import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import statistics as st
from scipy import stats
from scipy.optimize import curve_fit
from tkinter.filedialog import askopenfilename


# PERMET DE TRACER UN GRAPHE DE SERIE DE POINTS EN CALCULANT L'INCERTITUDE
# DE STUDENT, LA P-VALUE ET LES COEFFICIENTS DE REGRESSION
def graphe():
    for widget in frame.winfo_children():
        widget.destroy()

    def fichier():
        return askopenfilename(initialdir=".",
                               title="Choisir votre fichier",
                               filetypes=(("fichiers texte", "*.txt"),
                                          ("all files", "*.*")))

    data = np.loadtxt(fichier())
    absc = data[:, 0]
    ordo = data[:, 1]
    dx = data[:, 2]
    dy = data[:, 3]

    def graphe():
        labelx = eval(abscisses.get())
        labely = eval(ordonnees.get())
        plt.figure(figsize=(14.2, 7.7))
        plt.errorbar(absc, ordo, dy, dx, ls="",
                     marker='+', color="black", label="f(x)")
        plt.xlabel(labelx)
        plt.ylabel(labely)
        plt.legend()
        plt.grid()
        plt.show()

    # Fonction permettant de calculer les incertitudes selon la méthode de Student
    def delta():
        delta = stats.t.ppf(0.95, df=len(absc))*st.stdev(absc)/np.sqrt(len(absc))
        entree3.delete(0, tk.END)
        entree3.insert(0, delta)

    # Fonction permettant de calculer le coefficient de corrélation de Pearson
    def r2():
        p4 = np.poly1d(np.polyfit(absc, ordo, 1))
        xp = np.linspace(absc.min(), absc.max(), len(absc)*100)
        r2 = stats.linregress(xp, p4(xp)).rvalue**2
        entree2.delete(0, tk.END)
        entree2.insert(0, r2)

    # Fonction permettant de calculer le coefficient de corrélation de Spearman
    def r_s2():
        r_s2 = stats.spearmanr(absc, ordo).correlation
        entree1.delete(0, tk.END)
        entree1.insert(0, r_s2)

    # Fonction permettant de calculer la p-value
    def p():
        p = stats.spearmanr(absc, ordo).pvalue
        entree.delete(0, tk.END)
        entree.insert(0, p)

    texte1 = tk.Label(frame, text="titre x")
    texte1.pack()
    defaut = tk.StringVar()
    defaut.set("'x'")
    abscisses = tk.Entry(frame, width=40, textvariable=defaut)
    abscisses.pack()

    texte2 = tk.Label(frame, text="titre y")
    texte2.pack()
    defaut2 = tk.StringVar()
    defaut2.set("'y'")
    ordonnees = tk.Entry(frame, width=40, textvariable=defaut2)
    ordonnees.pack()

    # AFFICHAGE DES CALCULS
    # affichage de la p_value
    titre = tk.Label(frame, text="p-value")
    titre.pack()
    entree = tk.Entry(frame, width=40)
    entree.pack()
    bouton = tk.Button(frame, text='afficher', command=p)
    bouton.pack()

    # affichage du r_s2
    titre = tk.Label(frame, text="r_s2")
    titre.pack()
    entree1 = tk.Entry(frame, width=40)
    entree1.pack()
    bouton1 = tk.Button(frame, text='afficher', command=r_s2)
    bouton1.pack()

    # affichage du r2
    titre = tk.Label(frame, text="r2")
    titre.pack()
    entree2 = tk.Entry(frame, width=40)
    entree2.pack()
    bouton2 = tk.Button(frame, text='afficher', command=r2)
    bouton2.pack()

    # affichage de l'incertitude de Student
    titre = tk.Label(frame, text="incertitude avec Student")
    titre.pack()
    entree3 = tk.Entry(frame, width=40)
    entree3.pack()
    bouton3 = tk.Button(frame, text='afficher', command=delta)
    bouton3.pack()

    bouton4 = tk.Button(frame, text="tracer", command=graphe)
    bouton4.pack()


# FONCTION PERMETTANT DE CALCULER UNE REGRESSION LINEAIRE A PARTIR D'UNE SERIE DE POINTS
def lineaire():
    for widget in frame.winfo_children():
        widget.destroy()

    def fichier():
        return askopenfilename(initialdir=".",
                               title="Choisir votre fichier",
                               filetypes=(("fichiers texte", "*.txt"),
                                          ("all files", "*.*")))

    data = np.loadtxt(fichier())
    absc = data[:, 0]
    ordo = data[:, 1]
    dx = data[:, 2]
    dy = data[:, 3]

    def graphe():
        (a, b, R2, da, db) = stats.linregress(absc, ordo)
        labelx = eval(abscisses.get())
        labely = eval(ordonnees.get())
        plt.figure(figsize=(14.2, 7.7))
        plt.errorbar(absc, ordo, dy, dx, ls="",
                     marker='+', color="black", label="f(x)")
        plt.plot(absc, a*absc+b, label="régression")
        plt.xlabel(labelx)
        plt.ylabel(labely)
        plt.legend()
        plt.grid()
        plt.show()

    def regression():
        (a, b, R2, da, db) = stats.linregress(absc, ordo)
        entree1.delete(0, tk.END)
        entree1.insert(0, repr((a, b)))

    def incert_regression():
        (a, b, R2, da, db) = stats.linregress(absc, ordo)
        entree2.delete(0, tk.END)
        entree2.insert(0, repr((np.round(da, decimals=4),
                                np.round(db, decimals=4))))

    def r_s2():
        r_s2 = stats.spearmanr(absc, ordo).correlation
        entree3.delete(0, tk.END)
        entree3.insert(0, r_s2)

    texte1 = tk.Label(frame, text="titre x")
    texte1.pack()
    defaut = tk.StringVar()
    defaut.set("'x'")
    abscisses = tk.Entry(frame, width=40, textvariable=defaut)
    abscisses.pack()

    texte2 = tk.Label(frame, text="titre y")
    texte2.pack()
    defaut2 = tk.StringVar()
    defaut2.set("'y'")
    ordonnees = tk.Entry(frame, width=40, textvariable=defaut2)
    ordonnees.pack()

    titre1 = tk.Label(frame, text="coefficients de la droite")
    titre1.pack()
    entree1 = tk.Entry(frame, width=40)
    entree1.pack()
    bouton1 = tk.Button(frame, text='afficher', command=regression)
    bouton1.pack()

    titre2 = tk.Label(frame, text="incertitude des coefficients de la droite")
    titre2.pack()
    entree2 = tk.Entry(frame, width=40)
    entree2.pack()
    bouton2 = tk.Button(frame, text='afficher', command=incert_regression)
    bouton2.pack()

    titre3 = tk.Label(frame, text="r_s2")
    titre3.pack()
    entree3 = tk.Entry(frame, width=40)
    entree3.pack()
    bouton3 = tk.Button(frame, text='afficher', command=r_s2)
    bouton3.pack()

    bouton = tk.Button(frame, text="tracer", command=graphe)
    bouton.pack()


# PERMET DE TRACER UNE REGRESSION POLYNOMIALE A PARTIR D'UNE SERIE DE POINTS
def quadratique():
    for widget in frame.winfo_children():
        widget.destroy()

    def fichier():
        return askopenfilename(initialdir=".",
                               title="Choisir votre fichier",
                               filetypes=(("fichiers texte", "*.txt"),
                                          ("all files", "*.*")))

    data = np.loadtxt(fichier())
    absc = data[:, 0]
    ordo = data[:, 1]
    dx = data[:, 2]
    dy = data[:, 3]

    def modele(x, a, b, c):
        return a*x**2 + b*x + c

    def regression():
        popt, pcov = curve_fit(modele, absc, ordo)
        entree1.delete(0, tk.END)
        entree1.insert(0, repr(np.round(popt, decimals=4)))

    def incert_regression():
        popt, pcov = curve_fit(modele, absc, ordo)
        entree2.delete(0, tk.END)
        entree2.insert(0, repr(np.round(np.sqrt(np.diag(pcov)),
                                        decimals=4)))

    def graphe():
        popt, pcov = curve_fit(modele, absc, ordo)
        x_modele = np.linspace(min(absc), max(absc), 1000)
        labelx = eval(abscisses.get())
        labely = eval(ordonnees.get())
        plt.figure(figsize=(14.2, 7.7))
        plt.errorbar(absc, ordo, dy, dx, ls="",
                     marker='+', color="black", label="f(x)")
        plt.plot(x_modele, modele(x_modele, *popt), label="régression")
        plt.xlabel(labelx)
        plt.ylabel(labely)
        plt.legend()
        plt.grid()
        plt.show()

    texte1 = tk.Label(frame, text="titre x")
    texte1.pack()
    defaut = tk.StringVar()
    defaut.set("'x'")
    abscisses = tk.Entry(frame, width=40, textvariable=defaut)
    abscisses.pack()

    texte2 = tk.Label(frame, text="titre y")
    texte2.pack()
    defaut2 = tk.StringVar()
    defaut2.set("'y'")
    ordonnees = tk.Entry(frame, width=40, textvariable=defaut2)
    ordonnees.pack()

    titre1 = tk.Label(frame, text="coefficients de la droite")
    titre1.pack()
    entree1 = tk.Entry(frame, width=40)
    entree1.pack()
    bouton1 = tk.Button(frame, text='afficher', command=regression)
    bouton1.pack()

    titre2 = tk.Label(frame, text="incertitude des coefficients de la droite")
    titre2.pack()
    entree2 = tk.Entry(frame, width=40)
    entree2.pack()
    bouton2 = tk.Button(frame, text='afficher', command=incert_regression)
    bouton2.pack()

    bouton = tk.Button(frame, text="tracer", command=graphe)
    bouton.pack()


# PERMET DE TRACER UNE REGRESSION POLYNOMIALE A PARTIR D'UNE SERIE DE POINTS
def cubique():
    for widget in frame.winfo_children():
        widget.destroy()

    def fichier():
        return askopenfilename(initialdir=".",
                               title="Choisir votre fichier",
                               filetypes=(("fichiers texte", "*.txt"),
                                          ("all files", "*.*")))

    data = np.loadtxt(fichier())
    absc = data[:, 0]
    ordo = data[:, 1]
    dx = data[:, 2]
    dy = data[:, 3]

    def modele(x, a, b, c, d):
        return a*x**3 + b*x**2 + c*x + d

    def regression():
        popt, pcov = curve_fit(modele, absc, ordo)
        entree1.delete(0, tk.END)
        entree1.insert(0, repr(np.round(popt, decimals=4)))

    def incert_regression():
        popt, pcov = curve_fit(modele, absc, ordo)
        entree2.delete(0, tk.END)
        entree2.insert(0, repr(np.round(np.sqrt(np.diag(pcov)),
                                        decimals=4)))

    def r_s2():
        r_s2 = stats.spearmanr(absc, ordo).correlation
        entree3.delete(0, tk.END)
        entree3.insert(0, r_s2)

    def graphe():
        popt, pcov = curve_fit(modele, absc, ordo)
        x_modele = np.linspace(min(absc), max(absc), 1000)
        labelx = eval(abscisses.get())
        labely = eval(ordonnees.get())
        plt.figure(figsize=(14.2, 7.7))
        plt.errorbar(absc, ordo, dy, dx, ls="",
                     marker='+', color="black", label="f(x)")
        plt.plot(x_modele, modele(x_modele, *popt), label="régression")
        plt.xlabel(labelx)
        plt.ylabel(labely)
        plt.legend()
        plt.grid()
        plt.show()

    texte1 = tk.Label(frame, text="titre x")
    texte1.pack()
    defaut = tk.StringVar()
    defaut.set("'x'")
    abscisses = tk.Entry(frame, width=40, textvariable=defaut)
    abscisses.pack()

    texte2 = tk.Label(frame, text="titre y")
    texte2.pack()
    defaut2 = tk.StringVar()
    defaut2.set("'y'")
    ordonnees = tk.Entry(frame, width=40, textvariable=defaut2)
    ordonnees.pack()

    titre1 = tk.Label(frame, text="coefficients de la droite")
    titre1.pack()
    entree1 = tk.Entry(frame, width=40)
    entree1.pack()
    bouton1 = tk.Button(frame, text='afficher', command=regression)
    bouton1.pack()

    titre2 = tk.Label(frame, text="incertitude des coefficients de la droite")
    titre2.pack()
    entree2 = tk.Entry(frame, width=40)
    entree2.pack()
    bouton2 = tk.Button(frame, text='afficher', command=incert_regression)
    bouton2.pack()

    titre3 = tk.Label(frame, text="r_s2")
    titre3.pack()
    entree3 = tk.Entry(frame, width=40)
    entree3.pack()
    bouton3 = tk.Button(frame, text='afficher',
                        command=r_s2)
    bouton3.pack()

    bouton = tk.Button(frame, text="tracer", command=graphe)
    bouton.pack()


# PERMET DE TRACER UNE REGRESSION GAUSSIENNE A PARTIR D'UNE SERIE DE POINTS
def gaussienne():
    for widget in frame.winfo_children():
        widget.destroy()

    def fichier():
        return askopenfilename(initialdir=".",
                               title="Choisir votre fichier",
                               filetypes=(("fichiers texte", "*.txt"),
                                          ("all files", "*.*")))

    data = np.loadtxt(fichier())
    absc = data[:, 0]
    ordo = data[:, 1]
    dx = data[:, 2]
    dy = data[:, 3]

    def modele(x, sigma, mu):
        return 1/(sigma*np.sqrt(2*np.pi))*np.exp(-(x-mu)**2/(2*sigma**2))

    def regression():
        popt, pcov = curve_fit(modele, absc, ordo)
        entree1.delete(0, tk.END)
        entree1.insert(0, repr(np.round(popt, decimals=4)))

    def incert_regression():
        popt, pcov = curve_fit(modele, absc, ordo)
        entree2.delete(0, tk.END)
        entree2.insert(0, repr(np.round(np.sqrt(np.diag(pcov)),
                                        decimals=4)))

    def largeur_mi_hauteur():
        popt, pcov = curve_fit(modele, absc, ordo)
        largeur = 2*np.sqrt(2*np.log(2))*popt[0]
        entree3.delete(0, tk.END)
        entree3.insert(0, repr(largeur))

    def graphe():
        popt, pcov = curve_fit(modele, absc, ordo)
        x_modele = np.linspace(min(absc), max(absc), 1000)
        labelx = eval(abscisses.get())
        labely = eval(ordonnees.get())
        plt.figure(figsize=(14.2, 7.7))
        plt.errorbar(absc, ordo, dy, dx, ls="",
                     marker='+', color="black", label="f(x)")
        plt.plot(x_modele, modele(x_modele, *popt), label="régression")
        plt.xlabel(labelx)
        plt.ylabel(labely)
        plt.legend()
        plt.grid()
        plt.show()

    texte1 = tk.Label(frame, text="titre x")
    texte1.pack()
    defaut = tk.StringVar()
    defaut.set("'x'")
    abscisses = tk.Entry(frame, width=40, textvariable=defaut)
    abscisses.pack()

    texte2 = tk.Label(frame, text="titre y")
    texte2.pack()
    defaut2 = tk.StringVar()
    defaut2.set("'y'")
    ordonnees = tk.Entry(frame, width=40, textvariable=defaut2)
    ordonnees.pack()

    titre1 = tk.Label(frame, text="coefficients de la droite")
    titre1.pack()
    entree1 = tk.Entry(frame, width=40)
    entree1.pack()
    bouton1 = tk.Button(frame, text='afficher', command=regression)
    bouton1.pack()

    titre2 = tk.Label(frame, text="incertitude des coefficients de la droite")
    titre2.pack()
    entree2 = tk.Entry(frame, width=40)
    entree2.pack()
    bouton2 = tk.Button(frame, text='afficher', command=incert_regression)
    bouton2.pack()

    titre3 = tk.Label(frame, text="largeur à mi-hauteur")
    titre3.pack()
    entree3 = tk.Entry(frame, width=40)
    entree3.pack()
    bouton3 = tk.Button(frame, text='afficher',
                        command=largeur_mi_hauteur)
    bouton3.pack()

    bouton = tk.Button(frame, text="tracer", command=graphe)
    bouton.pack()


# PERMET DE TRACER UNE REGRESSION EXPONENTIELLE A PARTIR D'UNE SERIE DE POINTS
def exponentielle():
    for widget in frame.winfo_children():
        widget.destroy()

    def fichier():
        return askopenfilename(initialdir=".",
                               title="Choisir votre fichier",
                               filetypes=(("fichiers texte", "*.txt"),
                                          ("all files", "*.*")))

    data = np.loadtxt(fichier())
    absc = data[:, 0]
    ordo = data[:, 1]
    dx = data[:, 2]
    dy = data[:, 3]

    def modele(x, a, b):
        return a*np.exp(b*x)

    def regression():
        popt, pcov = curve_fit(modele, absc, ordo)
        entree1.delete(0, tk.END)
        entree1.insert(0, repr(np.round(popt, decimals=4)))

    def incert_regression():
        popt, pcov = curve_fit(modele, absc, ordo)
        entree2.delete(0, tk.END)
        entree2.insert(0, repr(np.round(np.sqrt(np.diag(pcov)),
                                        decimals=4)))

    def r_s2():
        r_s2 = stats.spearmanr(absc, ordo).correlation
        entree3.delete(0, tk.END)
        entree3.insert(0, r_s2)

    def graphe():
        popt, pcov = curve_fit(modele, absc, ordo)
        x_modele = np.linspace(min(absc), max(absc), 1000)
        labelx = eval(abscisses.get())
        labely = eval(ordonnees.get())
        plt.figure(figsize=(14.2, 7.7))
        plt.errorbar(absc, ordo, dy, dx, ls="",
                     marker='+', color="black", label="f(x)")
        plt.plot(x_modele, modele(x_modele, *popt), label="régression")
        plt.xlabel(labelx)
        plt.ylabel(labely)
        plt.legend()
        plt.grid()
        plt.show()

    texte1 = tk.Label(frame, text="titre x")
    texte1.pack()
    defaut = tk.StringVar()
    defaut.set("'x'")
    abscisses = tk.Entry(frame, width=40, textvariable=defaut)
    abscisses.pack()

    texte2 = tk.Label(frame, text="titre y")
    texte2.pack()
    defaut2 = tk.StringVar()
    defaut2.set("'y'")
    ordonnees = tk.Entry(frame, width=40, textvariable=defaut2)
    ordonnees.pack()

    titre1 = tk.Label(frame, text="coefficients de la droite")
    titre1.pack()
    entree1 = tk.Entry(frame, width=40)
    entree1.pack()
    bouton1 = tk.Button(frame, text='afficher', command=regression)
    bouton1.pack()

    titre2 = tk.Label(frame, text="incertitude des coefficients de la droite")
    titre2.pack()
    entree2 = tk.Entry(frame, width=40)
    entree2.pack()
    bouton2 = tk.Button(frame, text='afficher', command=incert_regression)
    bouton2.pack()

    titre3 = tk.Label(frame, text="r_s2")
    titre3.pack()
    entree3 = tk.Entry(frame, width=40)
    entree3.pack()
    bouton3 = tk.Button(frame, text='afficher',
                        command=r_s2)
    bouton3.pack()

    bouton = tk.Button(frame, text="tracer", command=graphe)
    bouton.pack()


# PERMET DE TRACER UNE REGRESSION LOGARITHMIQUE A PARTIR D'UNE SERIE DE POINTS
def logarithmique():
    for widget in frame.winfo_children():
        widget.destroy()

    def fichier():
        return askopenfilename(initialdir=".",
                               title="Choisir votre fichier",
                               filetypes=(("fichiers texte", "*.txt"),
                                          ("all files", "*.*")))

    data = np.loadtxt(fichier())
    absc = data[:, 0]
    ordo = data[:, 1]
    dx = data[:, 2]
    dy = data[:, 3]

    def modele(x, a, b):
        return a*np.log(b*x)

    def regression():
        popt, pcov = curve_fit(modele, absc, ordo)
        entree1.delete(0, tk.END)
        entree1.insert(0, repr(np.round(popt, decimals=4)))

    def incert_regression():
        popt, pcov = curve_fit(modele, absc, ordo)
        entree2.delete(0, tk.END)
        entree2.insert(0, repr(np.round(np.sqrt(np.diag(pcov)),
                                        decimals=4)))

    def r_s2():
        r_s2 = stats.spearmanr(absc, ordo).correlation
        entree3.delete(0, tk.END)
        entree3.insert(0, r_s2)

    def graphe():
        popt, pcov = curve_fit(modele, absc, ordo)
        x_modele = np.linspace(min(absc), max(absc), 1000)
        labelx = eval(abscisses.get())
        labely = eval(ordonnees.get())
        plt.figure(figsize=(14.2, 7.7))
        plt.errorbar(absc, ordo, dy, dx, ls="",
                     marker='+', color="black", label="f(x)")
        plt.plot(x_modele, modele(x_modele, *popt), label="régression")
        plt.xlabel(labelx)
        plt.ylabel(labely)
        plt.legend()
        plt.grid()
        plt.show()

    texte1 = tk.Label(frame, text="titre x")
    texte1.pack()
    defaut = tk.StringVar()
    defaut.set("'x'")
    abscisses = tk.Entry(frame, width=40, textvariable=defaut)
    abscisses.pack()

    texte2 = tk.Label(frame, text="titre y")
    texte2.pack()
    defaut2 = tk.StringVar()
    defaut2.set("'y'")
    ordonnees = tk.Entry(frame, width=40, textvariable=defaut2)
    ordonnees.pack()

    titre1 = tk.Label(frame, text="coefficients de la droite")
    titre1.pack()
    entree1 = tk.Entry(frame, width=40)
    entree1.pack()
    bouton1 = tk.Button(frame, text='afficher', command=regression)
    bouton1.pack()

    titre2 = tk.Label(frame, text="incertitude des coefficients de la droite")
    titre2.pack()
    entree2 = tk.Entry(frame, width=40)
    entree2.pack()
    bouton2 = tk.Button(frame, text='afficher', command=incert_regression)
    bouton2.pack()

    titre3 = tk.Label(frame, text="r_s2")
    titre3.pack()
    entree3 = tk.Entry(frame, width=40)
    entree3.pack()
    bouton3 = tk.Button(frame, text='afficher',
                        command=r_s2)
    bouton3.pack()

    bouton = tk.Button(frame, text="tracer", command=graphe)
    bouton.pack()


# PERMET DE TRACER UNE FONCTION MATHEMATIQUE QUELCONQUE
# IL FAUT ECRIRE X POUR LES ABSCISSES ET ON PEUT MODIFIER L'INTERVALLE
# DANS L'APPLICATION
def fgraphe():
    for widget in frame.winfo_children():
        widget.destroy()

    def trace():
        x = eval(abscisses.get())
        y = eval(fonction.get())
        plt.figure(figsize=(14.2, 7.7))
        plt.plot(x, y, label="f(x)")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.grid()
        plt.show()

    texte1 = tk.Label(frame, text="abscisses")
    texte1.pack()
    defaut = tk.StringVar()
    defaut.set("np.linspace(-5, 5, 1000)")
    abscisses = tk.Entry(frame, width=40, textvariable=defaut)
    abscisses.pack()

    texte2 = tk.Label(frame, text="fonction")
    texte2.pack()
    fonction = tk.Entry(frame, width=40)
    fonction.pack()
    bouton1 = tk.Button(frame, text='tracer', command=trace)
    bouton1.pack()


def live_graphe():
    def fichier():
        return askopenfilename(initialdir=".",
                               title="Choisir votre fichier",
                               filetypes=(("fichiers texte", "*.txt"),
                                          ("all files", "*.*")))

    chemin = fichier()
    data = np.loadtxt(chemin)

    for i in range(0, 500000):
        x = data[:, 0]
        y = data[:, 1]
        if i == 0:
            line, = plt.plot(x, y)
        else:
            line.set_data(x, y)

    plt.show()


# CREATION DE LA FENETRE PRINCIPALE
fen = tk.Tk()
fen.title('Graphique interactif')
fen.geometry("900x400")
fen.wm_state(newstate="zoomed")
# permet d'utiliser la touche échap pour quitter le mode plein écran
fen.bind('<Escape>', lambda e: fen.destroy())

frame = tk.Frame(fen)
frame.pack()

# CREATION DU MENU
menubar = tk.Menu(fen)
fen.config(menu=menubar)
menufichier = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Type de graphe", menu=menufichier)

# CREATION DES OPTIONS DU MENU
menufichier.add_command(label="Graphe", command=graphe)
menuregression = tk.Menu(menufichier, tearoff=0)
menufichier.add_cascade(label="Régression", menu=menuregression)
menuregression.add_command(label="Linéaire", command=lineaire)
menuregression.add_command(label="Quadratique", command=quadratique)
menuregression.add_command(label="Cubique", command=cubique)
menuregression.add_command(label="Gaussienne", command=gaussienne)
menuregression.add_command(label="Exponentielle", command=exponentielle)
menuregression.add_command(label="Logarithmique", command=logarithmique)
menufichier.add_command(label="Graphe de fonction", command=fgraphe)
menufichier.add_command(label="Graphe en direct", command=live_graphe)


# CREATION DU BOUTON POUR QUITTER
btn = tk.Button(text="Quitter", bg="red", command=fen.destroy)
btn.pack(side='left')

fen.mainloop()
