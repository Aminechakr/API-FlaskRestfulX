from distutils.core import setup

__version__ = "0.0.1"

setup(
    name= 'falskrestxapi',
    packages= ['.']
    version= __version__
    description= 'hello flask rest x api'
    author= 'Amine CHAKRELLAH'
    author_email= 'chakrelllah@gmail.com'
    url= "https://github.com/Aminechakr/API-FlaskRestfulX"
    keywords= ['API', 'Falsk_restX'],
    install_requires=[ 
        flask_restx,
        flask,
    ],
    python_requires='>=3.6',
    classifiers= [
        'Devlopment Status :: Devloppement',
        'Intended Audience :: Devloppers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.6',
        'Porgramming Language :: Python :: 3.7',
        'Porgramming Language :: Python :: 3.8',

    ],
)