FROM maven:3-eclipse-temurin-17-focal
WORKDIR /app
COPY pom.xml .
# Force download of dependencies to optimize Docker layers
RUN mvn verify --fail-never
COPY . .
CMD ["mvn", "spring-boot:run"]