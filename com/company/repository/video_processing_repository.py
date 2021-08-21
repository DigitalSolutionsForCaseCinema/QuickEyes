import psycopg2

connection = psycopg2.connect(dbname='video_editor', user='postgres',
                              password='admin', host='localhost')


def insert(video_name, time_from, time_to):
    with connection.cursor() as cursor:

        sql = "INSERT INTO video_processing ( video_name, time_from, time_to, status) " \
              "VALUES ( %s, %s, %s, %s);"
        cursor.execute(sql, (video_name, time_from, time_to, 'queued'))
        connection.commit()
        return select_video_processing_id(video_name, time_from, time_to)


def select_video_processing_id(video_name, time_from, time_to):
    with connection.cursor() as cursor:
        sql = "SELECT id FROM video_processing " \
              "WHERE video_name = %s AND " \
              "time_from = %s AND " \
              "time_to = %s " \
              "ORDER BY created_at DESC"
        cursor.execute(sql, (video_name, time_from, time_to))
        video_processing_id = cursor.fetchone()[0]
        connection.commit()

        return str(video_processing_id)


def set_status(video_processing_id, status):
    with connection.cursor() as cursor:
        sql = "UPDATE video_processing SET status = %s WHERE id = %s"
        cursor.execute(sql, (status, video_processing_id))
        connection.commit()
