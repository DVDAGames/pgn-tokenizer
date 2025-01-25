import datetime

from datasets import Dataset, DatasetDict, load_dataset
from jinja2 import Template
from pgn_tokenizer.constants import (
    BASE_DATASET_FILE_NAME,
    BASE_DATASET_NAME,
    CLEANED_SUFFIX,
    DATASET_FILE_EXTENSION,
    DATASET_NAME,
    SEED,
    SPECIAL_TOKENS,
)

ORIGINAL_DATASET_FILE_PATH = f".data/datasets/{BASE_DATASET_NAME}/{BASE_DATASET_FILE_NAME}-{CLEANED_SUFFIX}.{DATASET_FILE_EXTENSION}"

FORMATTED_DATASET_PATH = f".data/datasets/{DATASET_NAME}/"

MARKDOWN_TEMPLATE_PATH = "./templates/dataset-readme.md"


def load() -> Dataset:
    dataset = load_dataset("csv", data_files=ORIGINAL_DATASET_FILE_PATH)

    dataset["train"] = dataset["train"].filter(lambda x: x["PGN"] is not None)

    return dataset


def save_dataset(
    dataset: dict[str, Dataset],
    dataset_name: str,
    description_suffix: str = "",
) -> None:
    dataset_dict = DatasetDict(dataset)

    dataset_path = f"{FORMATTED_DATASET_PATH}/{dataset_name}"

    dataset_dict.save_to_disk(f"{dataset_path}/data")

    description = f"""
    This is a dataset of chess games in Portable Game Notation (PGN) format. The dataset was created by cleaning and formatting the [{BASE_DATASET_NAME}](https://www.kaggle.com/{BASE_DATASET_NAME}) dataset from Kaggle.
    """

    dataset_info: dict[str, str] = {
        "name": dataset_name,
        "pretty_name": dataset_name.replace("-", " ").title().replace("Pgn", "PGN"),
        "last_updated": datetime.datetime.now().strftime("%Y-%m-%d"),
        "description": description,
        "source": f"https://www.kaggle.com/datasets/{BASE_DATASET_NAME}",
    }

    if description_suffix:
        dataset_info["description"] += f"\n\n{description_suffix}"

    create_readme(dataset_info, dataset_path)

    dataset_dict.push_to_hub(f"InterwebAlchemy/{dataset_name}")


def generate_splits(dataset: Dataset, seed: int) -> DatasetDict:
    # split the dataset into train, test, and validation sets
    temp_dataset = dataset.train_test_split(test_size=0.1, seed=seed)

    # create a new DatasetDict for the full dataset
    dataset_dict = {
        "train": temp_dataset["train"],
        "test": temp_dataset["train"],
        "validation": temp_dataset["test"],
    }

    return dataset_dict


def add_special_tokens(dataset: Dataset) -> Dataset:
    # modify the PGN column to add the game start and game end tokens
    dataset = dataset.map(
        lambda x: {"PGN": SPECIAL_TOKENS["START"] + x["PGN"] + SPECIAL_TOKENS["END"]},
    )

    return dataset


def remove_extra_columns(dataset: Dataset) -> Dataset:
    # remove the extra columns from the dataset
    dataset = dataset.remove_columns(["Date", "WhiteElo", "BlackElo", "Result"])

    return dataset


def create_readme(dataset_info: dict, path: str) -> None:
    with open(MARKDOWN_TEMPLATE_PATH) as template_file:
        template = Template(template_file.read(), trim_blocks=True)
        template_file.close()

    readme = template.render(dataset=dataset_info)

    # output the file
    with open(f"{path}/README.md", "w") as output_file:
        output_file.write(readme)
        output_file.close()


# load the dataset
dataset = load()

# remove extra columns
dataset["train"] = remove_extra_columns(dataset["train"])

# split the dataset
split_dataset = generate_splits(dataset["train"], SEED)

# save the full dataset
save_dataset(
    split_dataset,
    "pgn-dataset",
    "This version of the pgn-dataset does not include the `[g_start]` and `[g_end]` special tokens that [PGNTokenizer]((https://huggingface.co/InterwebAlchemy/PGNTokenizer) uses to denote the start and end of a game. The [pgn-dataset-including-special-tokens](https://huggingface.co/datasets/InterwebAlchemy/pgn-dataset-including-special-tokens) dataset includes these tokens.",
)

# add special tokens to the dataset
tokenized_dataset = add_special_tokens(dataset)

# split the tokenized dataset
split_tokenized_dataset = generate_splits(tokenized_dataset["train"], SEED)

# save the tokenized dataset
save_dataset(
    split_tokenized_dataset,
    "pgn-dataset-including-special-tokens",
    "This version of the [pgn-dataset](https://huggingface.co/datasets/InterwebAlchemy/pgn-dataset) includes the `[g_start]` and `[g_end]` special tokens that [PGNTokenizer]((https://huggingface.co/InterwebAlchemy/PGNTokenizer) uses to denote the start and end of a game.",
)
