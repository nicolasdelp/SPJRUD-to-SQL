from SPJRUD.SPJRUD import SPJRUD
from SPJRUD.Select import Select
from SPJRUD.Project import Project
from SPJRUD.Join import Join
from SPJRUD.Rename import Rename
from SPJRUD.Union import Union
from SPJRUD.Difference import Difference

from Ope.Equal import Equal

from Representation.Constante import Constante
from Representation.Attribute import Attribute
from Representation.Relation import Relation

import sqlite3
import os

def creat_Database(name):
    """
    Création d'une base de donnée automatiquement rempli avec 3 tables (emp, dept, salgrade)
    - name = le nom de la base de donnée

    >> creat_Database("BDD")
    """
    #on vérifie que la base de donnée n'existe pas encore
    if os.path.exists(name+".db"):
        raise Exception("La base de donnée " + name + ".db existe déjà")

    connection = sqlite3.connect(name + ".db")
    cursor = connection.cursor()

    #stucture de la table emp
    struct_table = """ empno INTEGER PRIMARY KEY,
                    ename TEXT,
                    job TEXT,
                    mgr INTEGER,
                    hiredate TEXT,
                    sal REAL,
                    comm REAL,
                    deptno INTEGER NOT NULL
                """

    #création de la table emp
    cursor.execute("CREATE TABLE emp (" + struct_table + ");")

    #création des éléments de la table
    # cursor.execute("INSERT INTO emp VALUES (1234,'KING','PRESIDENT',NULL,'2001-11-17',5000,NULL,10);")
    # cursor.execute("INSERT INTO emp VALUES (2345,'KING','PRESIDENT',NULL,'2001-11-17',5000,NULL,10);")
    # cursor.execute("INSERT INTO emp VALUES (3456,'KING','PRESIDENT',NULL,'2001-11-17',5000,NULL,10);")
    # cursor.execute("INSERT INTO emp VALUES (4567,'CLARK','MANAGER',7839,'2001-06-09',2450,NULL,10);")

    cursor.execute("INSERT INTO emp VALUES (7839,'KING','PRESIDENT',NULL,'2001-11-17',5000,NULL,10);")
    cursor.execute("INSERT INTO emp VALUES (7698,'BLAKE','MANAGER',7839,'2001-05-01',2850,NULL,30);")
    cursor.execute("INSERT INTO emp VALUES (7782,'CLARK','MANAGER',7839,'2001-06-09',2450,NULL,10);")
    cursor.execute("INSERT INTO emp VALUES (7566,'JONES','MANAGER',7839,'2001-04-02',2975,NULL,20);")
    cursor.execute("INSERT INTO emp VALUES (7654,'MARTIN','SALESMAN',7698,'2001-09-28',1250,1400,30);")
    cursor.execute("INSERT INTO emp VALUES (7499,'ALLEN','SALESMAN',7698,'2001-02-20',1600,300,30);")
    cursor.execute("INSERT INTO emp VALUES (7844,'TURNER','SALESMAN',7698,'2001-09-08',1500,0,30);")
    cursor.execute("INSERT INTO emp VALUES (7900,'JAMES','CLERK',7698,'2001-12-03',950,NULL,30);")
    cursor.execute("INSERT INTO emp VALUES (7521,'WARD','SALESMAN',7698,'2001-02-22',1250,500,30);")
    cursor.execute("INSERT INTO emp VALUES (7902,'FORD','ANALYST',7566,'2001-12-03',3000,NULL,20);")
    cursor.execute("INSERT INTO emp VALUES (7369,'SMITH','CLERK',7902,'2000-12-17',800,NULL,20);")
    cursor.execute("INSERT INTO emp VALUES (7788,'SCOTT','ANALYST',7566,'2002-12-09',3000,NULL,20);")
    cursor.execute("INSERT INTO emp VALUES (7876,'ADAMS','CLERK',7788,'2003-01-12',1100,NULL,20);")
    cursor.execute("INSERT INTO emp VALUES (7934,'MILLER','CLERK',7902,'2002-01-23',1300,NULL,10);")
    cursor.execute("INSERT INTO emp VALUES (7939,'PALMER','ANALYST',7902,'2012-01-23',1300,NULL,10);")
    cursor.execute("INSERT INTO emp VALUES (7983,'LOPEZ','SALESMAN',7566,'2012-01-23',1500,600,20);")
    cursor.execute("INSERT INTO emp VALUES (7994,'WILLIAMS','ANALYST',7698,'2012-01-23',950,NULL,30);")

    #stucture de la table emp2
    struct_table = """ empno INTEGER PRIMARY KEY,
                    ename TEXT,
                    job TEXT,
                    mgr INTEGER,
                    hiredate TEXT,
                    sal REAL,
                    comm REAL,
                    deptno INTEGER NOT NULL
                """

    #création de la table emp
    cursor.execute("CREATE TABLE emp2 (" + struct_table + ");")

    #création des éléments de la table
    cursor.execute("INSERT INTO emp2 VALUES (2828,'NICOLAS','PRESIDENT',NULL,'2020-12-04',5000,NULL,10);")
    cursor.execute("INSERT INTO emp2 VALUES (2323,'ALEXANDRE','PRESIDENT',NULL,'2001-11-17',5000,NULL,10);")

    cursor.execute("INSERT INTO emp2 VALUES (7839,'KING','PRESIDENT',NULL,'2001-11-17',5000,NULL,10);")
    cursor.execute("INSERT INTO emp2 VALUES (7698,'BLAKE','MANAGER',7839,'2001-05-01',2850,NULL,30);")
    cursor.execute("INSERT INTO emp2 VALUES (7782,'CLARK','MANAGER',7839,'2001-06-09',2450,NULL,10);")
    cursor.execute("INSERT INTO emp2 VALUES (7566,'JONES','MANAGER',7839,'2001-04-02',2975,NULL,20);")

    #stucture de la table dept
    struct_table = """
                        deptno INTEGER PRIMARY KEY,
                        dname TEXT,
                        loc TEXT
                    """
    
    #création de la table dept
    cursor.execute("CREATE TABLE dept (" + struct_table + ");")

    #création des éléments de la table dept
    cursor.execute("INSERT INTO dept VALUES (10, 'ACCOUNTING','NEW YORK');")
    cursor.execute("INSERT INTO dept VALUES (20, 'RESEARCH','DALLAS');")
    cursor.execute("INSERT INTO dept VALUES (30, 'SALES','CHICAGO');")
    cursor.execute("INSERT INTO dept VALUES (40, 'OPERATIONS','BOSTON');")

    #stucture de la table salgrade
    struct_table = """
                        grade INTEGER PRIMARY KEY,
                        losal INTEGER,
                        hisal INTEGER
                    """

    cursor.execute("CREATE TABLE salgrade (" + struct_table + ");")

    #création des éléments de la table salgrade
    cursor.execute("INSERT INTO salgrade VALUES (1,700,1200);")
    cursor.execute("INSERT INTO salgrade VALUES (2,1201,1400);")
    cursor.execute("INSERT INTO salgrade VALUES (3,1401,2000);")
    cursor.execute("INSERT INTO salgrade VALUES (4,2001,3000);")
    cursor.execute("INSERT INTO salgrade VALUES (5,3001,9999);")

    #envoie des requetes
    connection.commit()

    #interruption de la connexion
    connection.close()

def print_Databases(database, table):
    """
    Affiche tout le contenu des 3 tables de la base de donnée dans la console
    - database = la base de donnée

    >> print_Databases("BDD.db")
    """
    #on vérifie que la base de donnée existe
    if not os.path.exists(database):
        raise Exception("La base de donnée " + database + " n\'existe pas")

    #on vérifie que la table existe
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='" + table + "'")

    if cursor.fetchone()[0]!=1 :
	    raise Exception("La table " + table + " n\'existe pas")
    
    connection.commit()

    #affichage des tables
    for row in cursor.execute("SELECT * FROM " + table):
        print(row)

    print("------------------------------------------")
    
    #interruption de la connexion
    connection.close()

def get_AttributesFromTable(database, table):
    """
    Retourne le nom des attributs et leur type, d'une table d'une base de donnée
    - database = la base de donnée
    - table = la table

    >> get_AttributesFromTable("BDD.db", "emp")
    """
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    infos = cursor.execute("PRAGMA table_info(" + table + ");")
    
    attributesName = []
    attributesType = []
    for att in infos:
        attributesName.append(att[1])
        attributesType.append(att[2])

    connection.close()
    return [attributesName, attributesType]
    
def creat_RelationFromDatabase(database, table):
    """
    Retourne une relation en fonction de la table d'une base de donnée
    - database = la base de donnée
    - table = la table

    >> creat_RelationFromDatabase("BDD.db", "emp")
    """
    #on vérifie que la base de donnée existe
    if not os.path.exists(database):
        raise Exception("La base de donnée " + database + " n\'existe pas")

    #on vérifie que la table existe
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='" + table + "'")

    if cursor.fetchone()[0]!=1 :
	    raise Exception("La table " + table + " n\'existe pas")
    
    connection.commit()
    connection.close()

    #on crée la relation en fonction de la table
    attributes = []
    for x in range(len(get_AttributesFromTable(database, table)[0])): #car la taille des 2 listes est la même
        attributes.append(Attribute(get_AttributesFromTable(database, table)[0][x], get_AttributesFromTable(database, table)[1][x])) #nom de l'attribut + type de l'attribut
    
    return Relation(table, attributes)

def executeSQL_OnDatabase(database, SQL):
    """
    Exécute une requéte SQL sur une base de donnée
    - database = la base de donnée
    - SQL = la requéte SQL

    >> executeSQL_OnDatabase(BDD.db, "SELECT * FROM table")
    """
    #on vérifie que la base de donnée existe
    if not os.path.exists(database):
        raise Exception("La base de donnée " + database + " n\'existe pas")

    #on execute la requéte
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    for row in cursor.execute(SQL):
        print(row)
    
    connection.commit()
    connection.close()