
cd gcp-functionA
docker build gcp-functionA -t functiona
docker run -p 8081:8080 functiona

cd gcp-functionB
docker build gcp-functionB -t functionb
docker run -p 8080:8080 functionb
