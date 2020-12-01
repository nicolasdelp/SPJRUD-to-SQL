import sqlite3

def creat_Database(name):
    connection = sqlite3.connect(name + ".db")
    cursor = connection.cursor()

    #stucture de la table emp
    struct_table = """ empno INTEGER PRIMARY KEY,
                    ename TEXT,
                    job TEXT,
                    mgr INTEGER,
                    hiredate TEXT,
                    sal FLOAT,
                    comm FLOAT,
                    deptno INTEGER NOT NULL
                """

    #création de la table emp
    cursor.execute("CREATE TABLE emp (" + struct_table + ");")

    #création des éléments de la table
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

def print_Databases(name):
    connection = sqlite3.connect(name + ".db")
    cursor = connection.cursor()

    #affichage des tables
    for row in cursor.execute('SELECT * FROM emp'):
        print(row)

    print("------------------------------------------")

    for row in cursor.execute('SELECT * FROM dept'):
        print(row)

    print("------------------------------------------")

    for row in cursor.execute('SELECT * FROM salgrade'):
        print(row)
    
    #interruption de la connexion
    connection.close()

def getAttributesFromTable(databaseName, table) :
    connection = sqlite3.connect(databaseName + ".db")
    cursor = connection.cursor()
    infos = cursor.execute("PRAGMA table_info(" + table + ");")
    
    res = []
    for att in infos:
        res.append(att[1])

    connection.close()

    return res

#creat_Database("database")
print_Databases("database")
# print(",".join(getAttributesFromTable("database", "emp")))