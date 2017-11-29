'''
Created on Nov 29, 2017

@author: Pita
'''
import MySQLdb
db=None
param1=None
param2=None
param3=None
param4=None
def codificaHash(hashuri):
    #returneaza un sir de caractere in care biti hashurilor sunt transformate in caractere
    pass
def creazaBazeDate():
    pass
def conecteazaBazeDate():
    db = MySQLdb.connect(param1,param2,param3,param4 )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")
    
    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    print "Database version : %s " % data
    return True
def adaugaMelodie(nume,genMuzical,hashuri):
    if db==None:
        return False
    cursor = db.cursor()
    hashcodificat= codificaHash(hashuri)
    sql = """INSERT INTO MELODII(NUME,
         GEN_MUZICAL, HASH)
         VALUES ('"""+nume+"""', '"""+genMuzical+"""', """+hashcodificat+""")"""
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
        return True
    except:
        # Rollback in case there is any error
        db.rollback()
        return False
    return True
def obtineOMelodie(nume):
        # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    sql = "SELECT * FROM MELODII \
           WHERE NUME = "+nume
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchone()
        return True,nume,results[2]
    except:
        return False,None,None
def obtineGenMuzica(genMuzical):
        # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    sql = "SELECT * FROM MELODII \
           WHERE GEN_MUZICAL = "+genMuzical
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchone()
        return True,results[2]
    except:
        return False,None
def obtineToateMelodiile():
        # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    sql = "SELECT * FROM MELODII "
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchone()
        return True,results[2]
    except:
        return False,None
def stergeDinBazaDate(nume):
        # prepare a cursor object using cursor() method
    if db==None:
        return False
    cursor = db.cursor()
    
    # Prepare SQL query to DELETE required records
    if nume!="default":  
        sql = "DELETE FROM MELODII WHERE AGE > '%d'" % (20)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
        return True
    except:
        # Rollback in case there is any error
        db.rollback()
        return False
def inchideBazaDate():
    db.close()