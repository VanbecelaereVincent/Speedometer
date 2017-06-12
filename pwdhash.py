import hashlib
import binascii
import os

from dbconn import DbConnection

# voorbeeld DB schema ter referentie
# NB: hash en salt hebben vaste lengte
#   --> datatype CHAR( aantal bytes x 2 )
ddl = """
CREATE TABLE `users` (
  `username` VARCHAR(512) NOT NULL,
  `pwd_hash` CHAR(64) NOT NULL,   
  `pwd_salt` CHAR(32) NOT NULL,
  PRIMARY KEY (`username`)
)
COLLATE='latin1_swedish_ci'
ENGINE=InnoDB
;
"""

db_ = DbConnection(database="project1")


def add_user(username, password):
    if db_.query("SELECT * FROM users WHERE username=%s", (username, )):
        print("Gebruiker bestaat al!")
        return False

    # 1) paswoord omzetten naar type bytes
    pwd_bytes = bytes(password, 'utf-8')

    # 2) random salt genereren, resultaat is al in bytes
    salt_bytes = os.urandom(16)

    # 3) hash berekenen
    hash_bytes = hashlib.pbkdf2_hmac('sha256', pwd_bytes, salt_bytes, 100000)

    # 4) omzetten naar hex-string
    salt_string = binascii.hexlify(salt_bytes).decode('utf-8')
    hash_string = binascii.hexlify(hash_bytes).decode('utf-8')

    # 5) opslaan in db
    # PyCharm valt over de syntax maar dat geeft niet
    sql = (
        'INSERT INTO project1.users (username, pwd_hash, pwd_salt) '
        'VALUES ( %(new_name)s, %(new_hash)s, %(new_salt)s );'
    )
    params = {
        'new_name': username,
        'new_hash': hash_string,
        'new_salt': salt_string,
    }
    # uitvoeren & klaar!
    result = db_.execute(sql, params)
    print(f'Gebruiker {username} toegevoegd')
    return result


def verify_credentials(username, password):

    # 1) hash en salt opvragen uit db
    sql = 'SELECT pwd_hash, pwd_salt FROM project1.users WHERE username=%(check_name)s;'
    params = {
        'check_name': username,
    }
    result = db_.query(sql, params, True)

    # als gebruiker niet bestaat moeten we niet verder kijken
    if not result:
        return False

    # 'username' is PK dus er kan maar 1 rij zijn
    db_user = result[0]

    # hash en salt uit resultaat halen
    db_hash_string = db_user['pwd_hash']
    db_salt_string = db_user['pwd_salt']

    # 2) hash berekenen met INGEVOERD WACHTWOORD en OPGESLAGEN SALT
    # eerst beide weer omzetten naar type bytes
    pwd_bytes = bytes(password, 'utf_8')
    db_salt_bytes = binascii.unhexlify(db_salt_string)

    # nieuwe hash berekenen
    hash_bytes = hashlib.pbkdf2_hmac('sha256', pwd_bytes, db_salt_bytes, 100000)

    # omzetten naar string om te kunnen vergelijken
    hash_string = binascii.hexlify(hash_bytes).decode('utf-8')

    # 3) enkel als het wachtwoord juist was komt de hash overeen
    return hash_string == db_hash_string

if __name__ == "__main__":
    if input("Table 'users' will be truncated, continue? (y/n)").lower() == "y":
        db_.execute("DELETE FROM users;")

        add_user('myuser', 'mypassword')
        add_user('youruser', 'yourpassword')
        print(verify_credentials('myuser', 'mypassword'))
        print(verify_credentials('myuser', 'wrongpassword'))
        print(verify_credentials('wronguser', 'anypassword'))
        print(verify_credentials('youruser', 'yourpassword'))

        add_user('firstuser', 'samepassword')
        add_user('otheruser', 'samepassword')
        hashes = db_.query("SELECT pwd_hash FROM users WHERE username IN ('firstuser', 'otheruser');", dictionary=True)
        print(hashes[0])
        print(hashes[1])

        add_user("'; DROP TABLE users; --", "'; SELECT username, password FROM users; --")

