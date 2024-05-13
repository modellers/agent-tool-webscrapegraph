# Update package index
sudo apt update
# Install pip for Python 3
sudo apt install python3-pip
# Install virtualenv using pip
sudo apt install python3-venv
git submodule update --init --recursive
python3 -m venv .venv
cd Scrapegraph-ai
pip install -e .
playwright install