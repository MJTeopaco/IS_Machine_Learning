import json
from pathlib import Path

nb_path = Path(r"d:\Real Estate\Predicting-Concrete-Compressive-Strength-Using-Random-Forest-Regression\Real_State\05_Act_Regression_Group_7.ipynb")
if not nb_path.exists():
    print(f"Notebook not found: {nb_path}")
    raise SystemExit(1)

with nb_path.open('r', encoding='utf-8') as f:
    nb = json.load(f)

cells = nb.get('cells', [])
new_cells = []
removed = 0
for cell in cells:
    cid = cell.get('id') or cell.get('metadata', {}).get('id')
    if cid == '#VSC-3795677c':
        removed += 1
        continue
    # also remove if the cell clearly contains the summary header
    source = ''.join(cell.get('source', []))
    if '### Final summary and next steps' in source:
        removed += 1
        continue
    new_cells.append(cell)

if removed == 0:
    print('No summary cell found to remove (v2).')
else:
    nb['cells'] = new_cells
    with nb_path.open('w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=4)
    print(f'Removed {removed} cell(s) and updated notebook: {nb_path}')
