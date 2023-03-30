
 
CREATE TABLE IF NOT EXISTS Serveur
(
    id_serveur INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    ip_addr VARCHAR(12)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS ReverseProxy
(
    id_proxy INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    id_serveur INT REFERENCES Serveur(id_serveur)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS ProxyLoc
(
    id_proxy_loc INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    proxy_bind VARCHAR(50),
    proxy_pass VARCHAR(50),
    location VARCHAR(50)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS WebServer
(
    nom_serveur VARCHAR(50) PRIMARY KEY NOT NULL,
    default_route VARCHAR(50),
    location VARCHAR(50),
    error_page VARCHAR(50),
    id_serveur INT REFERENCES Serveur(id_serveur)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS LoadBalancer
(
    id_LB INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    id_serveur INT REFERENCES Serveur(id_serveur),
    location VARCHAR(50),
    proxy_pass VARCHAR(50),
    id_type INT REFERENCES TypeLoadBalancer(id_type)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS TypeLoadBalancer
(
    id_type INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nom_type VARCHAR(50),
    serveur1 VARCHAR(50),
    serveur2 VARCHAR(50)
) ENGINE=InnoDB;
