import importlib
import importlib.util
import pip
import time


class MyImport:
    @staticmethod
    def __get_module_spec(module_name):
        """
        Checks if module can be imported without actually importing it
        """
        module_spec_var = importlib.util.find_spec(module_name)
        if module_spec_var is None:
            # print('Module: {} not found'.format(module_name))
            return None
        else:
            # print('Module: {} can be imported!'.format(module_name))
            return module_spec_var

    @staticmethod
    def __install_and_import(package):
        import importlib
        try:
            print("IN01")
            my_module = importlib.import_module(package)
            importlib.reload(my_module)
            print("IN02 = " + my_module)
        # except ImportError:
        except:
            import pip
            print("IN1")
            pip.main(['install', package])
            print("IN3")
        finally:
            print("IN4")
            globals()[package] = importlib.import_module(package)
            my_module = importlib.import_module(package)
            importlib.reload(my_module)

    @staticmethod
    def __import_module_from_spec(module_spec_var):
        """
        Import the module via the passed in module specification
        Returns the newly imported module
        """
        module_var = importlib.util.module_from_spec(module_spec_var)
        module_spec_var.loader.exec_module(module_var)
        return module_var

    @staticmethod
    def import_module(module_name):
        while True:
            module_spec = MyImport.__get_module_spec(module_name)
            if module_spec:
                break
            else:
                MyImport.__install_and_import(module_name)
            time.sleep(0.1)
        module_var = MyImport.__import_module_from_spec(module_spec)
        return module_var


    @staticmethod
    def update_and_import():
        import pip
        from subprocess import call

        packages = [dist.project_name for dist in pip.get_installed_distributions()]
        call("pip install --upgrade " + ' '.join(packages), shell=True)


if __name__ == '__main__':
    # Example #1
    module_os = MyImport.import_module('os')
    dir_path = module_os.path.dirname(module_os.path.realpath(__file__))
    print(dir_path)

    # Example #2
    module_os = MyImport.import_module('colorama')
    module_os.init(convert=True)
    print(module_os.Fore.RED + 'Hello world')
    print("END")
