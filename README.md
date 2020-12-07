# Projet de Bases de Données I : Compilation SPJRUD vers SQL

##### par Delplanque Nicolas

### 1. Présentation du projet
L’objectif de ce projet est d’implémenter en [Python](https://www.python.org/) un outil de traduction de requêtes SPJRUD vers des requêtes SQL. 
Il sera aussi possible d'exécuter une requête SQL (ayant été traduite en amont d'une requête SPJRUD) sur une base de données 
grâce à la librairie Python [SQLite](https://docs.python.org/3/library/sqlite3.html) après un certain nombre de vérifications.

### 2. SPJRUD c'est quoi ?
**SPJRUD** est un acronyme pour :

**S**elect - **P**roject - **J**oin - **R**ename - **U**nion - **D**ifference

En algèbre relationnelle, ces 6 opérateurs permettent d'effectuer des opérations sur des relations. Ils peuvent être facilement traduit en SQL, en y ajoutant quelques conditions supplémentaires car SPJRUD est plus restrictif pour certains opérateurs.

[Wikipédia](https://fr.wikipedia.org/wiki/Alg%C3%A8bre_relationnelle#:~:text=L'alg%C3%A8bre%20relationnelle%20est%20un,des%20bases%20de%20donn%C3%A9es%20relationnelles.)

### 3. SQL c'est quoi ?
**SQL** est un acronyme pour :

**S**tructured **Q**uery **L**anguage

SQL est un langage informatique normalisé servant à exploiter des bases de données relationnelles. SQL permet de rechercher, d'ajouter, de modifier ou de supprimer des données dans les bases de données relationnelles. 

[Wikipédia](https://fr.wikipedia.org/wiki/Structured_Query_Language#:~:text=SQL%20(sigle%20de%20Structured%20Query,des%20bases%20de%20donn%C3%A9es%20relationnelles.)) 

### 4. Mes choix d'implémentation
Mon implémentation est constitué de 3 "packages", **Ope**, **Representation** et **SPJRUD**.

+ Ope : le package Ope représente les opérations possibles pour l'opérateur Select. L'opération "=" (Equal) a été implémenter, et il est très simple d'en rajouter d'autre (>, <, !=, <>, ...), il suffit juste de créer un objet représentant l'opération héritant de Ope.

+ Representation : le package Representation représente ce qui est en lien avec une relation, c'est-à-dire la realtion en elle-même, les attributs qui la constitue mais aussi une constante qui peuvent être utilisé avec l'opérateur Select qui recherche dans une relation un élément bien particulier.

+ SPJRUD : le package SPJRUD représente, comme son nom l'indique, chaque les opérateur de l'algèbre relationnelle.

### 5. Difficultés rencontrées


### 6. Solutions apportées


### 7. Utilisation de la librairie

