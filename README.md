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

+ **Ope** : le package Ope représente les opérations possibles pour l'opérateur Select. L'opération "=" (`Equal.py`) a été implémenté. Il est très simple d'en rajouter d'autre (>, <, !=, <>, ...), il suffit juste de créer un objet (héritant de Ope) représentant l'opération.

+ **Representation** : le package Representation représente ce qui est en lien avec une relation, c'est-à-dire la relation en elle-même, les attributs qui constitue la relation, mais aussi une constante qui peuvent être utilisé avec l'opérateur Select qui recherche dans une relation un élément bien particulier.

+ **SPJRUD** : le package SPJRUD représente, comme son nom l'indique, chaque opérateur de l'algèbre relationnelle.

### 5. Difficultés rencontrées


### 6. Solutions apportées


### 7. Utilisation de la librairie

Ouvrez le fichier `Main.py` à la racine du projet et utilisez les méthodes ci-dessous à l'intérieur :

**INSTANCIER UNE RELATION SOI-MEME**

```python
rel = Relation(
        "RelationName", 
            [
                Attribute("attribute1", 'INTEGER'), 
                Attribute("attribute2", 'REAL'), 
                Attribute("attribute3", 'TEXT'),
            ])
```

**INSTANCIER UNE RELATION A PARTIR DE LA TABLE D'UNE BASE DE DONNEE**

```python
rel = creat_RelationFromDatabase("database.db", "table")
```

**INSTANCIER LES OPERATEURS SPJRUD**

```python
s1 = Select(Equal("attribute3", "Nicolas"), relation)
s2 = Select(Equal("attribute2", Constante(3.141592653589)), rel)
```

```python
p = Project(['attribute2', 'attribute4'], relation)
```

```python
j = Join(firstRelation, secondRelation)
```

```python
r = Rename("oldName", "newName", relation)
```

```python
u = Union(firstRelation, secondRelation)
```

```python
d = Difference(firstRelation, secondRelation)
```

```python
a = Project(["name", "sal", "job", "deptno"], firstRelation)
b = Project(["deptno", "departement", "loc"], Select(Equal("departement", Constante("RESEARCH")), Rename("dname", "departement", secondRelation)))
j = Join(a, b)
```

**AFFICHER L'EXPRESSION SPJRUD A LA CONSOLE**

```python
print(Select(Equal("attribute3", "Nicolas"), relation))
```
```
>> Select(Equal('attribute3', 'Nicolas'), Relation('RelationName'))
```

**AFFICHER L'EXPRESSION SQL A LA CONSOLE**

```python
print(Select(Equal("attribute3", "Nicolas"), relation).get_SQL())
```
```
>> SELECT * FROM (RelationName) WHERE attribute3 = "Nicolas"
```