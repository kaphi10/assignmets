# creating a database
import sqlite3
print ('successful')

#create a connection with database

con= sqlite3.connect("stock.db")
# assign cursor
cursor= con.cursor()
# create table stationary
# cursor.execute(
#     """
#     CREATE TABLE stationary(
#         item_id INTEGER,
#         item_name text,
#         cost_price float,
#         quantity INTEGER
#     )
#     """
# )
# print("table created successfully")
#insert into table
# st=[
#     (1,'Text Books',1200,5),
#     (2,'Note Books',1700,25),
#     (3,'Files',1000,10),
#     (4,'Biro',900,15),
#     (5,'Pencil',500,5),
#     (6,'Celltape',2000,4),
#     (7,'School Bag',3000,5),
#     (8,'Stapler',800,5),
#     (9,'Board',5000,3),
#     (10,'Eraser',200,15),

# ]
# query=("""
# INSERT INTO stationary VALUES(?,?,?,?)

# """)
# cursor.executemany(query,st)
# print("items inserted successfully")
query=(
    """
    SELECT 
    *,
        CASE
            WHEN quantity >8 THEN 'sufficient'
            WHEN cost_price >800 THEN 'sufficient'
            ELSE 'kindly restock'
        END AS status
    FROM stationary
    ORDER BY cost_price DESC
    """
)
cursor.execute(query)
items=cursor.fetchall()
print("id","item_name","\tcost_price","\tquantity","\tstatus\n"f"{'_'*80}")
for item in items:
    item_id,item_name,cost_price,quantity,status=item
    print(f"{item_id} {item_name}\t\t{cost_price}\t\t\t{quantity}\t\t\t\t{status}")

  #commit to database
con.commit()

#closse connection
con.close()
