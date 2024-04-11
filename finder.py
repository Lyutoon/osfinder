import argparse

def find_import_path(package, target_attr):
    exec(f'import {package}')
    stack = [(eval(package), package)]
    trace = []
    while stack:
        current_obj, import_path = stack.pop()
        if len(import_path.split('.')) > 5:
            continue
        try:
            for attr_name in dir(current_obj):
                attr = getattr(current_obj, attr_name)
                if attr_name == target_attr:
                    print(f"{import_path}.{target_attr}")
                    trace.append(f"{import_path}.{target_attr}")
                elif isinstance(attr, type(current_obj)):
                    module_path = f"{import_path}.{attr_name}"
                    stack.append((attr, module_path))
                if len(trace) > 1000:
                    return trace
        except:
            pass

    return None

def main(args):
    package = args.package
    target_attr = args.target
    import_path = find_import_path(package, target_attr)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--package', help='third party package', type=str)
    parser.add_argument('--target', help='target, default to be os', type=str, default='os')
    args = parser.parse_args()
    main(args)
