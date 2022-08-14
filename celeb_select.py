import sqlite3
# create a celeb data base
con=sqlite3.connect("celeb.db")
#print("connection successfull")
cursor=con.cursor()
#print("cursor created")

# select query
# query="""
# SELECT * FROM famous WHERE award>5
# """
# cursor.execute(query)
# con.commit()
# items=cursor.fetchall()
# print(items)
# print name of celebrity with highest award
# query="""
# SELECT name,award FROM famous WHERE award=(SELECT MAX(award) FROM famous)
# """
# cursor.execute(query)
# con.commit()
# items=cursor.fetchall()
# print("name","\t\taward\n"f"{'_'*20}")
# for item in items:
#     name,award=item
#     print(f"{name}\t\t{award}")
#print oldest celebrity
# query="""
# SELECT name,age FROM famous WHERE age=(SELECT MAX(age) FROM famous)
# """
# cursor.execute(query)
# con.commit()
# items=cursor.fetchall()
# #print("name","\t\tage\n"f"{'_'*20}")
# for item in items:
#     name,age=item
#     print(f"{name} is the oldest actor with age {age} years")

# print the celebrity name that has been in the industry for a long time
# query="""
# SELECT name,age,year_in_industry FROM famous WHERE year_in_industry=(SELECT MAX(year_in_industry) FROM famous)
# """
# cursor.execute(query)
# con.commit()
# items=cursor.fetchall()
# for item in items:
#     name,age,year_in_industry=item
#     print(f"{name} is the oldest in industry who is {age} years old and been in industry since {year_in_industry}")
# print all details of celebrity who has been in the industry for long
# query="""
# SELECT * FROM famous WHERE year_in_industry=(SELECT MAX(year_in_industry) FROM famous)
# """
# cursor.execute(query)
# con.commit()
# items=cursor.fetchall()
# print(items)
#count of genre
# query="""
# SELECT genre,count(genre) FROM famous GROUP by genre
# """
# cursor.execute(query)
# con.commit()
# items=cursor.fetchall()
# print(items)
#Genre that appear most in the table
# query="""
# SELECT MAX(genre) FROM famous
# """
# cursor.execute(query)

# items=cursor.fetchall()
# for item in items:
#     genre=item
#     print(f"{item} is the most active genre in the collection")

#MINIMUM ALBUM
query="""
SELECT name,award,num_album FROM famous WHERE num_album=(SELECT MIN(num_album) FROM famous)
"""
cursor.execute(query)
con.commit()

items=cursor.fetchall()
print("Name of celebrity","\tAward","\t\tNo_of album\n"f"{'_'*50}")
for item in items:
    name,award,num_album=item
    print(f"{name}\t\t{award}\t\t\t{num_album}")

con.close()