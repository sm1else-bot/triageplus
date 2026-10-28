# TRIAGE / TRIAGE+ engineering case study

Static portfolio publication for Jessenth Ebenezer. Public URL: **https://projects.jessenth.com/triageplus/**. The publication repository and URL use `triageplus`; the project retains the TRIAGE / TRIAGE+ names.

This repository contains the case study, screenshot assets and static build tooling. The private analytical application is a separate repository. No backend, report database, provider credentials or live-analysis endpoint is included here. The TRIAGE+ public interactive demo is **coming soon**.

## Build and preview

Python 3, no package installation:

```sh
python3 tools/build_site.py
python3 tools/check_site.py
python3 -m http.server 8771 --bind 127.0.0.1 --directory _site
```

Open `http://127.0.0.1:8771/`. All asset URLs are relative, allowing GitHub project Pages hosting at `/triageplus/`. The account-level projects gallery links to that directory. Previewing the complete gallery locally requires serving this build at its `triageplus/` subdirectory.

The build copies an explicit allowlist: HTML, CSS, JavaScript, favicon and media. It versions script/style URLs with content hashes, following the existing project collection. No framework or runtime dependencies were introduced. Google Fonts supplies the portfolio's existing DM Sans / Bebas Neue pairing, with system fallbacks.

## Hosting

The existing portfolio and Mozhi use GitHub Actions Pages deployment on `main`; this repository follows that workflow. Configure Pages with `build_type: workflow`. Do not set a project-level custom domain: the account site owns `projects.jessenth.com`, and this project inherits the `/triageplus/` path. The publication workflow deploys `_site/` only.

## Media provenance and authenticity

All captures were made on 27 October 2026 through a browser. WebP derivatives use `cwebp -q 88`, without compositing or altering interface content. Original JPEG captures are preserved in `assets/originals/`. Images have intrinsic dimensions, lower-page lazy loading and a native-dialog image viewer. Original image links work without JavaScript; mobile enlargement supports horizontal scrolling. Escape closes the viewer and returns focus to its opener.

| Asset stem              | Capture source / view                                                              | Data                                                                                                                                                                         |
| ----------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `original-triage`       | `https://triage-production-b22c.up.railway.app/`, initial submission screen        | Empty input; no analysis requested. 1434 × 996 capture. This is the currently deployed original interface, captured in October, not a screenshot taken during the hackathon. |
| `workstation-report`    | Current `astra-revamp` application at isolated loopback port 8001, restored report | Synthetic Northstar Coffee regression fixture. 1280 × 720. Also used for the gallery thumbnail and Open Graph image.                                                         |
| `workstation-overview`  | Same isolated application, Overview                                                | Same synthetic fixture, 1280 × 720.                                                                                                                                          |
| `workstation-inspector` | Same isolated application, supplier-concentration finding drawer                   | Same synthetic fixture, 1280 × 720. Shows a USER_FACT with no independent source group.                                                                                      |
| `workstation-sources`   | Same isolated application, Evidence library                                        | Same fixture; `northstar.example` is a reserved example domain, not a real research source. 1280 × 720.                                                                      |
| `workstation-history`   | Same isolated application, Analysis history                                        | Only the fixture's saved specialist/report snapshots, 1280 × 720.                                                                                                            |

The fixture was regenerated using `tests/test_end_to_end.py::test_complete_realistic_company_workflow` against engineering commit `e4edc2b`, in an isolated temporary data directory. Its model/search providers are deterministic replacements. The resulting snapshots were restored through the actual application UI; no interface elements were fabricated for the images. The test passes under evidence policy `2026-10-27.1`. This fixture is distinct from the historical live investigation discussed in the article.

No private company reports, user-provided report exports, keys or paid analysis runs were used for media. The original deployment's page loaded; its analysis behavior, billing and security were not exercised. Its demo is explicitly labelled legacy, and the page advises using public or synthetic business information.

Missing historical artifacts: no original report-result screenshot or pitch/demo recording was found in the inspected repositories and local project artifacts. The article documents that absence. It does not fabricate replacements.

## Technical source map

Claims were reviewed against the private engineering repository's **`astra-revamp`** branch at `e4edc2b` and the 27 October hardening report. `main` was used only for historical context. Public source links refer to this publication, never to a purported public analytical backend.

| Article topic                       | Engineering source inspected                                                        | Boundary retained in the article                                                                                                                                                              |
| ----------------------------------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dependency graph                    | `backend/api/main.py`, `_full_analysis`, competitive and compliance endpoints       | DD first; three parallel branches; mapping before selected-competitor research; signal/news parallel; detection → realtime → advisor. Controlled workflow, not arbitrary autonomous planning. |
| Specialist contracts                | `backend/core/pipeline.py`, `models.py`, specialist implementations                 | Nine specialist envelopes; internal sub-agents and reconciliation involve more than nine provider calls. Invalid items can be excluded while valid ones survive.                              |
| Textual evidence gates              | `backend/core/evidence.py`, `integrity.py`                                          | Whole-statement reproduction, no automatic VERIFIED; no semantic truth guarantee.                                                                                                             |
| Concrete conditional example        | `tests/benchmarks/evidence_cases.json`, `conditional_requirement`; benchmark runner | Nuclear-license sentence is synthetic and expected INFERRED when its condition is omitted.                                                                                                    |
| Source grouping                     | `backend/core/sources.py`                                                           | Exact/fingerprint/host/upstream grouping and five-word shingles over first 500 words; overlap threshold .85 with minimum 12 shingles. Bounded independence heuristic.                         |
| Conflict and dependency propagation | `backend/core/integrity.py`, `evidence.py`                                          | Bounded aliases, exact quantities and temporal normalization; conflict exclusion; no arbitrary semantic interpretation.                                                                       |
| Regulatory context                  | Finding schema and integrity checks                                                 | Activity/trigger/source/effective-date fields; potential/unknown applicability and constrained authoritative dates.                                                                           |
| Report synthesis                    | `backend/agents/master_report.py`                                                   | Deterministic revalidation/scoring; constrained relationship proposals and selection of existing finding IDs. Scores are uncalibrated heuristics.                                             |
| Durable execution                   | `backend/core/storage.py`, `backend/api/main.py`                                    | Persisted jobs/checkpoints, transactional idempotency, cooperative cancellation, startup INTERRUPTED; no automatic stage resume or distributed queue.                                         |
| Budgets                             | `backend/core/usage.py`, provider clients, README                                   | 2m accounted/reserved tokens, 64 model attempts, 128 searches, 900 seconds, one active root, 12 starts/minute. Estimates and process-local controls, not billing ceilings or public credits.  |
| Interface                           | `frontend/src/App.jsx`, `frontend/src/workstation/`                                 | Actual current application captures; default light, optional dark, clinical metadata/register vocabulary.                                                                                     |
| Regression verification             | Backend/frontend suites and hardening report                                        | Re-run during case-study implementation: 100 backend, 14 frontend, successful Vite production build. Not coverage or factual accuracy.                                                        |
| Historical measurement              | Archived October 5 engineering record, current hardening report                     | 54 findings, 199 source records, 389.7s, 1,068,479 aggregate reported tokens; pre-hardening and not a cost/accuracy/current-latency benchmark. Private report is omitted.                     |

## Chronology and attribution

Original commits span 28–29 March 2026. Jessenth Ebenezer's initial commits include `e9535ec` and `28f9707`. Disha Shanbhag's `10d2944` introduced the stress-test work, with subsequent stress-test commits including `443c6cd` and `7e7aa6f`. Later edits by Zuzanna Bak include `58365b9` and `aadb083`. Zuzanna's history also records competitive/compliance work and report synthesis (`16ea329`, with related report work recorded in the March history). The article credits both original stress-test authorship and subsequent changes.

TRIAGE+ development is recorded on 5 October (`a49830a` and follow-up commits); the continuation/hardening pass is 27 October (`e4edc2b`). Later development was directed by Jessenth with AI coding assistance. Git establishes code history, but not complete off-repository authorship of ideation, design, presentations or hackathon teamwork; those remain team-level credit.

## Review boundaries

The page deliberately retains unresolved source truth/attribution, semantic entailment, real-world evaluation, score calibration, public authentication/ownership, distributed execution, stage resume and provider economics. Legacy availability is a page-load observation, not an endorsement of security or a guarantee of current analysis behavior.

The case study uses no invented model benchmark, no Llama-7B performance claim, no fake waitlist and no clickable TRIAGE+ analysis button. It leaves the existing Railway deployment untouched.
