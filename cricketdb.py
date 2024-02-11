import sqlite3

c=sqlite3.connect('.\Final_Project\cricket.db')
myCursor=c.cursor()



sql='''CREATE TABLE tblPlayers (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                playerName TEXT(25) NOT NULL
         );
       '''
myCursor.execute(sql)
print("Players table Created Succesfully")


sql='''CREATE TABLE tblStats (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                playerID INTEGER,
                matches INTEGER NOT NULL,
                runs INTEGER NOT NULL,
                century INTEGER NOT NULL,
                half_century INTEGER NOT NULL,
                value INTEGER NOT NULL,
                ctg TEXT(5),
                FOREIGN KEY(playerID) REFERENCES tblPlayers("ID")
         );
       '''
myCursor.execute(sql)
print("Stats table Created Succesfully")

sql='''CREATE TABLE tblTeams (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                teamName TEXT(20),
                playerID INTEGER,
                value INTEGER NOT NULL,
                FOREIGN KEY(playerID) REFERENCES tblPlayers("ID")
         );
       '''
myCursor.execute(sql)
print("Teams table Created Succesfully")

sql='''CREATE TABLE tblMatch_1 (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                playerID INTEGER,
                scored INTEGER NOT NULL,
                faced INTEGER NOT NULL,
                fours INTEGER NOT NULL,
                sixes INTEGER NOT NULL,
                bowled INTEGER NOT NULL,
                maiden INTEGER NOT NULL,
                given INTEGER NOT NULL,
                wkts INTEGER NOT NULL,
                catches INTEGER NOT NULL,
                stumping INTEGER NOT NULL,
                runOut INTEGER NOT NULL,
                FOREIGN KEY(playerID) REFERENCES tblPlayers("ID")
         );
       '''
myCursor.execute(sql)
print("Match_1 table Created Succesfully")


sql='''INSERT INTO tblPlayers VALUES 
            (1,"Kohli"),
            (2,"Yuvraj"),
            (3,"Rahane"),
            (4,"Dhawan"),
            (5,"Dhoni"),
            (6,"Axar"),
            (7,"Pandya"),
            (8,"Jadeja"),
            (9,"Kedar"),
            (10,"Ashwin"),
            (11,"Umesh"),
            (12,"Bumrah"),
            (13,"Bhuwaneshwar"),
            (14,"Rohit"),
            (15,"kartick");
       '''
myCursor.execute(sql)
print("Players table Inserted Succesfully") 

sql = '''INSERT INTO tblMatch_1 VALUES 
    (1,1,102,98,8,2,0,0,0,0,0,0,1),
    (2,2,12,20,1,0,48,0,36,1,0,0,0),
    (3,3,49,75,3,0,0,0,0,0,1,0,0),
    (4,4,32,35,4,0,0,0,0,0,0,0,0),
    (5,5,56,45,3,1,0,0,0,0,3,2,0),
    (6,6,8,4,2,0,48,2,35,1,0,0,0),
    (7,7,42,36,3,3,30,0,25,0,1,0,0),
    (8,8,18,10,1,1,60,3,50,2,1,0,1),
    (9,9,65,60,7,0,24,0,24,0,0,0,0),
    (10,10,23,42,3,0,60,2,45,6,0,0,0),
    (11,11,0,0,0,0,54,0,50,4,1,0,0),
    (12,12,0,0,0,0,60,2,49,1,0,0,0),
    (13,13,15,12,2,0,60,1,46,2,0,0,0),
    (14,14,46,65,5,1,0,0,0,0,1,0,0),
    (15,15,29,42,3,0,0,0,0,0,2,0,1);
    '''
myCursor.execute(sql)
print("Mactch_1 table Inserted Succesfully")

sql = """INSERT INTO tblStats VALUES 
        (1,1,189,8257,28,43,120,"BAT"),
        (2,2,86,3589,10,21,100,"BAT"),
        (3,3,158,5435,11,31,100,"BAT"),
        (4,4,25,565,2,1,85,"AR"),
        (5,5,78,2573,3,19,75,"BAT"),
        (6,6,67,208,0,0,100,"BWL"),
        (7,7,70,77,0,0,75,"BWL"),
        (8,8,16,1,0,0,85,"BWL"),
        (9,9,111,675,0,1,90,"BWL"),
        (10,10,136,1914,0,10,100,"AR"),
        (11,11,296,9496,10,64,110,"WK"),
        (12,12,73,1365,0,8,60,"WK"),
        (13,13,17,289,0,2,75,"AR"),
        (14,14,304,8701,14,52,85,"BAT"),
        (15,15,11,111,0,0,75,"AR");
  
        """
myCursor.execute(sql)
print("Stats table Inserted Succesfully")
