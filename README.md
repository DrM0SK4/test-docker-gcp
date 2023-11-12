
cd gcp-functionA
docker build . -f dockerfile.functiona -t functiona
docker run -p 8081:8080 functiona

cd gcp-functionB
docker build . -f dockerfile.functionb -t functionb
docker run -p 8080:8080 functionb
