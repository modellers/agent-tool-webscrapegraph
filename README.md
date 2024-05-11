# agent-tool-webscrapegraph

## Configure submodule

Setup


  - git submodule add https://github.com/modellers/Scrapegraph-ai
  - git commit -m "Added Scrapegraph-ai as a submodule"
  - git push

## Install

Install this

  - git clone --recurse-submodules https://github.com/modellers/agent-tool-webscrapegraph

## Update

  - git submodule update --init --recursive

## Run

#### Run the agent

```bash
python cli.py <source> --model <model> --temperature <temperature> --format <format> --base_url <base_url> --embeddings_model <embeddings_model> --verbose --output <output_file>

#### Example

python cli.py <source> --model <model> --temperature <temperature> --format <format> --base_url <base_url> --embeddings_model <embeddings_model> --verbose --output <output_file>
