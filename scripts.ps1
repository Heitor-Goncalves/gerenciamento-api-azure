docker build -t api-filmes-app:latest .

docker run -d -p 80:80 api-filmes-app:latest
# create resource group and container registry
az group create --name api-container-group --location eastus

# create container registry
az acr create --resource-group api-container-group --name heitoracrapi --sku Basic

#login to the container registry
az acr login --name heitoracrapi

# tag the image
docker tag api-filmes-app:latest heitoracrapi.azurecr.io/api-filmes-app:latest

# push the image to the container registry
docker push heitoracrapi.azurecr.io/api-filmes-app:latest

#containerID = heitoracrapi.azurecr.io/api-filmes-app:latest
#user = heitoracrapi
#password = L0XhIyf03o/xbB9bJUTH2ujqacE3myoKSPhgREqBqz+ACRDcElKR

#create Environment container app
az containerapp env create --name api-filmes-env --resource-group api-container-group --location eastus

#create container app
az containerapp create --name api-filmes-app --resource-group api-container-group --environment api-filmes-env --image heitoracrapi.azurecr.io/api-filmes-app:latest --target-port 80 --ingress 'external' --registry-server heitoracrapi.azurecr.io --registry-username heitoracrapi --registry-password 0XhIyf03o/xbB9bJUTH2ujqacE3myoKSPhgREqBqz+ACRDcElKR

# update container app with new image
az containerapp update --name api-filmes-app --resource-group api-container-group --image heitoracrapi.azurecr.io/api-filmes-app:latest

az containerapp registry set \
  --name api-filmes-app \
  --resource-group api-container-group \
  --server heitoracrapi.azurecr.io \
  --identity system

  az containerapp create \
  --name api-filmes-app \
  --resource-group api-container-group \
  --image heitoracrapi.azurecr.io/api-filmes-app:latest \
  --environment api-filmes-env \
  --ingress external \
  --target-port 5000 \
  --registry-server heitoracrapi.azurecr.io \
  --registry-identity system \
  --system-assigned

  az acr login --name heitoracrapi
docker tag api-filmes-app:latest heitoracrapi.azurecr.io/api-filmes-app:latest
docker push heitoracrapi.azurecr.io/api-filmes-app:latest
