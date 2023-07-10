import sqlite3

mydb = sqlite3.connect("\database.db")
mycursor = mydb.cursor()

try :
    mycursor.execute("""
    CREATE TABLE CourseDataVideos (
        Videos INT (2)
        )""")

    mycursor.execute("""
    CREATE TABLE CourseDataSheets (
        Sheets INT (2)
        )""")

    ###### Complete Videos
    mycursor.execute("""
    CREATE TABLE  VideosCompleted (
    videos INT (2) NOT NULL,
    UNIQUE(videos)
    );""")

    mycursor.execute("""
    CREATE TABLE  2VideosCompleted (
    videos INT (2) NOT NULL,
    UNIQUE(videos)
    );""")

    mycursor.execute("""
    CREATE TABLE  VideosCompleted (
        videos INT (2) NOT NULL,
        UNIQUE(videos)
    );""")

    mycursor.execute("""
    CREATE TABLE  VideosCompleted (
        videos INT (2) NOT NULL,
        UNIQUE(videos)
    );""")

    mycursor.execute("""
    CREATE TABLE  VideosCompleted (
        videos INT (2) NOT NULL,
        UNIQUE(videos)
    );""")

    mycursor.execute("""
    CREATE TABLE  VideosCompleted (
        videos INT (2) NOT NULL,
        UNIQUE(videos)
    );""")

    mycursor.execute("""
    CREATE TABLE  VideosCompleted (
        videos INT (2) NOT NULL,
        UNIQUE(videos)
    );""")

    mycursor.execute("""
    CREATE TABLE  VideosCompleted (
        videos INT (2) NOT NULL,
        UNIQUE(videos)
    );""")

    ###### Remain Videos
    mycursor.execute("""
    CREATE TABLE  VideosRemanning (
    videos INT (2) NOT NULL,
    UNIQUE(videos)
    );""")

    mycursor.execute("""
    CREATE TABLE  VideosRemanning (
    videos INT (2) NOT NULL,
    UNIQUE(videos)
    );""")

    mycursor.execute("""
    CREATE TABLE  VideosRemanning (
        videos INT (2) NOT NULL,
        UNIQUE(videos)
    );""")

    mycursor.execute("""
    CREATE TABLE  VideosRemanning (
        videos INT (2) NOT NULL,
        UNIQUE(videos)
    );""")

    mycursor.execute("""
    CREATE TABLE  VideosRemanning (
        videos INT (2) NOT NULL,
        UNIQUE(videos)
    );""")

    mycursor.execute("""
    CREATE TABLE  VideosRemanning (
        videos INT (2) NOT NULL,
        UNIQUE(videos)
    );""")

    mycursor.execute("""
    CREATE TABLE  VideosRemanning (
        videos INT (2) NOT NULL,
        UNIQUE(videos)
    );""")

    mycursor.execute("""
    CREATE TABLE  VideosRemanning (
        videos INT (2) NOT NULL,
        UNIQUE(videos)
    );""")
    ###### COmplete Sheets
    mycursor.execute("""
    CREATE TABLE  SheetsCompleted (
    Sheets INT (2) NOT NULL,
    UNIQUE(Sheets)
    );""")

    mycursor.execute("""
    CREATE TABLE  2SheetsCompleted (
    Sheets INT (2) NOT NULL,
    UNIQUE(Sheets)
    );""")

    mycursor.execute("""
    CREATE TABLE  SheetsCompleted (
        Sheets INT (2) NOT NULL,
        UNIQUE(Sheets)
    );""")

    mycursor.execute("""
    CREATE TABLE  SheetsCompleted (
        Sheets INT (2) NOT NULL,
        UNIQUE(Sheets)
    );""")

    mycursor.execute("""
    CREATE TABLE  SheetsCompleted (
        Sheets INT (2) NOT NULL,
        UNIQUE(Sheets)
    );""")

    mycursor.execute("""
    CREATE TABLE  SheetsCompleted (
        Sheets INT (2) NOT NULL,
        UNIQUE(Sheets)
    );""")

    mycursor.execute("""
    CREATE TABLE  SheetsCompleted (
        Sheets INT (2) NOT NULL,
        UNIQUE(Sheets)
    );""")

    mycursor.execute("""
    CREATE TABLE  SheetsCompleted (
        Sheets INT (2) NOT NULL,
        UNIQUE(Sheets)
    );""")

    ###### Remain Sheets
    mycursor.execute("""
    CREATE TABLE  SheetsRemanning (
    Sheets INT (2) NOT NULL,
    UNIQUE(Sheets)
    );""")

    mycursor.execute("""
    CREATE TABLE  SheetsRemanning (
    Sheets INT (2) NOT NULL,
    UNIQUE(Sheets)
    );""")

    mycursor.execute("""
    CREATE TABLE  SheetsRemanning (
        Sheets INT (2) NOT NULL,
        UNIQUE(Sheets)
    );""")

    mycursor.execute("""
    CREATE TABLE  SheetsRemanning (
        Sheets INT (2) NOT NULL,
        UNIQUE(Sheets)
    );""")

    mycursor.execute("""
    CREATE TABLE  SheetsRemanning (
        Sheets INT (2) NOT NULL,
        UNIQUE(Sheets)
    );""")

    mycursor.execute("""
    CREATE TABLE  SheetsRemanning (
        Sheets INT (2) NOT NULL,
        UNIQUE(Sheets)
    );""")

    mycursor.execute("""
    CREATE TABLE  SheetsRemanning (
        Sheets INT (2) NOT NULL,
        UNIQUE(Sheets)
    );""")

    mycursor.execute("""
    CREATE TABLE  SheetsRemanning (
        Sheets INT (2) NOT NULL,
        UNIQUE(Sheets)
    );""")

    ##### Notes
    mycursor.execute("""
    CREATE TABLE  Notes (
    Notes varchar(255) ,
    ID INTEGER  PRIMARY KEY AUTOINCREMENT
    );""")

    mycursor.execute("""
    CREATE TABLE  Notes (
    Notes varchar(255) ,
    ID INTEGER  PRIMARY KEY AUTOINCREMENT
    );""")

    mycursor.execute("""
    CREATE TABLE  Notes (
        Notes varchar(255) ,
        ID INTEGER  PRIMARY KEY AUTOINCREMENT
    );""")

    mycursor.execute("""
    CREATE TABLE  Notes (
        Notes varchar(255) ,
        ID INTEGER  PRIMARY KEY AUTOINCREMENT
    );""")

    mycursor.execute("""
    CREATE TABLE  Notes (
        Notes varchar(255) ,
        ID INTEGER  PRIMARY KEY AUTOINCREMENT
    );""")

    mycursor.execute("""
    CREATE TABLE  Notes (
        Notes varchar(255) ,
        ID INTEGER  PRIMARY KEY AUTOINCREMENT
    );""")

    mycursor.execute("""
    CREATE TABLE  Notes (
        Notes varchar(255) ,
        ID INTEGER  PRIMARY KEY AUTOINCREMENT
    );""")

    mycursor.execute("""
    CREATE TABLE  Notes (
        Notes varchar(255) ,
        ID INTEGER  PRIMARY KEY AUTOINCREMENT
    );""")
except :
    x=4

for x in range(1,66):
    mycursor.execute(f"INSERT INTO CourseDataVideos VALUES({x})")
    mycursor.execute(f"INSERT INTO  VideosRemanning VALUES({x})")
    mycursor.execute(f"INSERT INTO  VideosRemanning VALUES({x})")
    mycursor.execute(f"INSERT INTO  VideosRemanning VALUES({x})")
    mycursor.execute(f"INSERT INTO  VideosRemanning VALUES({x})")
    mycursor.execute(f"INSERT INTO  VideosRemanning VALUES({x})")
    mycursor.execute(f"INSERT INTO  VideosRemanning VALUES({x})")
    mycursor.execute(f"INSERT INTO  VideosRemanning VALUES({x})")
    mycursor.execute(f"INSERT INTO  VideosRemanning VALUES({x})")

for x in range(1,6):
    mycursor.execute(f"INSERT INTO CourseDataSheets VALUES({x})")
    mycursor.execute(f"INSERT INTO  SheetsRemanning VALUES({x})")
    mycursor.execute(f"INSERT INTO  SheetsRemanning VALUES({x})")
    mycursor.execute(f"INSERT INTO  SheetsRemanning VALUES({x})")
    mycursor.execute(f"INSERT INTO  SheetsRemanning VALUES({x})")
    mycursor.execute(f"INSERT INTO  SheetsRemanning VALUES({x})")
    mycursor.execute(f"INSERT INTO  SheetsRemanning VALUES({x})")
    mycursor.execute(f"INSERT INTO  SheetsRemanning VALUES({x})")
    mycursor.execute(f"INSERT INTO  SheetsRemanning VALUES({x})")

mydb.commit()
