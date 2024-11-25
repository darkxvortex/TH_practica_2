FROM ubuntu:22.04
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y openjdk-11-jdk maven iputils-ping

RUN mkdir -p /opt/shop/
WORKDIR /opt/shop/
COPY pom.xml .
RUN mvn -B dependency:resolve-plugins dependency:resolve
COPY . .
RUN mvn -B clean package
CMD ["java", "-jar", "target/shop-0.0.1-SNAPSHOT.jar"]
