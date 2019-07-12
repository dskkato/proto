from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(name="proto",
      version="0.1",
      description="Prototype project",
      author="Daisuke Kato",
      author_email="kato.daisuke429@gmail.com",
      license="MIT",
      packages=["proto"],
      zip_safe=False,
      test_suite="nose.collector",
      tests_require=["nose", "pycodestyle"],
      scripts=["bin/hello"],
      )
