# Core-geonetwork
## Installation
You need to have JDK 1.7+

Add path to JDK into ```JAVA_HOME```

Install maven package. Example for CentOS:
```sh
$ yum install maven
```
## Deploying
```sh
$ git clone https://github.com/CedrikNikita/core-geonetwork.git
$ cd core-geonetwork
$ mvn clean install -DskipTests
$ cd web
$ mvn jetty:run -Penv-dev
```

You have to install Python 2.7+

Required Python modules:
- pdfminer
- wget
