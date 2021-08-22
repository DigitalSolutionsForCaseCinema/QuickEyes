CREATE TABLE video_processing
(
    id SERIAL PRIMARY KEY,
    video_name VARCHAR(255) NOT NULL,
    time_from INTEGER NOT NULL DEFAULT 0,
    time_to INTEGER NOT NULL DEFAULT -1,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    status VARCHAR(255) NOT NULL DEFAULT 'queued'
);

--rollback DROP TABLE IF EXISTS video_processing;