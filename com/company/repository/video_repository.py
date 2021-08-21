import psycopg2

connection = psycopg2.connect(dbname='video_editor', user='postgres',
                              password='admin', host='localhost')


def insert_video(video_name):
    with connection.cursor() as cursor:
        sql = "INSERT INTO videos (name, status) VALUES (%s, %s)"
        cursor.execute(sql, (video_name, 'queued'))
        connection.commit()


def set_status(video_name, status):
    with connection.cursor() as cursor:
        sql = "UPDATE videos SET status = %s WHERE name = %s"
        cursor.execute(sql, (status, video_name))
        connection.commit()
