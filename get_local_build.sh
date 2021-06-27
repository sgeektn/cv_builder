docker exec cv_builder /bin/bash local.sh
mkdir results
chmod 777 results
docker cp cv_builder:/usr/src/app/localversion.tar.gz results

