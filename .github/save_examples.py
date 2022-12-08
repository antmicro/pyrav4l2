from pathlib import Path
import sys
from tuttest import get_snippets

if __name__ == "__main__":
    snippets = get_snippets(sys.argv[1])

    examples_path = Path("examples")
    examples_path.mkdir(parents=True, exist_ok=True)

    for snippet_name in snippets.keys():
        snippet = snippets[snippet_name]

        if snippet.lang == "python" and "unnamed" not in snippet_name:
            with open(examples_path / Path(f"{snippet_name}.py"), "w") as f:
                f.write(snippet.text)
