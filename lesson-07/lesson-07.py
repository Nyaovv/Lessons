                        # Базы данных
                    _           _
MySQL (MariaDB)      |           |              
PostgreSQL           |           |              
MS SQL Server        |} СУБД     |}SQL              
Oracle              _|           |                  
                                 |
SQLite                          _|

(DB API) - стандарт

    #User                                               #role
id  username    password  role_id              name     title
 1  root        toor       admin               admim    админ
 2  stud        itmo       user               user   пользователь
 
                        # User
 # id - PK Primary Key (Первчиный ключ) (Первая колонка)
 # Могут быть ситуации когда он может отсутствовать, но нужны
 # очень веские причины
 
 # relo_id - FK Foreign Key (Внешний ключ)
 
 SQL ==подмножества==> DDL (create table) # Язык описания данных
                       DML 
                       
# Любая база даннах работает медленно, если в ней есть 0 / null
