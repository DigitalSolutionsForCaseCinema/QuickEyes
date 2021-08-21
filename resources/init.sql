CREATE TABLE videos
(
    name varchar(255) primary key,
    created_at timestamp default now(),
    status varchar(255)
);

--rollback DROP TABLE IF EXISTS videos;