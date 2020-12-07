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

### 4. Organisation de la librairie
La librairie est constitué de 3 "packages", **Ope**, **Representation** et **SPJRUD** ainsi que 2 fichiers, `sql.py` et `main.py`

+ **Ope** : le package Ope représente les opérations possibles pour l'opérateur Select. L'opération "=" (`Equal.py`) a été implémenté. Il est très simple d'en rajouter d'autre (>, <, !=, <>, ...), il suffit juste de créer un objet (héritant de Ope) représentant l'opération.

+ **Representation** : le package Representation représente tout ce qui est en lien avec une relation, c'est-à-dire la relation en elle-même, les attributs qui constitue la relation, mais aussi une constante qui peuvent être utilisé avec l'opérateur Select qui recherche dans un attribut un élément bien particulier.

+ **SPJRUD** : le package SPJRUD représente, comme son nom l'indique, chaque opérateur de l'algèbre relationnelle.

+ `sql.py` : ce fichier contient les méthodes a utiliser lorsque l'on applique les opérateurs SPJRUD sur une base de données.

+ `main.py` : ce fichier est l'entrée de la librairie, c'est ici que l'utilisateur doit instancier ses relations, ses opérateurs SPJRUD ainsi qu'utiliser les méthodes s'appliquant à une base de données SQLite.

Une implémentation comme celle-ci permet la modularité de la librairie, il est très simple de rajouter des classes dans chaque "package"

### 5. Mes choix d'implémentation


### 6. Utilisation de la librairie

Ouvrez le fichier `Main.py` à la racine du projet et utilisez les méthodes ci-dessous à l'intérieur :

**Instancier une relation soi-même**

```python
rel = Relation(
        "RelationName", 
            [
                Attribute("attribute1", 'INTEGER'), 
                Attribute("attribute2", 'REAL'), 
                Attribute("attribute3", 'TEXT'),
            ])
```

**Instancier une relation à partir de la table d'une base de données**

```python
rel = creat_RelationFromDatabase("database.db", "table")
```

**Instancier les opérateurs SPJRUD**

```python
s1 = Select(Equal("attribute3", "attribute2"), relation) #retourne les tuples ayant la même valeur dans les 2 attributs
s2 = Select(Equal("attribute2", Constante(3.141592653589)), relation) #retourne les éléments de l'attribut ayant comme valeur la constante
```

```python
p = Project(['attribute2', 'attribute4'], relation) #retourne tout les tuples avec seulement ces attributs
```

```python
j = Join(firstRelation, secondRelation) #retourne la jointure des 2 relations si au moins 1 attribut correspond dans les 2 relations
```

```python
r = Rename("oldName", "newName", relation) #renomme un attribut d'une relation
```

```python
u = Union(firstRelation, secondRelation) #retourne l'union des 2 relations si elles ont les mêmes attributs et supprime les doublons
```

```python
d = Difference(firstRelation, secondRelation) #retourne la difference des 2 relations si elles ont les mêmes attributs
```

**Instancier un opérateur SPJRUD de manière récursive**

```python
a = Project(["name", "sal", "job", "deptno"], firstRelation)
b = Project(["deptno", "departement", "loc"], Select(Equal("departement", Constante("RESEARCH")), Rename("dname", "departement", secondRelation)))

j = Join(a, b)
```

**Afficher l'expression SPJRUD dans la console**

```python
print(Select(Equal("attribute3", "Nicolas"), relation))
```
```
>> Select(Equal('attribute3', 'Nicolas'), Relation('RelationName'))
```

**Afficher l'expression SQL dans la console**

```python
print(Select(Equal("attribute3", "Nicolas"), relation).get_SQL())
```
```
>> SELECT * FROM (RelationName) WHERE attribute3 = "Nicolas"
```

**Exécuter une requête SQL sur une base de données (BDD des TPs)**

```python
executeSQL_OnDatabase("database.db", Project(["name", "sal", "job", "deptno"], Select(Equal("sal", Constante(5000.0)), Rename("ename", "name", creat_RelationFromDatabase("database.db", "emp")))).get_SQL())
```
```
>> ('KING', 5000.0, 'PRESIDENT', 10)
```