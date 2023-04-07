from cryptography import x509
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives.serialization import load_pem_private_key
import datetime


def generate_certificate(organization, common_name, country, state, city):
    # Generate a private key for the CA
    key_data = open("keys/ca.key", "rb").read()
    ca_private_key = load_pem_private_key(key_data, password=None)

    # Create a self-signed certificate for the CA using the private key
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COMMON_NAME,
                           u'USTHB certificate authority'),

    ])

    # Generate a public/private key pair for the entity that needs a digital certificate
    entity_private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    entity_public_key = entity_private_key.public_key()
    # This creates another RSA key pair consisting of a private key and a corresponding public key, which will be used by an entity that needs a digital certificate.

    # Create a Certificate Signing Request (CSR) for the entity

    # Create a certificate signing request (CSR)
    csr_subject = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, country),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, state),
        x509.NameAttribute(NameOID.LOCALITY_NAME, city),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, organization),
        x509.NameAttribute(NameOID.COMMON_NAME, common_name)
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
        x509.SubjectAlternativeName([x509.DNSName(common_name)]),
        critical=False,
    ).sign(ca_private_key, hashes.SHA256())

    # Save the entity's private key and certificate to files
    with open("generated/entity.key", "wb") as f:
        f.write(entity_private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))
    with open("generated/entity.crt", "wb") as f:
        f.write(builder.public_bytes(
            encoding=serialization.Encoding.PEM,
        ))
