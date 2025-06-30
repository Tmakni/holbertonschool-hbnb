#!/usr/bin/python3

"""
ce fichier sert de boîte à réglages pour l'application
imagine un grand cahier où l'on écrit toutes les règles
que notre programme doit suivre
"""

import os
from pathlib import Path

"""
BASE_DIR pointe vers le dossier principal du projet
on s'en servira pour fabriquer des chemins sûrs, peu importe
l'endroit d'où l'on lance le programme
"""
BASE_DIR = Path(__file__).resolve().parent.parent


class Config:
    """
    La classe Config est comme une armoire :
    on y range des étiquettes avec des informations importantes
    que Flask ira récupérer toute seule
    Les enfants (autres classes) pourront hériter de ces étiquettes
    """

    SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-prod")
    """
    SECRET_KEY est un mot magique.
    Il aide Flask à garder les biscuits (cookies) en sécurité
    pour que personne ne les vole
    Si le mot magique n'est pas donné depuis l'extérieur,
    on écrit « change-me-in-prod » pour rappeler qu'il faut le remplacer
    """

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    """
    cette ligne dit à la bibliothèque SQLAlchemy :
    « Ne note pas chaque micro-changement, ça ferait
    travailler lordinateur pour rien »
    """

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "another-secret")
    """
    un second mot secret, utilisé spécialement
    pour signer les cartes didentité (tokens JWT) des utilisateurs
    """

    ITEMS_PER_PAGE = 20
    """
    Quand on affiche une longue liste de choses,
    on choisit de les montrer par paquets de 20.
    Comme ça, la page nest pas trop longue et reste facile à lire
    """
class DevelopmentConfig(Config):
    """
    Cette classe représente l'environnement « développement ».
    On l'utilise quand on code tranquillement sur son ordinateur
    Elle hérite de toutes les règles de Config
    """

    DEBUG = True
    """
    Lorsque DEBUG est a True Flask affiche
    des messages d'erreur et recharge automatiquement
    le serveur dès qu'on modifie un fichier
    """

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASE_DIR/'dev.db'}"
    """
    ici on dit à SQLAlchemy d'enregistrer les données
    dans un petit fichier « dev.db » placé à la racine du projet.
    C'est pratique, car on n'a pas besoin d'installer
    un vrai serveur de base de données pour tester le code.
    """


class TestingConfig(Config):
    """
    Cette classe est faite pour les tests automatisés.
    L'idée est de pouvoir lancer des vérifications très vite
    sans polluer le disque ni mélanger les données.
    """

    TESTING = True
    """
    Avec TESTING à True, Flask se met dans un mode spécial :
    les erreurs sont propagées pour que les tests les détectent ;
    certaines sécurités (comme le CSRF) sont désactivées.
    """

    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    """
    “sqlite:///:memory:” signifie :
    « Crée la base directement en mémoire vive ».
    Dès que le test se termine, la base disparaît :
    aucun fichier n'est créé et les tests restent rapides.
    """

    ITEMS_PER_PAGE = 5
    """
    Pendant les tests, on réduit la pagination à 5 objets
    pour écrire des assertions plus courtes et plus simples.
    """


class ProductionConfig(Config):
    """
    Cette classe correspond à l'application en “vraie vie” :
    celle que les utilisateurs verront en ligne.
    La sécurité et la performance passent avant tout.
    """

    DEBUG = False
    """
    On coupe le mode DEBUG, sinon les messages d'erreur détaillés
    pourraient révéler des informations sensibles aux visiteurs.
    """

    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://{user}:{pwd}@{host}/{db}".format(
            user=os.getenv("MYSQL_USER", "hbnb_user"),
            pwd=os.getenv("MYSQL_PASSWORD", "please-change"),
            host=os.getenv("MYSQL_HOST", "localhost"),
            db=os.getenv("MYSQL_DATABASE", "hbnb_production")
        )
    )
    """
    On choisit MySQL pour gérer les vraies données.
    Les informations de connexion (utilisateur, mot de passe, etc.)
    sont lues dans les variables d'environnement :
    ainsi, elles ne sont jamais écrites dans le code source.
    """

    SECRET_KEY = os.getenv("SECRET_KEY")
    """
    Ici, on enlève la valeur de secours :
    si SECRET_KEY n'est pas définie sur le serveur,
    l'application refusera de démarrer.
    C'est un filet de sécurité pour ne pas oublier
    de définir une clé solide en production.
    """


def get_config(path: str):
    """
    Cette fonction est un petit assistant :
    elle reçoit un texte comme « 'config.DevelopmentConfig' »
    et renvoie la classe correspondante.
    Cela permet de choisir la configuration
    via une simple chaîne (variable d'environnement, argument CLI…).
    """
    module_path, class_name = path.rsplit(".", 1)

    """
    On importe le module qui contient la classe.
    Par exemple, si path vaut 'config.DevelopmentConfig',
    module_path sera 'config' et class_name 'DevelopmentConfig'.
    """
    module = __import__(module_path, fromlist=[class_name])

    """
    getattr récupère la classe à l'intérieur du module.
    On la renvoie pour que create_app puisse l'utiliser.
    """
    return getattr(module, class_name)
