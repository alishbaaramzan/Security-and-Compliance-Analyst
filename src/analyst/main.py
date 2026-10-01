import json
import sys

from .agent import SecurityAnalyst


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: uv run analyst <use-case.json>")
        raise SystemExit(1)

    with open(sys.argv[1], encoding="utf-8") as file:
        use_case = json.load(file)

    assessment = SecurityAnalyst().assess(use_case)

    print(assessment.model_dump_json(indent=2))


if __name__ == "__main__":
    main()