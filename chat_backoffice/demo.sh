export KUBECONFIG=$PWD/../rit-tst-1.yaml

# create ns
kubectl create namespace client02
kubectl label namespaces client02 istio-injection=enabled --overwrite=true

# deploy app
helm install --set name=client02 client02 --set domain=my.example.com . -n client02

# test
curl -L https://my.example.com/ --resolve my.example.com:443:171.22.246.28

curl -k -v -L https://tim.my.example.com -L --resolve admin.my.example.com:443:171.22.246.28 --resolve tim.my.example.com:443:171.22.246.28

curl -k -v -L https://ruuter.my.example.com/  --resolve ruuter.my.example.com:443:171.22.246.28


