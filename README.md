# Aircraft_sizing

Small aircraft mission weight estimation script.

This repository contains a single procedural script that computes mission weight fractions (Breguet-type fuel fractions and loiter), estimates an empirical empty-weight fraction, and iteratively solves for the takeoff weight.

**Files**
- `weight_estimation.py` — main script; single source of truth for mission math.

Quick summary
- Language: Python 3.11+ (tested with Python 3.12 in the development environment)
- Primary dependency: `numpy`

Usage

1. Install dependencies (recommended to use a virtual environment):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install numpy
```

2. Run the script from the repository root:

```powershell
python weight_estimation.py
```

Or run with an explicit interpreter path (example from the dev environment):

```powershell
& C:/Users/<user>/AppData/Local/Programs/Python/Python312/python.exe d:/python/coding_practise/Aircraft_sizing/weight_estimation.py
```

What to edit
- Open `weight_estimation.py` and change the top-of-file parameters to experiment with missions:
  - `ran` (range in meters)
  - `endu` (loiter endurance, seconds)
  - `V_cz` (cruise speed, m/s)
  - `c_crz`, `c_loiter` (SFC-like values; currently mg/Ns converted to 1/s units)
  - `w_pay` (payload weight, N)
  - `L_D_c`, `L_D_e` (lift-to-drag ratios for cruise and loiter)

Implementation notes & conventions
- Variable naming uses underscore-separated fraction notation, e.g. `w3_w2` denotes weight fraction w3/w2.
- Fuel fractions use exponential (Breguet-style) formulas: `math.exp(-(range*c)/(V*L_D))`.
- Empty-weight fraction follows an empirical relation: `we_w0 = A * w0**C` (A and C at the top of the script).
- Solver loop uses a simple fixed-point / averaging scheme and a tolerance of `1e-4` to converge `w0`.

Examples
- Quick run (default inputs in the file): prints `w3_w2`, `w4_w3`, `w_fuel_w0`, converged takeoff weight, empty and payload fractions.
- Add a mission phase: add a new `wX_wY` computed using the same exponential pattern and include it when computing `w_fuel_w0`.

Suggested small improvements (optional)
- Convert the script into functions and add `if __name__ == '__main__'` to enable imports and unit tests.
- Add a `requirements.txt` containing `numpy` (and `scipy` if you plan to use `scipy.optimize` for root-finding).
- Add small unit tests that assert expected weight fractions for a couple of fixed parameter sets.

Finding the GitHub path for this repository
- I added this `README.md` to the local repository at `d:/python/coding_practise/Aircraft_sizing/README.md`.
- To find the repository's configured GitHub remote (the exact URL to use on GitHub), run in PowerShell from the repo root:

```powershell
git remote -v
```

- If your remote is `origin` and your GitHub repository is named `Aircraft_sizing`, the README will appear at a URL like:

```
https://github.com/<your-username>/Aircraft_sizing/blob/main/README.md
```

Replace `<your-username>` and `main` with your GitHub username and branch name as appropriate.

If you want, I can:
- add a `requirements.txt` and commit it,
- refactor `weight_estimation.py` into an importable module and add a couple of unit tests,
- or commit and push these changes to your remote if you provide push credentials or let me run `git` locally here.
