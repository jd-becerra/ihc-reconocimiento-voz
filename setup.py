from setuptools import setup, find_packages

setup(
    name="IHC - Reconocimiento de voz",
    version="0.1.0",
    author="David Becerra, Aldo Valdez, José Moctezuma",
    description="Proyecto de IHC para moverse en un grid con comandos de voz",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/jd-becerra/ihc-reconocimiento-voz",
    packages=find_packages(),
    install_requires=[
        'pygame',
        'SpeechRecognition',
        'pyaudio'
    ],
    entry_points={
        'console_scripts': [
            'start=src.gui:start_app',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)