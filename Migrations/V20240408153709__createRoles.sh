psql --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" << EOF
    CREATE ROLE reader;
    CREATE ROLE writer;

    GRANT SELECT ON ALL TABLES IN SCHEMA public TO reader;
    GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO writer;

    CREATE USER analytic;
    GRANT SELECT ON public.Login_log TO analytic;

    CREATE ROLE moderators WITH NOLOGIN;
    GRANT SELECT, INSERT, DELETE ON ALL TABLES IN SCHEMA public TO moderators;
EOF

MODERATORS="$(cat /config/env | grep "MODERATORS" | awk -F '=' '{print $2}')"

for moderator in $moderators
do
    psql -v user=$moderator --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" << EOF
        CREATE USER :user WITH PASSWORD 'password';
        GRANT CONNECT ON DATABASE postgres TO :user;
        GRANT :user TO moderators;
EOF
done
