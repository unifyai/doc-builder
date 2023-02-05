print_log = None


def set_verbose(flag):
    global print_log
    if flag:
        def _print_log(string):
            print(string)
    else:
        def _print_log(string):
            return
    print_log = _print_log
