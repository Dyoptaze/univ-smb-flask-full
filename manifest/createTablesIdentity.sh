
CREATE TABLE IF NOT EXISTS Utilisateur
(
    id_user INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nom VARCHAR(50),
    prenom VARCHAR(50),
    naissance DATE
);

CREATE TABLE IF NOT EXISTS Authentification 
(
    login VARCHAR(50) PRIMARY KEY NOT NULL,
    password VARCHAR(50) NOT NULL,
    id_user VARCHAR(50) REFERENCES utilisateur(id_user)
);
