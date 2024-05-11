import argparse
from scrapegraphai.graphs import SmartScraperGraph

def main():
    parser = argparse.ArgumentParser(description='Run SmartScraperGraph')
    parser.add_argument('prompt', type=str, help='What to search for in source')
    parser.add_argument('source', type=str, help='Source URL or HTML code')
    parser.add_argument('--model', type=str, default='ollama/magicoder', help='Model to use')
    parser.add_argument('--temperature', type=float, default=0, help='Temperature for model')
    parser.add_argument('--format', type=str, default='json', help='Output format')
    parser.add_argument('--base_url', type=str, default='http://localhost:11434', help='Base URL for Ollama')
    parser.add_argument('--embeddings_model', type=str, default='ollama/nomic-embed-text', help='Embeddings model to use')
    parser.add_argument('--verbose', action='store_true', help='Verbose output')
    parser.add_argument('--output', type=str, help='Output file')

    args = parser.parse_args()

    graph_config = {
        "llm": {
            "model": args.model,
            "temperature": args.temperature,
            "format": args.format,
            "base_url": args.base_url,
        },
        "embeddings": {
            "model": args.embeddings_model,
            "base_url": args.base_url,
        },
        "verbose": args.verbose,
    }

    smart_scraper_graph = SmartScraperGraph(
        prompt=args.prompt,
        source=args.source,
        config=graph_config
    )

    result = smart_scraper_graph.run()

    if args.output:
        with open(args.output, 'w') as f:
            f.write(result)
    else:
        print(result)

if __name__ == "__main__":
    main()