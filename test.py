import lib.my_import


if __name__ == '__main__':
    # Example #1
    module_os = lib.my_import.MyImport.import_module('os')
    dir_path = module_os.path.dirname(module_os.path.realpath(__file__))
    print(dir_path)

    # Example #2
    module_os = lib.my_import.MyImport.import_module('colorama')
    module_os.init(convert=True)
    print(module_os.Fore.RED + 'Hello world')
    print("END")
