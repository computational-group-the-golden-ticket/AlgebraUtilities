from distutils.core import setup

setup(
    name='algebra_utilities',
    packages=['algebra_utilities'],
    version='0.1',
    license='MIT',
    description='tools to manipulate algebraic objects (semigroup, group, and monoids); permutation oriented.',
    author='CG The Golden Ticket',
    author_email='cgthegoldenticket@gmail.com',
    url='https://github.com/computational-group-the-golden-ticket/AlgebraUtilities',
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
    keywords=['Algebra', 'Objects', 'Structures', 'Monoid', 'Group',
              'Semigroup', 'Permutation'],

    install_requires=[            # I get to this in a second
        'unittest',
    ],

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
