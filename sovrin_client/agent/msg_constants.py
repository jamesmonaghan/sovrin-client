# REQUEST MSGS TO AGENT
ACCEPT_INVITE = 'ACCEPT_INVITE'
REQUEST_CLAIM = 'REQUEST_CLAIM'
CLAIM_PROOF = 'CLAIM_PROOF'
REQ_AVAIL_CLAIMS = 'REQ_AVAIL_CLAIMS'

# RESPONSE MSGS FROM AGENT
INVITE_ACCEPTED = "INVITE_ACCEPTED"
AVAIL_CLAIM_LIST = 'AVAIL_CLAIM_LIST'
CLAIM = 'CLAIM'
CLAIM_PROOF_STATUS = 'CLAIM_PROOF_STATUS'
NEW_AVAILABLE_CLAIMS = "NEW_AVAILABLE_CLAIMS"

CLAIM_REQ_FIELD = 'claimReq'
CLAIM_FIELD = 'claim'
PROOF_FIELD = 'proof'
PROOF_INPUT_FIELD = 'proofInput'
REVEALED_ATTRS_FIELD = 'revealedAttrs'

# Other
CLAIM_NAME_FIELD = "claimName"
REF_REQUEST_ID = "refRequestId"

"""
ACCEPT_INVITE
{
    "type": 'ACCEPT_INVITE',
    "identifier": <id>,
    "nonce": <nonce>,
    "signature" : <sig>
}


AVAIL_CLAIM_LIST
{
    'type': 'AVAIL_CLAIM_LIST',
    'claims_list': [
        "Name": "Transcript",
        "Version": "1.2",
        "Definition": {
            "Attributes": {
                "student_name": "string",
                "ssn": "int",
                "degree": "string",
                "year": "string",
                "status": "string"
            }
        }
    ],
    "signature" : <sig>
}

AVAIL_CLAIM_LIST
{
    'type': 'AVAIL_CLAIM_LIST',
    'claims_list': [
        "Name": "Transcript",
        "Version": "1.2",
        "Definition": {
            "Attributes": {
                "student_name": "string",
                "ssn": "int",
                "degree": "string",
                "year": "string",
                "status": "string"
            }
        }
    ],
    "signature" : <sig>
}

"""
