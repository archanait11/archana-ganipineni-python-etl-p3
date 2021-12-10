
create_schema = ('''
    create schema if not exists petl3
''')

create_table = ('''
    create table if not exists petl3.viable_countys(
        geo_id	int,
        state	text,
        county	text,
        sales_vector	int

    )
''')

truncate_table = ('''
    TRUNCATE TABLE petl3.viable_countys
''')

insert_viable_countys = ('''
    INSERT INTO petl3.viable_countys 
    VALUES (%s,%s,%s,%s)
''')
