from setuptools import find_packages, setup
# from discutil.core import setup

setup(
    name='algebra_utilities',
    packages=find_packages(),
    version='0.1',
    license='MIT',
    description='tools to manipulate algebraic objects (semigroup, group, and monoids); permutation oriented.',
    author='CG The Golden Ticket',
    author_email='cgthegoldenticket@gmail.com',
    url='https://github.com/computational-group-the-golden-ticket/AlgebraUtilities',
    download_url='https://github.com/computational-group-the-golden-ticket/AlgebraUtilities/archive/0.1.tar.gz',    # I explain this later on
    keywords=['Algebra', 'Objects', 'Structures', 'Monoid', 'Group',
              'Semigroup', 'Permutation'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)
