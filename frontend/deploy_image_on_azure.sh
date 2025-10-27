source variable.sh

#creatre a container registry
creds=$(az acr credential show --resource-group "$ressource_group" --name "$registry_name")
username=$( echo "$creds" | jq -r '.username' )
password=$( echo "$creds" | jq -r '.passwords[0].value' )

docker login "$registry_fqdn" --username "$username" --password "$password"
docker tag "$image_to_deploy" "$registry_fqdn/$image_to_deploy"
docker push "$registry_fqdn/$image_to_deploy"
