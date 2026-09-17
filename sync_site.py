from pathlib import Path
import shutil
root = Path(__file__).resolve().parent
shutil.copyfile(root / "2027_snowboard_trip_budget_clean.html", root / "public/index.html")
print("public/index.html を更新しました")
