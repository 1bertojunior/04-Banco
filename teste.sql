
CREATE TABLE client (
	id INT(4) PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(25) NOT NULL,
    surname VARCHAR(25) NOT NULL,
    cpf VARCHAR(11) NOT NULL,
    password VARCHAR(32) NOT NULL
);
CREATE TABLE historic(
	id INT(4) PRIMARY KEY AUTO_INCREMENT,
    historic text NOT NULL,
    fk_client INT(4) NOT NULL,
    FOREIGN KEY (fk_client ) REFERENCES client(id)    
);
CREATE TABLE account(
	id INT(4) PRIMARY KEY AUTO_INCREMENT,
    balance FLOAT(10,2) default 0.0,
    limited FLOAT(10,2) default 0.0,
    fk_client INT(4) NOT NULL,
    fk_historic INT(4) NOT NULL,
    FOREIGN KEY (fk_client ) REFERENCES client(id),
    FOREIGN KEY (fk_historic) REFERENCES historic(id)
);

INSERT INTO client(
);