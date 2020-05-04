#!./venv/bin/python3
import os
import click
import shutil
import requests

from pathlib import Path


@click.command()
@click.option('--remove-archive', '-r', default=True, show_default=True,
              type=bool, help='Remove the archive after its content will be extracted.')
def download(remove_archive):
    """Download rtsd-r3 part of RTSD Dataset."""
    download_url = requests.get('https://cloud-api.yandex.net/v1/disk/public/resources/download', params={
        'public_key': 'https://yadi.sk/d/TX5k2hkEm9wqZ',
        'path': '/classification/rtsd-r3.tar.lzma'
    }).json()['href']

    archive_path = Path('./rtsd-r3.tar.lzma')
    with open(archive_path, 'wb') as file:
        archive_ = requests.get(download_url).content
        file.write(archive_)

    extract_to = Path('./datasets')
    extract_to.mkdir(parents=True, exist_ok=True)
    shutil.unpack_archive(archive_path, extract_to, format='xztar')
    os.remove(extract_to / 'rtsd-r3/.crop.swp')
    if (remove_archive):
        os.remove(archive_path)


if __name__ == '__main__':
    download()
