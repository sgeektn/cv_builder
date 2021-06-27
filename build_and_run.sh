docker stop cv_builder
docker rm cv_builder
docker build . --tag "cv_builder" 
docker run -d --name cv_builder -p 8000:8000 cv_builder