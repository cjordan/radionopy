from setuptools import find_packages
import os
import subprocess

__version__ = '1.0.0-dev'
authors = 'James Aguirre, Immanuel Washington, Saul Kohn, Zachary Martinot'

setup_args = {
    'name': 'radionopy',
    'author': authors,
    'description': 'package for ionosphere RM',
    'url': 'https://github.com/jaguirre/radionopy.git',
    'license': 'MIT',
    'package_dir' : {'radionopy': ''},
    'packages' : find_packages(),
    'version': __version__,
}

root_dir = os.path.dirname(__file__)
igrf_dir = os.path.join(root_dir, 'IGRF/geomag70_linux')

if __name__ == '__main__':
    try:
        from setuptools import setup
    except:
        from distutils.core import setup
    try:
        apply(setup, (), setup_args)
    except:
        setup(**setup_args)

    #Compiles geomag C script
    compiler = "gcc"
    source = os.path.join(igrf_dir, "geomag70.c")
    exe_name = os.path.join(igrf_dir, "geomag70")
    link_args = "-lm"
    subprocess.call([compiler, "-O2", source, "-o", exe_name, link_args])

    open(igrf_dir + '/input.txt', 'a').close()
    open(igrf_dir + '/output.txt', 'a').close()

    # os.system('touch ' + igrf_dir + '/input.txt')
    # os.system('touch ' + igrf_dir + '/output.txt')
