import psycopg2

connection = psycopg2.connect(dbname='video_editor', user='postgres',
                              password='admin', host='localhost')


def insert_video(video_name, time_from, time_to):
    with connection.cursor() as cursor:
        sql = "INSERT INTO video_processing (video_name, time_from, time_to, status) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (video_name, time_from, time_to, 'queued'))
        connection.commit()


def set_status(video_name, time_from, time_to, status):
    with connection.cursor() as cursor:
        sql = "UPDATE video_processing SET status = %s " \
              "WHERE video_name = %s AND time_from = %s AND time_to = %s"
        cursor.execute(sql, (status, video_name, time_from, time_to))
        connection.commit()
