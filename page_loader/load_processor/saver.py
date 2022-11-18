from pathlib import Path
from typing import Union, Callable


def save_data_to_file(data: Union[str, bytes],
                      file_path: Path,
                      mode: str) -> None:
    with file_path.open(mode) as file:
        file.write(data)


def save_page(data: str, file_path: Path) -> Callable[..., None]:
    save_data_to_file(data, file_path, 'w')


def save_resource(data: bytes, file_path: Path) -> Callable[..., None]:
    save_data_to_file(data, file_path, 'wb')
