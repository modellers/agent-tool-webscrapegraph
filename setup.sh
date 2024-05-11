git submodule update --init --recursive
python3 -m venv .venv
source .venv/bin/activate
cd Scrapegraph-ai
pip install -e .
playwright install