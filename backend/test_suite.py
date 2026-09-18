import requests
import json
import time
import sys

BASE = "http://localhost:5000"

def log(msg):
    # Ensure safe ascii printing on Windows console
    print(msg.encode("ascii", errors="replace").decode("ascii"), flush=True)

def test_endpoint(name, method, path, params=None, json_data=None, timeout=45):
    url = f"{BASE}{path}"
    log(f"\n--- Testing [{name}] -> {path} ---")
    t0 = time.time()
    try:
        if method == "GET":
            r = requests.get(url, params=params, timeout=timeout)
        else:
            r = requests.post(url, json=json_data, timeout=timeout)
        elapsed = round(time.time() - t0, 2)
        log(f"Status: {r.status_code} ({elapsed}s)")
        if r.status_code != 200:
            log(f"ERROR Response: {r.text[:300]}")
            return False, r.status_code, None
        data = r.json()
        return True, r.status_code, data
    except Exception as e:
        log(f"EXCEPTION: {e}")
        return False, 0, None

def run_tests():
    results = {}

    # 1. Health
    ok, code, data = test_endpoint("Health", "GET", "/api/health")
    results["1. Health"] = "PASS" if ok and data.get("status") == "HEALTHY" else "FAIL"
    if ok:
        log(f"   Services: Ollama: {data.get('services',{}).get('ollama',{}).get('status')}, "
            f"Model: {data.get('services',{}).get('ollama',{}).get('model')}")

    # 2. Cache Stats
    ok, code, data = test_endpoint("Cache Stats", "GET", "/api/cache-stats")
    results["2. Cache Stats"] = "PASS" if ok and "total_cached_diseases" in data else "FAIL"

    # 3. Compound Analyzer (Aspirin)
    ok, code, data = test_endpoint(
        "Compound Analyzer", "GET", "/api/compound/analyze",
        params={"smiles": "CC(=O)OC1=CC=CC=C1C(=O)O"}
    )
    results["3. Compound Analyzer"] = "PASS" if ok and "descriptors" in data else "FAIL"
    if ok:
        desc = data.get("descriptors", {})
        log(f"   MW: {desc.get('mw')}, LogP: {desc.get('logp')}, Lipinski: {desc.get('lipinski_pass')}")

    # 4. Reverse Lookup
    ok, code, data = test_endpoint("Reverse Lookup", "GET", "/api/reverse-lookup", params={"query": "aspirin"})
    results["4. Reverse Lookup"] = "PASS" if ok and "top_off_targets" in data else "FAIL"
    if ok:
        log(f"   Target count: {len(data.get('top_off_targets', []))}")

    # 5. Pathway Retrieval
    ok, code, data = test_endpoint("Pathways", "GET", "/api/pathways", params={"gene": "PTGS2"})
    results["5. Pathways"] = "PASS" if ok and len(data.get("pathways", [])) > 0 else "FAIL"
    if ok:
        log(f"   Pathways retrieved: {len(data.get('pathways', []))}")

    # 6. Disease Explorer (Alzheimer's)
    ok, code, data = test_endpoint("Disease Explorer", "GET", "/api/repurpose", params={"disease": "Alzheimer's disease"}, timeout=120)
    results["6. Disease Explorer"] = "PASS" if ok and len(data.get("candidates", [])) > 0 else "FAIL"
    if ok:
        log(f"   Resolved: {data.get('resolvedName')}, Candidates: {len(data.get('candidates', []))}, "
            f"Cached: {data.get('fromCache')}")

    # 7. AI SAR Analysis
    ok, code, data = test_endpoint(
        "AI SAR Analysis", "GET", "/api/ai/sar-analysis",
        params={
            "smiles": "CC(=O)OC1=CC=CC=C1C(=O)O",
            "name": "Aspirin",
            "mw": "180.16",
            "logp": "1.2",
            "tpsa": "63.6",
            "hbd": "1",
            "hba": "4",
            "rotb": "3",
            "lipinski": "true",
            "pains": "false"
        },
        timeout=60
    )
    results["7. AI SAR Analysis"] = "PASS" if ok and "sar_analysis" in data else "FAIL"
    if ok:
        log(f"   AI Powered: {data.get('aiPowered')}, Model: {data.get('model')}")
        log(f"   SAR Excerpt: {data.get('sar_analysis', '')[:120]}...")

    # 8. AI Pathway Crosstalk
    ok, code, data = test_endpoint(
        "AI Pathway Crosstalk", "GET", "/api/ai/pathway-crosstalk",
        params={
            "drug": "Aspirin",
            "targets": "PTGS2,PTGS1",
            "pathways": "Arachidonic acid metabolism, Prostaglandin synthesis",
            "disease": "Alzheimer's disease"
        },
        timeout=60
    )
    results["8. AI Pathway Crosstalk"] = "PASS" if ok and "crosstalk_analysis" in data else "FAIL"
    if ok:
        log(f"   AI Powered: {data.get('aiPowered')}, Model: {data.get('model')}")
        log(f"   Crosstalk Excerpt: {data.get('crosstalk_analysis', '')[:120]}...")

    # 9. AI Head-to-Head Comparison Synthesis
    ok, code, data = test_endpoint(
        "AI Comparison Synthesis", "POST", "/api/ai/compare-synthesis",
        json_data={
            "disease": "Alzheimer's disease",
            "candidates": [
                {"name": "Donepezil", "gene": "ACHE", "score": 0.94, "phase": "Phase IV Approved", "origUse": "Alzheimer's"},
                {"name": "Galantamine", "gene": "ACHE", "score": 0.88, "phase": "Phase IV Approved", "origUse": "Dementia"},
                {"name": "Memantine", "gene": "GRIN1", "score": 0.85, "phase": "Phase IV Approved", "origUse": "Alzheimer's"}
            ]
        },
        timeout=60
    )
    results["9. AI Comparison Synthesis"] = "PASS" if ok and "synthesis" in data else "FAIL"
    if ok:
        log(f"   AI Powered: {data.get('aiPowered')}, Model: {data.get('model')}")
        log(f"   Synthesis Excerpt: {data.get('synthesis', '')[:120]}...")

    # 10. AI Deepen Rationale
    ok, code, data = test_endpoint(
        "AI Deepen Rationale", "GET", "/api/explain",
        params={
            "drug": "Donepezil",
            "disease": "Alzheimer's disease",
            "target_gene": "ACHE",
            "target_name": "Acetylcholinesterase",
            "score": "0.94",
            "stage": "Phase IV Approved",
            "original_use": "Mild to moderate Alzheimer's dementia"
        },
        timeout=60
    )
    results["10. AI Deepen Rationale"] = "PASS" if ok and "explanation" in data else "FAIL"
    if ok:
        log(f"   AI Powered: {data.get('aiPowered')}, Model: {data.get('model')}")
        log(f"   Rationale Excerpt: {data.get('explanation', '')[:120]}...")

    log("\n==========================================")
    log("          REMEDX TEST SUMMARY             ")
    log("==========================================")
    all_pass = True
    for test, status in results.items():
        log(f"  {test.ljust(30)}: {status}")
        if status != "PASS":
            all_pass = False
    log("==========================================")
    log(f"OVERALL RESULT: {'ALL PASS' if all_pass else 'SOME TESTS FAILED'}")

if __name__ == "__main__":
    run_tests()
