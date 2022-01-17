import ckan.plugins as p
import ckan.plugins.toolkit as tk


class OaiMetadataschemaPlugin(p.SingletonPlugin, tk.DefaultDatasetForm):
    p.implements(p.IDatasetForm)
    p.implements(p.IConfigurer)

    def create_package_schema(self):
        # let's grab the default schema in our plugin
        schema = super(OaiMetadataschemaPlugin, self).create_package_schema()
        # our custom field
        schema.update({
            u'custom_text': [tk.get_validator(u'ignore_missing'),
                             tk.get_converter(u'convert_to_extras')],

            u'language': [tk.get_validator(u'ignore_missing'),
                             tk.get_converter(u'convert_to_extras')],

            u'inchi': [tk.get_validator(u'ignore_missing'),
                          tk.get_converter(u'convert_to_extras')],

            u'smiles': [tk.get_validator(u'ignore_missing'),
                       tk.get_converter(u'convert_to_extras')],

            u'inchi_key': [tk.get_validator(u'ignore_missing'),
                        tk.get_converter(u'convert_to_extras')],

            u'exactmass': [tk.get_validator(u'ignore_missing'),
                          tk.get_converter(u'convert_to_extras')],

        #
        #    u'relation': [tk.get_validator(u'ignore_missing'),
        #                  tk.get_converter(u'convert_to_extras')],
        #
        #    u'relationType': [tk.get_validator(u'ignore_missing'),
        #                         tk.get_converter(u'convert_to_extras')],
        })

        dict_list = [{u'relation': [tk.get_validator(u'ignore_missing'),
                                    tk.get_converter(u'convert_to_extras')],

                      u'relationType': [tk.get_validator(u'ignore_missing'),
                                        tk.get_converter(u'convert_to_extras')]
                      }]

        for dict in dict_list:
            schema.update(dict)

        return schema

    def update_package_schema(self):
        schema = super(OaiMetadataschemaPlugin, self).update_package_schema()
        # our custom field

        schema.update({
            u'custom_text': [tk.get_validator(u'ignore_missing'),
                             tk.get_converter(u'convert_to_extras')],

            u'language': [tk.get_validator(u'ignore_missing'),
                             tk.get_converter(u'convert_to_extras')],

            u'inchi': [tk.get_validator(u'ignore_missing'),
                          tk.get_converter(u'convert_to_extras')],
            u'smiles': [tk.get_validator(u'ignore_missing'),
                       tk.get_converter(u'convert_to_extras')],

            u'inchi_key': [tk.get_validator(u'ignore_missing'),
                        tk.get_converter(u'convert_to_extras')],

            u'exactmass': [tk.get_validator(u'ignore_missing'),
                          tk.get_converter(u'convert_to_extras')],

         #  u'relation': [tk.get_validator(u'ignore_missing'),
         #                tk.get_converter(u'convert_to_extras')],
         #
         #  u'relationType': [tk.get_validator(u'ignore_missing'),
         #                   tk.get_converter(u'convert_to_extras')],
        })

        dict_list = [{ u'relation': [tk.get_validator(u'ignore_missing'),
                          tk.get_converter(u'convert_to_extras')],

                     u'relationType': [tk.get_validator(u'ignore_missing'),
                             tk.get_converter(u'convert_to_extras')]
                       }]

        for dict in dict_list:
            schema.update(dict)

        return schema

    def show_package_schema(self):
        schema = super(OaiMetadataschemaPlugin, self).show_package_schema()

        schema.update({
            u'language': [tk.get_converter(u'convert_from_extras'),
                             tk.get_validator(u'ignore_missing')],
          #  u'relation': [tk.get_converter(u'convert_from_extras'),
          #                tk.get_validator(u'ignore_missing')],
          #
          #  u'relationType': [tk.get_converter(u'convert_from_extras'),
          #                    tk.get_validator(u'ignore_missing')]


            u'inchi': [tk.get_converter(u'convert_from_extras'),
                      tk.get_validator(u'ignore_missing')],

            u'smiles': [tk.get_converter(u'convert_from_extras'),
                       tk.get_validator(u'ignore_missing')],

            u'inchi_key': [tk.get_converter(u'convert_from_extras'),
                        tk.get_validator(u'ignore_missing')],

            u'exactmass': [tk.get_converter(u'convert_from_extras'),
                          tk.get_validator(u'ignore_missing')],

        })

        dict_list = [{u'relation': [tk.get_converter(u'convert_from_extras'),
                             tk.get_validator(u'ignore_missing')],

                      u'relationType': [tk.get_converter(u'convert_from_extras'),
                             tk.get_validator(u'ignore_missing')],}]

        for dict in dict_list:
            schema.update(dict)

        return schema

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return [u'fancy_type']

    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')
