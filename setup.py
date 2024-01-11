from setuptools import setup

setup(
    name='calculate_triangle_area',
    version='0.1.0',
    py_modules=['calculate_triangle_area', 'triangle_area'],
    install_requires=[
        # List any dependencies here if needed
    ],
    entry_points={
        'console_scripts': [
            'calculate_triangle_area = calculate_triangle_area:main',
        ],
    },
    author='Chuan-Fu Chuang',
    author_email='iamcf.chuang@gmail.com',
    description='Calculate the area of a triangle',
    long_description='A simple Python script to calculate the area of a triangle.',
    long_description_content_type='text/plain',
    url='https://github.com/Blessir/CFChuang',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
