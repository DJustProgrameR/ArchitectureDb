#!/bin/bash

for file in /migrations/*.sql; do
    filename=$(basename "$file")
    version=${filename:1:14}
    if [[ "$version" -gt $LAST_MIGRATION_VERSION ]]; then
        echo "Stopping migration at version $version"
        break
    fi
    echo "Executing migration $version"
    psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -f "$file"
done

for file in /migrations/*.sh; do
    filename=$(basename "$file")
    version=${filename:1:14}
    if [[ "$version" -gt $LAST_MIGRATION_VERSION ]]; then
        echo "Stopping migration at version $version"
        break
    fi
    echo "Executing migration $version"
    bash $file
done