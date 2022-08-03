#import sql
import sqlite3

#connect to database
con= sqlite3.connect('stutern.db')
print('connection succesfully')

cursor=con.cursor()


#create table
# cursor.execute(
#     """
#     CREATE TABLE dscientist(
#         first_name text,
#         last_name text,
#         email_id text,
#         course
#     )
#     """
    
# )
# print("table created")
# student_list = [
#     ("Mariam","Adeoti","mariam.adeoti@stutern.com","Data Science"),
#     ("Abubakar","Adisa","abubakar.adisa@stutern.com","Data Science"),
#     ("Eniola","Osadare","eniola.osadare@stutern.com","Data Science"),
#     ("Temitope","Bamidele","temitope.bamidele@stutern.com","Data Science"),
#     ("Angela","Emmanuel","angela.emanuel@stutern.com","Data Science"),
#     ("Kafayat","Ibrahim","kafayat.ibrahim@stutern.com","Data Science"),
#     ("Omowumi","Awoniran","omowumi.awonira@stutern.com","Data Science"),
#     ("Aisha","Abass","aisha.abass@stutern.com","Data Science"),
#     ("Babagide","Adesugba","babagide.adesugba@stutern.com","Data Science"),
#     ("Rashida","Sikiru","rahida.sikiru@stutern.com","Data Science"),
#     ("Faith","Amure","faith.amure@stutern.com","Data Science"),
#     ("Deborah","Olorunnishola","deborah.olorunnishola@stutern.com","Data Science"),
#     ("Prince","Okocha","prince.okocha@stutern.com","Data Science"),
#     ("Cynthia","Awiya","cynthia.awiya@stutern.com","Data Science"),
#     ("Stephen","Ogungbile","stephen.ogungbile@stutern.com","Data Science"),
#     ("Tawakalitu","Awonaike","tawakalitu.awonaike@stutern.com","Data Science"),
#     ("Ade","Afolabi","ade.afolabi@stutern.com","Data Science"),
#     ("Ramotallahi","Jubril","ramatallahi.jubril@stutern.com","Data Science"),
#     ("Joyce","Ezeonwu","joyce.ezeonwu@stutern.com","Data Science"),
#     ("Praise","Emmanuel","praise.emmanuel@stutern.com","Data Science"),
#     ("Sheriff","Azeez","sheriff.azeez@stutern.com","Data Science"),
#     ("Kehinde","Orolade","kehinde.orolade@stutern.com","Data Science"),
#     ("Christian","Uzondu","christian.uzondu@stutern.com","Data Science"),
#     ("Theresa","Karamoh","theresa.karamoh@stutern.com","Data Science"),
#     ("Tina","Uyateide","tina.uyateide@stutern.com","Data Science"),
#     ("Bukola","Ajayi","bukola.ajayi@stutern.com","Data Science"),
#     ("Gideon","George","gideon.george@stutern.com","Data Science"),
#     ("Esther","Akpanowo","esther.akpanowo@stutern.com","Data Science"),
#     ("Binta","Umar","binta.umar@stutern.com","Data Science"),
#     ("Placidus","Ali","placidus.ali@stutern.com","Data Science"),
#     ("Deborah","Adesanya","deborah.adesanya@stutern.com","Data Science"),
#     ("Ogechi","Njemanze","ogechi.njemanze@stutern.com","Data Science"),
#     ("Victoria","Chukwuno","victoria.chukwuno@stutern.com","Data Science"),
#     ("Ganiyat","Shittu","ganiyat.shittu@stutern.com","Data Science"),
#     ("Lawrence","Aneshimokha","lawrence.aneshimokha@stutern.com","Data Science"),
#     ("Eke","Ihuoma","eke.ihuoma@stutern.com","Data Science"),
#     ("Angela","Emmanuel","angela.emmanuel@stutern.com","Data Science"),
#     ("Oluwaseyi","Nichiolas","oluwaseyi.nichiolas@stutern.com","Data Science"),
#     ("Kehinde","Ayanleye","kehinde.ayanleye@stutern.com","Data Science")
# ]
    
# query=("""INSERT INTO dscientist
# VALUES(?,?,?,?)""")
# cursor.executemany(query,student_list)
# print("Items inserted succefully")
#fetch the items in the table
cursor.execute(
    """
    SELECT * FROM dscientist
    """
)
items= cursor.fetchall()
print("items fetched successfully")
#print output to display in a tabular form
print("first_name", "\tlast_name" +"\t\t\tE-mail"+"\t\t\t\tcourse\n" f"{'.'*90}")

#loop through the items
for item in items:
   first_name,last_name,email_id,course=item
   print(f"{first_name:16}\t{last_name:16}\t{email_id:16}\t\t{course}")
con.commit()
con.close()
