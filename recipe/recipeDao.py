import cx_Oracle

def getConnection():
    try:
          conn=cx_Oracle.connect("hr/happy@localhost:1521/xe")
    except Exception as e:
          print(e)
    return conn

def recipeListData(page):
    conn=getConnection()
    cursor=conn.cursor()
    rowSize=12
    start=(rowSize*page)-(rowSize-1)
    end=(rowSize*page)
    sql=f"""
            SELECT no,title,poster,chef,num 
            FROM (SELECT no,title,poster,chef,rownum as num
            FROM (SELECT no,title,poster,chef
            FROM recipe ORDER BY no ASC))
            WHERE num BETWEEN {start} AND {end}
          """
    cursor.execute(sql)
    recipe_data=cursor.fetchall()
    cursor.close()
    conn.close()
    print(recipe_data)
    return recipe_data

def recipe_info(no):
    conn=getConnection()
    cursor=conn.cursor()
    sql=f"""
           SELECT no,title,poster FROM recipe 
           WHERE no={no}
          """
    cursor.execute(sql)
    info_data=cursor.fetchone()
    cursor.close()
    conn.close()
    return info_data
