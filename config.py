# ==========================================
# MASTER CONFIGURATION CHEAT SHEET
# Fill these in with your unique assigned values from the Exam Portal!
# ==========================================

# 1. Your IITM Email
EMAIL = "23f3004032@ds.study.iitm.ac.in"

# 2. Q1: CORS Allowed Origin
Q1_ALLOWED_ORIGIN = "https://dash-yr6yeq.example.com"

# 3. Q2: OAuth JWKS (Issuer, Audience, and Public Key)
ISSUER = "https://idp.exam.local"
AUDIENCE = "tds-5m86sjkh.apps.exam.local"
PUBLIC_KEY_PEM = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2okOHspNjgA+2rTLbeuY
cxiP/hG8C6Sb9iwg3yiLAA4HCnpITcbWCSelbvbYGuc3EbNy4xFyf5Cbj5DHJMID
EkryOgyd2giIIIBOUBj8S63uGcnRpOBh9NFatfNwheKuzsPuVNldu6A9cNteNpXc
WyJjG2axVfmq7i6SuKr1JoWYG7xTTAvKPujSl4OtsQfO3h5NepzdfXpr28oNnzfW
ed+zclR6BcmNNo/WVfJ4xyCLSf0BCOgdTgW6PdaChd1l9VDetJZVEgC5tkyvXsfI
SI6iyrYbKR0NEBSqq4XkadEjsCs4F1RncsS4LlgniT7GlkL9Mce3b0wGLs9/7ZIX
dQIDAQAB
-----END PUBLIC KEY-----"""

# 4. Q3: 12-Factor Config (Manually merge the variables)
Q3_PORT = 8216
Q3_WORKERS = 16
Q3_DEBUG = False
Q3_LOG_LEVEL = "error"

# 5. Q5: Analytics
Q5_API_KEY = "ak_pczjmhoz501ld4dejpc2oo9m"

# 6. Q9: Idempotency & Rate Limit
Q9_TOTAL_ORDERS = 59
Q9_RATE_LIMIT = 18

# 7. Q10: Middleware Rate Limit
Q10_ALLOWED_ORIGIN = "https://app-oe8q94.example.com"
Q10_RATE_LIMIT = 9

# ==========================================
# FIXED VARIABLES (Do not change these)
# ==========================================
EXAM_PORTAL_ORIGIN = "https://exam.sanand.workers.dev"
