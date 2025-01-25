---
license: mit
tags:
- chess
- pgn
- tokenizer
pretty_name: {{dataset["pretty_name"]}}
size_categories:
  - 1M<n<10M
source_datasets:
- {{dataset["source"]}}
task_categories:
  - token-classification
task_ids:
  - parsing
dataset_info:
  features:
    - name: PGN
      dtype: string
---

# {{dataset["pretty_name"]}}

**Last Updated**: {{dataset["last_updated"]}}

## Description

{{dataset["description"]}}

## Notes

This was the training dataset for [`PGNTokenizer`](https://huggingface.co/InterwebAlchemy/PGNTokenizer). For more information about using `PGNTokenizer` visit the [GitHub repository](https://github.com/DVDAGames/pgn-tokenizer).

You can read more about [research from the original dataset](https://chess-research-project.readthedocs.io/en/latest/).
