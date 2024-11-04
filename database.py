from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://qnhHWnNi6Hnwnvz.root:3Z5TAyONBzX4adyS@gateway01.eu-central-1.prod.aws.tidbcloud.com/test?charset=utf8mb4"

engine = create_engine(db_connection_string, 
                       connect_args={
                          "ssl": {
                              "ca": "client-ssl/isrgrootx1.pem"
                          }
                      })


with engine.connect() as conn:
    result = conn.execute(text("select * from pilgrims"))
    pilgrims = []
    for row in result.all():
      pilgrims.append(row._mapping)
    

    # print(pilgrims)
    first_pilgrim = pilgrims[0]
    print(type(first_pilgrim))
    print(first_pilgrim)
    print(first_pilgrim['id'])
    print(first_pilgrim['pilgrim_name'])
    print(first_pilgrim['camp'])


    
    