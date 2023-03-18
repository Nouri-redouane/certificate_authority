from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

cert_file = open('')
cert_data = cert_file.read()
cert = x509.load_der_x509_certificate(data=cert_data)

# chain contains the Let's Encrypt certificate 
chain_file = open('')
chain_data = chain_file.read()
chain = x509.load_pem_x509_certificate(data=chain_data, backend=default_backend())

public_key = chain.public_key()

verifier = public_key.verifier(
                signature = cert.signature,
                padding = padding.PSS(
                              mgf = padding.MGF1(hashes.SHA256()),
                              salt_length = padding.PSS.MAX_LENGTH),
                algorithm = hashes.SHA256())

verifier.update(cert.tbs_certificate_bytes)
verifier.verify()

# throws an InvalidSignature exception, but using verifying with openssl works.