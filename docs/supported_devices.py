import sys

sys.path.append("..")

import ivy


def get_flags(fn_name):
    if 'static' in fn_name:
        fn_name = '_'.join(fn_name.split('_')[1:])
    flags = []
    if fn_name not in ivy.__dict__:
        return (), False
    for device in ["cpu", "gpu"]:
        for backend in ["jax", "numpy", "tensorflow", "torch"]:
            ivy.set_backend(backend)
            try:
                if fn_name not in ivy.__dict__:
                    flags.append("❌")
                elif device not in ivy.function_unsupported_devices(ivy.__dict__[fn_name]):
                    flags.append("✅")
                else:
                    flags.append("❌")
            except Exception as e:
                flags.append("❌")
            ivy.unset_backend()
    return tuple(flags), True
