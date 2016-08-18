import csv
import psycopg2

conn = psycopg2.connect(database="resilienceserver", user="metrica", password="centrality", host="localhost")
cur = conn.cursor()

insert_paper_query = "INSERT INTO papers_paper (doi, title, publication_year, abstract, times_cited, source_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
insert_source_query = "INSERT INTO papers_source (name) VALUES (%s) RETURNING id"
insert_author_query = "INSERT INTO papers_author (name) VALUES (%s) RETURNING id"
insert_paper_author_relationship_query = "INSERT INTO papers_paper_authors (paper_id, author_id) VALUES (%s, %s)"

get_author_by_name_query = "SELECT * FROM papers_author WHERE name = %s;"
get_source_by_name_query = "SELECT * FROM papers_source WHERE name = %s;"

# cur.execute(insert_author_query, ("Julio",))
# cur.execute(get_author_by_name_query, ("Julio",))
#
# res = cur.fetchone()
#
# print(res)
# cur.execute(insert_author_query, ("Tizghadam, A.",))

with open('papers.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    source = 'no_source'
    source_id = -100
    for row in csv_reader:
        if i == 0:
            i = 1
            continue
        if row[0] != source and row[0] != '':
            source = row[0]
            ## Insert source
            cur.execute(insert_source_query, (source,))
            res = cur.fetchall()
            source_id = res[0][0]
            continue
        if row[2] == '-' or row[2] == '' or row[2] == ' ':
            continue
        if row[10] != '2':
            continue
        title = row[2]
        authors = ''
        if source == 'IEEE' or source == 'Web of Science':
            authors = [x.strip(" ") for x in row[3].split(";")]
        else:
            authors = [x.strip(" ") for x in row[3].split(",")]
        abstract = row[4]
        year = row[5]
        doi = row[6]

        # SQL
        ## Insert authors
        inserted_author_ids = []
        for author in authors:
            cur.execute(get_author_by_name_query, (author,))
            res = cur.fetchall()
            if len(res) == 0:
                cur.execute(insert_author_query, (author,))
                res = cur.fetchall()
                inserted_author_ids.append(res[0][0])
            else:
                inserted_author_ids.append(res[0][0])
        ## Insert paper
        cur.execute(insert_paper_query, (doi, title, year, abstract, 0, source_id,))
        res = cur.fetchall()
        paper_id = res[0][0]
        ## Insert paper-author relationships
        for author_id in inserted_author_ids:
            cur.execute(insert_paper_author_relationship_query, (paper_id, author_id,))

conn.commit()
cur.close()
conn.close()
