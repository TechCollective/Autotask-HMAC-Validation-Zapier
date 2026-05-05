"""
This is a python script to validate the HMAC signature of an Autotask webhook.

It is specifically designed to work in Zapier. The code is written to be used in the Zapier Code step.

See README.md for implementation details.
"""
import json
import hmac
import hashlib
import base64
from typing import Optional

def validate_autotask_hmac_signature(sig: str, body: str, secret: str) -> Optional[dict]:
    """
    Verify AutoTask HMAC signature - requires signature, raw request body and secret
    """
    if sig.startswith('sha1='):
        sig = sig[5:]

    computed_hash = hmac.new(
        key=secret.encode(),
        msg=body.encode(),
        digestmod=hashlib.sha1
    ).digest()

    encoded_hash = base64.b64encode(computed_hash).decode()

    if not hmac.compare_digest(encoded_hash, sig):
        raise ValueError("Invalid HMAC Signature")

    body = json.loads(raw_body)
    # Flatten Fields into body
    body.update(body["Fields"])
    del body["Fields"]

    return { "body": body, "verified": True}

# input_data is provided by Zapier
return validate_autotask_hmac_signature(sig=input_data.get('hook', ''), # Mapped to the raw body of the webhook
                                        body=input_data.get('raw_body', ''), # The secret key you gave AutoTask
                                        secret=input_data.get('secret_key', '')) # The header calculated by AutoTask
