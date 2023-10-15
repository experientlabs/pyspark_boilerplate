import os
import re
from invoke import task

pre_release_placeholder = 'SNAPSHOT'
version_filepath = os.path.join('.', 'VERSION')
version_pattern = re.compile(fr'^\d+.\d+.\d+(-{pre_release_placeholder})?$')


def get_version(with_pre_release_placeholder=False):
    with open(version_filepath, 'r') as version_file:
        version_lines = version_file.readlines()
        assert len(version_lines) == 1, 'Version file is malformed'
        version = version_lines[0]
        assert version_pattern.match(version), 'Version string is malformed'
        if with_pre_release_placeholder:
            print(version)
            return version
        else:
            version = version.replace(f'-{pre_release_placeholder}', '')
            print(version)
            return version.replace(f'-{pre_release_placeholder}', '')


@task
def get(c, with_pre_release_placeholder=False):
    get_version(with_pre_release_placeholder=False)



@task
def write_version_file(c, major, minor, patch):
    version = f'{major}.{minor}.{patch}-{pre_release_placeholder}'
    with open(version_filepath, 'w') as version_file:
        version_file.write(version)


@task
def inc_patch(c):
    version = get(c)
    major, minor, patch = version.split('.')
    write_version_file(c, major, minor, int(patch) + 1)


@task
def inc_minor(c):
    version = get(c)
    major, minor, patch = version.split('.')
    write_version_file(c, major, int(minor) + 1, patch)


@task
def inc_major(c):
    version = get(c)
    major, minor, patch = version.split('.')
    write_version_file(c, int(major) + 1, minor, patch)


@task
def project_root(c):
    project_root_dir = os.path.dirname(os.path.abspath(__file__))
    print(project_root_dir)
    return project_root_dir
