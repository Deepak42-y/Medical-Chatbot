from setuptools import setup , find_packages
setup( 
    name='medical chatbot', 
    version='0.0.1', 
    # description='A sample Python package', 
    author='Deepak Yadav', 
    author_email='honestharry1980@gmail.com', 
    packages=find_packages(), 
    install_requires=[ 
        'numpy', 
        'pandas', 
        'ctransformers',
        'langchain',
        "streamlit",
        "sentence-transformers",
        "flask",
        "langchain_community"
    ], 
)