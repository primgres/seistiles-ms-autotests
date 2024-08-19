BASE_URL = "https://oec-prod-dsif2.openearth.io/services/seistiles-job-orchestrator-qa"
TOKEN_URL = "https://dssecurity.oec-prod-dsif2.openearth.io"
SUCCESSFUL_STATUS_CODE = 200
MAX_GEN_TIMEOUT = 300
HEADERS = {"Content-Type": "application/json"}
HEALTHCHECK_ENDPOINT = "/msp/health"
TILES_GEN_ENDPOINT = "/msp/api/v1/seismic-tiles-file-system"
PATCH_GEN_ENDPOINT = "/msp/api/v1/seismic-patches"
TOKEN_ENDPOINT = "/auth/realms/DecisionSpace_Integration_Server/protocol/openid-connect/token"
TILEGEN_DATA = [
    'data/payload_tilegen_positive_case1.json',
    'data/payload_tilegen_positive_case2.json',
    'data/payload_tilegen_positive_case3.json',
    'data/payload_tilegen_positive_case4.json',
    'data/payload_tilegen_positive_case5.json'
]
PATCHGEN_DATA = [
    'data/payload_patchgen_positive_case1.json',
    'data/payload_patchgen_positive_case2.json',
    'data/payload_patchgen_positive_case3.json',
    'data/payload_patchgen_positive_case4.json',
    'data/payload_patchgen_positive_case5.json'
]
