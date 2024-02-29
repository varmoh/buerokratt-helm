# Buerokratt Helm chart

A Helm chart for [Buerokratt](https://github.com/buerokratt) project 

#### Manual deploy  

##### Installing/upgrading using charts    

helm install project-name folder_of_charts/ -n namespace  

for example  

```
helm install byk chat_backoffice/ -n byk-test
```

When upgrading, replace `install` with `upgrade`

```
helm upgrade byk chat_backoffice/ -n byk-test
```

##### Installing/upgrading using tarball  

helm install charts/chart_backoffice-version.tgz -n namespace 

for ecxample  

```
helm install charts/chart_backoffice-0.1.49.tgz -n byk-test  
``` 

When upgrading, replace `install` with `upgrade` and chage the .tgz into latest version you have.

for example

```
helm upgrade byk charts/chart_backoffice-0.1.50.tgz -n byk-test
```  

#### Auto deploy   

Change the .env file accordingly

```
version: 0.1.49
```

This will start workflows.

First half of the workflow moves older version of tarball into charts/archive folder, assigns the given version for the new to be created tarball and then builds and publishes it.  
Second half of the workflow connects to k8s environment and either installs new project or upgrades the existing one.  
