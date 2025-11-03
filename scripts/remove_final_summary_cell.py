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
    source = ''.join(cell.get('source', []))
    # Remove cells that contain the specific summary heading or the exact sentence
    if 'Final summary and next steps' in source or 'What I ran and saved' in source:
        removed += 1
        continue
    new_cells.append(cell)

if removed == 0:
    print('No summary cell found to remove.')
else:
    nb['cells'] = new_cells
    with nb_path.open('w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=4)
    print(f'Removed {removed} cell(s) and updated notebook: {nb_path}')
