#!/usr/bin/env python3

import psycopg2

DBNAME = "news"


def query1():
    '''This function executes the first query
    and prints a well-formatted output for the same.'''
    c = db.cursor()
    query = ("SELECT title, COUNT(*) as noofviews "
             "FROM articles, log "
             "WHERE log.path LIKE CONCAT('%', slug) "
             "GROUP BY title "
             "ORDER BY noofviews DESC "
             "LIMIT 3;")
    c.execute(query)
    row = c.fetchone()
    while row is not None:
        print("\t" + row[0] + " - " + str(row[1]) + " views")
        row = c.fetchone()


def query2():
    '''This function executes the second query
    and prints a well-formatted output for the same.'''
    c = db.cursor()
    query = ("SELECT name, COUNT(*) as noofviews "
             "FROM articles, authors, log "
             "WHERE log.path LIKE CONCAT('%', slug) "
             "AND articles.author = authors.id "
             "GROUP BY name "
             "ORDER BY noofviews desc;")
    c.execute(query)
    row = c.fetchone()
    while row is not None:
        print("\t" + row[0] + " - " + str(row[1]) + " views")
        row = c.fetchone()


def query3():
    '''This function executes the third query
    and prints a well-formatted output for the same.'''
    c = db.cursor()
    query = ("SELECT to_char(time, 'FMMonth dd, yyyy'), percent "
             "FROM finalpercents "
             "WHERE percent > 1;")
    c.execute(query)
    row = c.fetchone()
    while row is not None:
        print("\t" + row[0] + " - " + str(row[1]) + "%")
        row = c.fetchone()

db = psycopg2.connect(database=DBNAME)
print('')
print('1. What are the most popular three articles of all time?')
query1()
print('')
print('2. Who are the most popular article authors of all time?')
query2()
print('')
print('3. On which days did more than 1% of requests lead to errors?')
query3()
print('')
db.close()
