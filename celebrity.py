import sqlite3
# create a celeb data base
con=sqlite3.connect("celeb.db")
print("connection successfull")
cursor=con.cursor()
print("cursor created")
#create table
# cursor.execute(
#     """
#     CREATE TABLE famous(
#         name text,
#         genre text,
#         num_album INTEGER,
#         age INTEGER,
#         award INTEGER,
#         year_in_industry INTEGER
#     )
#     """
# )
# con.commit()
# print("table created")
celeb_list=[
    ('Bukunmi Afolabi','Mystery',10,30,4,2000),
    ('Eniola Badmus','Adventure',12,32,5,2001),
    ('John Dumelus','Romance',11,45,3,2002),
    ('Adekola Odun','Fiction',20,40,5,2003),
    ('Funke Akindele','Drama',24,43,10,2000),
    ('Jide Salami','Comedy',15,32,6,2002),
    ('Rotimi Salami','Fiction',13,35,3,2005),
    ('Iyabo Ojo','Family',10,41,3,2004),
    ('Toyin Abraham','Drama',13,40,5,2005),
    ('Afeez Owo','Drama',10,43,3,2001),
    ('Taiwo Hassan','Drama',30,50,10,2000),
    ('Kabir Adekunle','music',20,42,4,2005),
    ('Shola Shobowale','Adventure',10,36,2,2006),
    ('David Adeleke','Music',20,35,5,2002),
    ('Simisola Ogunleye','Music',15,33,6,2007),
    ('Kosoko Adekunle','music',18,37,5,2005),
    ('Ayodeji Richard','Comedy',20,39,4,2000),
    ('Bright Okpocha','Comedy',15,35,2,2002),
    ('Bovi Ugboma','Comedy',15,32,3,2001),
    ('Asa Bukola Elemide','Music',15,43,5,2007)
]
query=(
    """
    INSERT INTO famous VALUES(?,?,?,?,?,?)
    """)

cursor.executemany(query,celeb_list)
con.commit()
print("Data inserted successful")
con.close()