# ReMedX 🧬💊
> **Next-Generation AI Precision Drug Repurposing & Polypharmacology Studio**  
> *Transforming pharmaceutical discovery from decades to seconds by synthesizing genomics, cheminformatics, biological pathway crosstalk, and local AI reasoning.*

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.3-green.svg)](https://flask.palletsprojects.com/)
[![Ollama](https://img.shields.io/badge/Ollama-gemma3%3Alatest-orange.svg)](https://ollama.com/)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Hackathon%20Production%20Ready-brightgreen.svg)]()

---

## 📖 Overview

Bringing a novel pharmaceutical compound from bench to bedside typically requires **10–15 years** and over **$2.6 billion**, with failure rates exceeding 90% in clinical trials. 

**ReMedX** inverts this paradigm through algorithmic precision drug repurposing. By fusing genomic disease associations (Open Targets Platform), clinical bioactivities (ChEMBL), deep cheminformatics and ADMET screening (RDKit), biological pathway networks (Reactome), and local LLM reasoning (Ollama Gemma 3), ReMedX discovers high-confidence, non-obvious therapeutic hypotheses for established, clinically-validated molecules.

```
+-----------------------------------------------------------------------------------------------+
|                                       ReMedX Architecture                                     |
|                                                                                               |
|   [ Disease / Drug Query ]                                                                    |
|              │                                                                                |
|              ▼                                                                                |
|   Open Targets GraphQL v4 ──► Genomic Disease-Target Association & Scoring                    |
|              │                                                                                |
|              ├──────────────► ChEMBL REST v33: Bioactivities & Off-Target Binding (pChEMBL)   |
|              │                                                                                |
|              ├──────────────► Reactome REST: Signaling Pathway Enrichment & Biological Maps   |
|              │                                                                                |
|              ├──────────────► RDKit QSAR Engine: Lipinski, Veber, Ghose, PAINS & Brenk Alerts |
|              │                                                                                |
|              ▼                                                                                |
|   Ollama (Gemma 3) Engine ──► 4-Pillar AI Intelligence:                                      |
|              │                ├─ Multi-Dimensional Clinical Rationale                         |
|              │                ├─ Medicinal Chemistry SAR (Structure-Activity Relationship)   |
|              │                ├─ Polypharmacological Pathway Crosstalk Synergy                |
|              │                └─ Head-to-Head Multi-Drug Comparative Synthesis                |
|              ▼                                                                                |
|   Dual-Interface Experience:                                                                  |
|   ├─ Interactive Landing Page (Realistic 3D Donepezil Molecule + Live Sandbox)               |
|   └─ Research Studio Workbench (Chapter 1, 2, 3 + Comparison Dock + PDF Export)              |
+-----------------------------------------------------------------------------------------------+
```

---

## ✨ Core Features

### 1. Dual Interactive Web Experiences
- **Landing Page (`/`)**:
  - **Realistic 3D Chemical Hero**: Accurately modeled 3D molecular structure of **Donepezil** ($C_{24}H_{29}NO_3$) with indanone fused rings, dimethoxy oxygens, piperidine nitrogen, and benzyl group.
  - **Fluid Interactivity**: Physics-based drag inertia, mousewheel and pinch zoom, raycasted atom hover tooltips (element symbol, name, valence), and click-to-highlight.
  - **Live Evidence Sandbox**: Live interactive search connected directly to backend endpoints with fallback resilience.
- **Research Studio Workbench (`/app`)**:
  - **Chapter 1: Disease Explorer**: Search any human condition, filter by clinical trial stage (Phase I–IV, Approved), view real-time confidence scores, and dive into deep clinical rationales.
  - **Chapter 2: Compound & ADMET Lab**: Input any SMILES string to compute 20+ physicochemical descriptors, Lipinski Rule of 5 compliance, Veber/Ghose rules, PAINS/Brenk toxicophore filters, and radar envelope charts.
  - **Chapter 3: Target Pathways & Reverse Lookup**: Identify off-target proteins via ChEMBL, explore Reactome biological pathways, and plot binding affinity kinetics.
  - **Comparison Dock**: Pin up to 4 drug candidates into a persistent dock, generate a side-by-side parametric matrix, and synthesize AI recommendations.
  - **One-Click PDF Dossier Export**: Generate publication-quality clinical research dossiers in seconds.

### 2. The 4 AI Pillars (Powered by Ollama `gemma3:latest`)
Ollama is tightly integrated into every scientific phase of the platform:
1. **Clinical Repurposing Rationale** (`/api/explain`): Synthesizes primary mechanism of action, biomarker validation strategies (PET tracers, plasma cytokines), and patient population safety scrutiny.
2. **Medicinal Chemistry SAR Insight** (`/api/ai/sar-analysis`): Interprets SMILES functional groups, explains lipophilicity/permeability trade-offs, and proposes bioisosteric modifications.
3. **Polypharmacological Pathway Crosstalk** (`/api/ai/pathway-crosstalk`): Evaluates how concurrent off-target inhibition creates network synergy across shared downstream effectors (e.g., NF-κB, MAPK).
4. **Head-to-Head Comparative Synthesis** (`/api/ai/compare-synthesis`): Compares multiple pinned candidates, designates a **Primary Lead** and **Secondary Backup**, and highlights regulatory risk factors.

---

## 📂 Repository Structure

```text
REMEDX-/
├── .gitignore                      # Git exclusion rules (caches, virtualenvs, logs)
├── README.md                       # Comprehensive platform documentation
├── PRODUCT.md                      # Product vision and design principles
│
├── frontend/                       # Interactive Web User Interfaces
│   ├── index.html                  # Landing Page with 3D Molecule & Live Sandbox
│   ├── app.html                    # Research Studio Workbench (Chapters 1, 2, 3)
│   ├── package.json                # Frontend asset configuration
│   ├── remedx-background.png       # Design assets
│   └── components/                 # WebGL & shader components
│
├── backend/                        # High-Performance Backend & AI Engine
│   ├── app.py                      # Flask REST API server (threaded, CORS-enabled)
│   ├── chembl_client.py            # ChEMBL REST reverse lookup client
│   ├── cheminformatics.py          # RDKit QSAR, Lipinski, PAINS & Brenk alerts
│   ├── reactome_client.py          # Reactome pathway enrichment client
│   ├── test_suite.py               # Comprehensive 10-endpoint automated test suite
│   ├── prewarm_cache.py            # Cache pre-warmer for instant presentation responses
│   ├── requirements.txt            # Python dependencies
│   ├── .env.example                # Safe environment variables template
│   └── tests/                      # Additional unit and load testing scripts
│
└── docs/                           # Documentation, Literature & Media
    ├── proposal/                   # Project proposal and background
    ├── presentation/               # Slide decks and executive summaries
    └── research/                   # Bioinformatics and computational chemistry notes
```

---

## 🚀 Quick Start Guide

### Prerequisites
- **Python 3.10+**
- **Git**
- *(Optional for AI)* **[Ollama](https://ollama.com/)** with `gemma3:latest` pulled:
  ```bash
  ollama pull gemma3:latest
  ```
  *(Note: If Ollama is not installed or offline, ReMedX automatically engages high-fidelity deterministic algorithmic fallbacks so all features remain 100% functional).*

---

### Step 1: Clone the Repository
```bash
git clone https://github.com/ahammedfahim4456/REMEDX-.git
cd REMEDX-
```

### Step 2: Install Backend Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### Step 3: Run the ReMedX Server
```bash
python app.py
```
*The server will start at `http://localhost:5000` with SQLite caching enabled.*

### Step 4: Open in Browser
- **Landing Page & 3D Molecule**: Open [http://localhost:5000/](http://localhost:5000/)
- **Research Studio Workbench**: Open [http://localhost:5000/app](http://localhost:5000/app)

---

## 📡 REST API Reference

| Endpoint | Method | Parameters | Description |
| :--- | :--- | :--- | :--- |
| `/` | `GET` | — | Serves the interactive 3D landing page |
| `/app` | `GET` | — | Serves the Research Studio Workbench |
| `/api/repurpose` | `GET` | `disease` | Fetches genomic targets & repurposing candidates via Open Targets |
| `/api/compound/analyze` | `GET` | `smiles` | RDKit QSAR analysis, Lipinski, Veber, PAINS, Brenk alerts |
| `/api/reverse-lookup` | `GET` | `query` | ChEMBL bioactivities and target affinity profiling (pChEMBL) |
| `/api/pathways` | `GET` | `gene` | Reactome biological pathway enrichment |
| `/api/explain` | `GET` | `drug, disease, target_gene` | **AI Pillar 1**: Multi-dimensional clinical repurposing rationale |
| `/api/ai/sar-analysis` | `GET` | `smiles, name, mw, logp, tpsa` | **AI Pillar 2**: Medicinal chemistry SAR insight & bioisosteres |
| `/api/ai/pathway-crosstalk` | `GET` | `drug, targets, pathways` | **AI Pillar 3**: Polypharmacological pathway crosstalk synergy |
| `/api/ai/compare-synthesis` | `POST` | JSON `{ disease, candidates }` | **AI Pillar 4**: Head-to-head candidate comparative evaluation |
| `/api/export-pdf` | `GET` | `disease` | Generates a publication-grade scientific PDF report |
| `/api/health` | `GET` | — | Real-time health status of all 6 platform microservices |
| `/api/cache-stats` | `GET` | — | SQLite caching performance and storage metrics |

---

## 🧪 Testing & Verification

ReMedX includes an automated test suite that exercises all 10 endpoints, cheminformatics rules, and AI generation pipelines:

```bash
cd backend
python -u test_suite.py
```

### Automated Verification Summary
```text
==========================================
          REMEDX TEST SUMMARY             
==========================================
  1. Health                     : PASS
  2. Cache Stats                : PASS
  3. Compound Analyzer          : PASS
  4. Reverse Lookup             : PASS
  5. Pathways                   : PASS
  6. Disease Explorer           : PASS
  7. AI SAR Analysis            : PASS
  8. AI Pathway Crosstalk       : PASS
  9. AI Comparison Synthesis    : PASS
  10. AI Deepen Rationale       : PASS
==========================================
OVERALL RESULT: ALL PASS
```

---

## ⚡ Pre-Warming Cache for Demos
To ensure instantaneous `<50ms` responses during live presentations and judging demonstrations:
```bash
# With python app.py running in one terminal:
python prewarm_cache.py
```
This populates the SQLite WAL database (`repurpose_cache.db`) with canonical conditions (Alzheimer's, Parkinson's, Type 2 Diabetes, Breast Cancer, etc.).

---

## 🛡️ Security & Privacy
- **Zero API Key Leaks**: ReMedX utilizes open public biomedical endpoints (Open Targets, ChEMBL, Reactome) and local private AI inference via Ollama. No proprietary patient data or API keys leave the local environment.
- **Git Protection**: Cache databases (`*.db`), Python virtualenvs, and log files are excluded by `.gitignore`.

---

## 👥 Authors & Acknowledgements
- **Team ReMedX**
- Data providers: [Open Targets Platform](https://platform.opentargets.org/), [ChEMBL](https://www.ebi.ac.uk/chembl/), [Reactome](https://reactome.org/), [RDKit](https://www.rdkit.org/), and [Ollama](https://ollama.com/).
