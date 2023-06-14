[![Tests](https://github.com/BhavHUb/ckanext-oai_metadataschema/workflows/Tests/badge.svg?branch=main)](https://github.com/bhavin2897/ckanext-oai_metadataschema/actions)

# ckanext-oai_metadataschema

Providing a metadataschema for displaing metadata fields to enrich the datasets on ckan. 
This extension inspired and developed using offical documentation from CKAN, https://docs.ckan.org/en/2.9/extensions/adding-custom-fields.html


## Requirements

If your extension works across different versions you can add the following table:

Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
| 2.8             | not tested    |
| 2.9             | yes    |



## Installation

To install ckanext-oai_metadataschema:

1. Activate your CKAN virtual environment, for example:

     . /usr/lib/ckan/default/bin/activate

2. Clone the source and install it on the virtualenv

    git clone https://github.com/bhavin2897/ckanext-oai_metadataschema.git
    cd ckanext-oai_metadataschema
    pip install -e .
	pip install -r requirements.txt

3. Add `oai_metadataschema` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

     sudo service apache2 reload
     

## Config settings

None at present

**TODO:** Document any optional config settings here. For example:

	# The minimum number of hours to wait before re-checking a resource
	# (optional, default: 24).
	ckanext.oai_metadataschema.some_setting = some_default_value


## Developer installation

To install ckanext-oai_metadataschema for development, activate your CKAN virtualenv and
do:

    git clone https://github.com/BhavHUb/ckanext-oai_metadataschema.git
    cd ckanext-oai_metadataschema
    python setup.py develop
    pip install -r dev-requirements.txt


Restart Serverr
	sudo service supervisor reload
	sudo service nginx reload


## Releasing a new version of ckanext-oai_metadataschema

If ckanext-oai_metadataschema should be available on PyPI you can follow these steps to publish a new version:

1. Update the version number in the `setup.py` file. See [PEP 440](http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers) for how to choose version numbers.

2. Make sure you have the latest version of necessary packages:

    pip install --upgrade setuptools wheel twine

3. Create a source and binary distributions of the new version:

       python setup.py sdist bdist_wheel && twine check dist/*

   Fix any errors you get.

4. Upload the source distribution to PyPI:

       twine upload dist/*

5. Commit any outstanding changes:

       git commit -a
       git push

6. Tag the new release of the project on GitHub with the version number from
   the `setup.py` file. For example if the version number in `setup.py` is
   0.0.1 then do:

       git tag 0.0.1
       git push --tags

## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
