from cryptography.hazmat.primitives.asymmetric import padding
from cryptography import x509
from datetime import datetime

def verify(filename):
    cert_to_check = x509.load_pem_x509_certificate(data=open("uploads/"+filename, "rb").read())
    ca_cer = x509.load_pem_x509_certificate(data=open("ca.crt", "rb").read())
    issuer_public_key = ca_cer.public_key()

    # Vérification de la période de validité
    now = datetime.now()
    if now < cert_to_check.not_valid_before or now > cert_to_check.not_valid_after:
        return False
    
    try:
        issuer_public_key.verify(
            cert_to_check.signature,
            cert_to_check.tbs_certificate_bytes,
            padding.PKCS1v15(),
            cert_to_check.signature_hash_algorithm,
        )
        
        return True
    except:
        return False
