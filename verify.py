from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

cert_file = open("entity.crt", "rb")
cert_data = cert_file.read()
cert = x509.load_pem_x509_certificate(data=cert_data)

# chain contains the Let's Encrypt certificate 
chain_file = open("ca.crt", "rb")
chain_data = chain_file.read()
chain = x509.load_pem_x509_certificate(data=chain_data)

public_key = chain.public_key()
print(cert.signature)
verifier = public_key.verify(
                signature = cert.signature,
                data=cert_data,
                padding = padding.PKCS1v15(),
                algorithm = hashes.SHA256())
verifier.update(cert.tbs_certificate_bytes)
verifier.verify()

# throws an InvalidSignature exception, but using verifying with openssl works.