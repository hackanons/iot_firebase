import mysql.connector as pm

try:
    con = pm.connect(host='localhost', database='acadviewdb', user='root', password='password')
    cursor = con.cursor()
    query6 = 'Create table Authors(AuthorID int primary key,FirstName varchar(15),MiddleName varchar(15),LastName varchar(15))'
    cursor.execute(query6)
    query4 = 'Create table Zip_Codes(Zip_Code_ID int primary key,City varchar(15),State varchar(20),Zip_Code int)'
    cursor.execute(query4)
    query3 = 'Create table Publishers(Publisher_ID int primary key,Name varchar(15),Street_Address varchar(50),\
    Suite_Number int,Zip_Code_ID int,foreign key(Zip_Code_ID) references Zip_Codes(Zip_Code_ID))'
    cursor.execute(query3)
    query2 = 'Create table Titles(TitleId int primary key,Title varchar(35),ISBN int,Publisher_ID int,Publication_Year int,\
    foreign key(Publisher_ID) references Publishers(Publisher_ID))'
    cursor.execute(query2)
    query1 = 'Create table Books(BookId int primary key,TitleId int,Location varchar(15),Genre varchar(10),\
    foreign key(TitleId) references Titles(TitleId))'
    cursor.execute(query1)
    query5 = 'Create table Authors_Titles(Author_Title_ID int primary key,AuthorID int ,TitleId int,\
    foreign key(AuthorID) references Authors(AuthorID),foreign key(TitleId) references Titles(TitleId))'
    cursor.execute(query5)
    print('Table Created')

except pm.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('DONE!!')
