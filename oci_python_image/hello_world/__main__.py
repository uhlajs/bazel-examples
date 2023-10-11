import os
from pathlib import Path
from pprint import pformat

import runfiles
from hello_world.app import Cow


def cow_hello() -> None:
    app = Cow("John")
    app.say_hello()


def show_runfiles_environments() -> None:
    print("Runtime Environments")
    print(
        pformat(
            {
                key: value
                for key, value in os.environ.items()
                if key.startswith("RUNFILES_")
            }
        ),
    )


def runfiles_resolution(config_path: Path) -> None:
    print("Runfiles resolution")
    r = runfiles.Create()

    p = Path(r.Rlocation(config_path.as_posix()))
    print(p)
    print(p.is_file())

    if p.is_file():
        print("File content")
        with p.open("r") as file:
            print(file.readlines())


def runfiles_resolution_with_additional_mapping(config_path: Path) -> None:
    print("Runfiles resolution with addtional mapping")
    r = runfiles.Create()

    # Manually add _repo_mapping
    if not r._repo_mapping:
        print("Applying repo mapping")
        r._repo_mapping = {("", "my_module"): "_main", ("", "my_workspace"): "_main"}

    p = Path(r.Rlocation(config_path.as_posix()))
    print(p)
    print(p.is_file())

    if p.is_file():
        print("File content")
        with p.open("r") as file:
            print(file.readlines())


def main() -> None:
    cow_hello()

    config_path = Path("my_workspace/hello_world/data/config.json")

    show_runfiles_environments()
    print()
    runfiles_resolution(config_path)
    print()
    runfiles_resolution_with_additional_mapping(config_path)


if __name__ == "__main__":
    main()
