#import sql
import sqlite3

#connect to database
con= sqlite3.connect('stutern.db')
print('connection succesfully')

cursor=con.cursor()
con.commit()

#create table
# cursor.execute(
#     """
#     CREATE TABLE datascientist(
#         first_name text,
#         last_name text,
#         email_id text,
#         course
#     )
#     """
    
# )
# con.commit()
# print("table created successfully")

# student_list = [
#     ("Mariam","Adeoti","mariam.adeoti@stutern.com","Data Science"),
#     ("Abubakar","Adisa","abubakar.adisa@stutern.com","Data Science"),
#     ("Eniola","Osadare","eniola.osadare@stutern.com","Data Science"),
#     ("Temitope","Bamidele","temitope.bamidele@stutern.com","Data Science"),
#     ("Angela","Emmanuel","angela.emanuel@stutern.com","Data Science"),
#     ("Kafayat","Ibrahim","kafayat.ibrahim@stutern.com","Data Science"),
#     ("Omowumi","Awoniran","omowumi.awonira@stutern.com","Data Science")
    
# ]
# cursor.executemany(
# """
# INSERT INTO datascientist
# VALUES (?, ?, ?, ?)
# """,
# student_list
# )
# con.commit()
# print("multiple items inserted successfully")
# cursor.execute(
#     """
#     SELECT * FROM datastudent
#     """
# )
# items=cursor.fetchall()
# print("student list retrieve successfully")
# #print output to display in a tabular form
# print("first_name", "\tlast_name" +"\t\t\tE-mail"+"\t\t\t\tcourse\n" f"{'.'*90}")

# #loop through the items
# for item in items:
#    first_name,last_name,email_id,course=item
#    print(f"{first_name:16}\t{last_name:16}\t{email_id:16}\t{course}")
#print(items)

#con.commit()

# Alter the table
# cursor.execute("ALTER TABLE datascientist RENAME to datastudent")
# con.commit()
#print("table name changed")
#alter column
# cursor.execute("ALTER TABLE datastudent ADD COLUMN level")
# con.commit()
#print("column to the data")
#update the table by adding vallue to level
# cursor.execute(""" UPDATE datastudent SET level ='Stage1'""")
# con.commit()
# print("table updated")
# cursor.execute(
#     """
#     SELECT * FROM datastudent
#     """
# )
# items=cursor.fetchall()
# print("student list retrieve successfully")
# #print output to display in a tabular form
# print("first_name", "\tlast_name" +"\t\t\tE-mail"+"\t\t\tcourse"+"\tlevel\n" f"{'.'*100}")

# #loop through the items
# for item in items:
#    first_name,last_name,email_id,course,level=item
#    print(f"{first_name:16}\t{last_name:16}\t{email_id:16}\t{course:20}{level}")
#delete from table
cursor.execute("DELETE FROM datastudent WHERE rowid ='2'")
con.commit()
print("item deleted successfully")
cursor.execute(
    """
    SELECT * FROM datastudent
    """
)
items=cursor.fetchall()
#print("student list retrieve successfully")
#print output to display in a tabular form
print("first_name", "\tlast_name" +"\t\t\tE-mail"+"\t\t\tcourse"+"\tlevel\n" f"{'.'*100}")

#loop through the items
for item in items:
   first_name,last_name,email_id,course,level=item
   print(f"{first_name:16}\t{last_name:16}\t{email_id:16}\t{course:20}{level}")
#fetch the items in the table
con.close()