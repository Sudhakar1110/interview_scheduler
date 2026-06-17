from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = [line.strip() for line in f if line.strip() and not line.startswith("#")]

version = "1.0.0"

setup(
	name="hireflow",
	version=version,
	description="Interview Scheduling & Recruitment Management Platform",
	author="Antigravity",
	author_email="info@antigravity.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
