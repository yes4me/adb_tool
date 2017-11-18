import importlib
import importlib.util


class Import:

    @staticmethod
    def get_module_spec(module_name):
        """
        Checks if module can be imported without actually
        importing it
        """
        module_spec_var = importlib.util.find_spec(module_name)
        if module_spec_var is None:
            # print('Module: {} not found'.format(module_name))
            return None
        else:
            # print('Module: {} can be imported!'.format(module_name))
            return module_spec_var

    @staticmethod
    def import_module_from_spec(module_spec_var):
        """
        Import the module via the passed in module specification
        Returns the newly imported module
        """
        module_var = importlib.util.module_from_spec(module_spec_var)
        module_spec_var.loader.exec_module(module_var)
        return module_var

    @staticmethod
    def install_and_import(package):
        import importlib
        try:
            importlib.import_module(package)
        except ImportError:
            import pip
            pip.main(['install', package])
        finally:
            globals()[package] = importlib.import_module(package)


if __name__ == '__main__':
    # Example #1
    module_spec = Import.get_module_spec('os')
    if module_spec:
        module_os = Import.import_module_from_spec(module_spec)
        dir_path = module_os.path.dirname(module_os.path.realpath(__file__))
        print(dir_path)

    # Example #2
    module_spec = Import.get_module_spec('colorama')
    if module_spec:
        module_os = Import.import_module_from_spec(module_spec)
        module_os.init(convert=True)
        print(module_os.Fore.RED + 'Hello world')
