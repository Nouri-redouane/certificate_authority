"""les étapes li lazem njouzo 3lihoum pour créer une CA et gèrer les certif numérique:
1) gènèrer une clé privé et une clé publique pour la CA
2) créer un certif auto signé avec la clé privé pour la CA  (ki hwst pourquoi :
9alk its the first step in establishing a trust infrastructure for issuing digital certeficates .
3) créer une CSR (certificate Signing Request ) pour les entités qui demandent un certif
elle va contenir les informations sur le client (nom de l'entité , pays , address.. )
4) signer les CSR avec la clé privé du CA pour générer le certif numérique
"""
############################################################### code #####

# généralement cryptography lazem tala3ha (pip install cryptography)







from cryptography import x509 # c'est la nomre utilisé pour créer les certif (chouf fl cours te3 belkhir )
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
import datetime

# Generate a public/private key pair for the CA
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Create a self-signed certificate for the CA using the private key
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COMMON_NAME, u'MyCA'),
    
])
issuer_cert = x509.CertificateBuilder().subject_name(
    subject
).issuer_name(
    issuer
).public_key(
    public_key
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    datetime.datetime.utcnow()
).not_valid_after(
    # Set the expiration time of the CA's certificate here
    datetime.datetime.utcnow() + datetime.timedelta(days=365)
).add_extension(
    x509.BasicConstraints(ca=True, path_length=None), critical=True
).sign(private_key, hashes.SHA256())
#This creates a self-signed digital certificate for the CA using the private key generated in step 2. The certificate contains information about the CA, such as its name, public key, and expiration date. It also includes an extension that identifies the certificate as a CA certificate and sets its path length constraint to None.





# Save the CA's private key and certificate to files
with open("ca.key", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ))
with open("ca.crt", "wb") as f:
    f.write(issuer_cert.public_bytes(
        encoding=serialization.Encoding.PEM,
    ))

# Generate a public/private key pair for the entity that needs a digital certificate
entity_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
entity_public_key = entity_private_key.public_key()
#This creates another RSA key pair consisting of a private key and a corresponding public key, which will be used by an entity that needs a digital certificate.

# Create a Certificate Signing Request (CSR) for the entity
subject = x509.Name([
    x509.NameAttribute(NameOID.COMMON_NAME, u'MyEntity'),
   
])
csr = x509.CertificateSigningRequestBuilder().subject_name(
    subject
).add_extension(
    x509.BasicConstraints(ca=False, path_length=None), critical=True
).sign(entity_private_key, hashes.SHA256())

# Sign the CSR with the CA's private key to generate a digital certificate for the entity
builder = x509.CertificateBuilder().subject_name(
    csr.subject
).issuer_name(
    issuer
).public_key(
    entity_public_key
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    datetime.datetime.utcnow()
).not_valid_after(
    # Set the expiration time of the entity's certificate here
    datetime.datetime.utcnow() + datetime.timedelta(days=365)
).add_extension(
    x509.SubjectAlternativeName([x509.DNSName(u"localhost")]),
    critical=False,
).sign(private_key, hashes.SHA256())

# Save the entity's private key and certificate to files
with open("entity.key", "wb") as f:
    f.write(entity_private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ))
with open("entity.crt", "wb") as f:
    f.write(builder.public_bytes(
        encoding=serialization.Encoding.PEM,
    ))
