import Dezero

# =============================================================================
# step23.pyからstep32.pyまではsimple_coreを利用
is_simple_core = True  # True
# =============================================================================

if is_simple_core:
    from Dezero.dezero.core_simple import Variable
    from Dezero.dezero.core_simple import Function
    from Dezero.dezero.core_simple import using_config
    from Dezero.dezero.core_simple import no_grad
    from Dezero.dezero.core_simple import as_array
    from Dezero.dezero.core_simple import as_variable
    from Dezero.dezero.core_simple import setup_variable

else:
    from Dezero.dezero.core import Variable
    from Dezero.dezero.core import Parameter
    from Dezero.dezero.core import using_config
    from Dezero.dezero.core import no_grad
    from Dezero.dezero.core import test_mode
    from Dezero.dezero.core import as_array
    from Dezero.dezero.core import as_variable
    from Dezero.dezero.core import setup_variable
    from Dezero.dezero.core import Config
    from Dezero.dezero.layers import Layer
    from Dezero.dezero.models import Model
    from Dezero.dezero.datasets import Dataset
    from Dezero.dezero.dataloaders import DataLoader
    from Dezero.dezero.dataloaders import SeqDataLoader

    import Dezero.dezero.datasets
    import Dezero.dezero.dataloaders
    import Dezero.dezero.optimizers
    import Dezero.dezero.functions
    import Dezero.dezero.functions_conv
    import Dezero.dezero.layers
    import Dezero.dezero.utils
    import Dezero.dezero.cuda
    import Dezero.dezero.transforms

setup_variable()
__version__ = '0.0.13'