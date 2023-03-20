from cryptography.hazmat.primitives.asymmetric import padding
from cryptography import x509

def verify(filename):

    cert_to_check = x509.load_pem_x509_certificate(data=open("uploads/"+filename, "rb").read())
    ca_cer = x509.load_pem_x509_certificate(data=open("ca.crt", "rb").read())
    issuer_public_key = ca_cer.public_key()

    try:
        issuer_public_key.verify(
            cert_to_check.signature,
            cert_to_check.tbs_certificate_bytes,
            # Depends on the algorithm used to create the certificate
            padding.PKCS1v15(),
            cert_to_check.signature_hash_algorithm,
        )
        
        return True
    except:
        return False