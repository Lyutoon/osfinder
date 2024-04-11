# osfinder
A small tool to find &lt;module 'os' (frozen)> import path in any given package to bypass some sandboxes or solve CTF challenges.

## Usage
```
python3 finder.py --package=pandas --target=os --maxl=5 --maxn=100
```

- package: the target package in which we want to find os.
- target: target module, default to be os.
- maxl: maximum length of import chain.
- maxn: maximum number of import chains.

## Examples
run with `python3 finder.py --package=xxxx --target=os --maxl=5 --maxn=100`

pandas:
```
pandas.util._validators.np.ctypeslib.os
pandas.util._validators.np._pytesttester.os
pandas.util._validators.np.__config__.os
pandas.util._tester.os
pandas.util._print_versions.os
pandas.util._print_versions.platform.os
pandas.util._exceptions.os
pandas.util._exceptions.inspect.os
pandas.util._exceptions.inspect.linecache.os
pandas.util._exceptions.contextlib.os
pandas.util._decorators.inspect.os
pandas.util._decorators.inspect.linecache.os
pandas.tseries.frequencies.np.ctypeslib.os
pandas.tseries.frequencies.np._pytesttester.os
pandas.tseries.frequencies.np.__config__.os
pandas.pandas.util._tester.os
pandas.pandas.util._print_versions.os
pandas.pandas.util._print_versions.platform.os
pandas.pandas.util._exceptions.os
pandas.pandas.util._exceptions.inspect.os
pandas.pandas.util._exceptions.contextlib.os
pandas.pandas.util._decorators.inspect.os
pandas.pandas.pandas.util._tester.os
pandas.pandas.pandas.util._print_versions.os
pandas.pandas.pandas.util._exceptions.os
pandas.pandas.pandas.pandas.compat.os
pandas.pandas.pandas.pandas._testing.os
pandas.pandas.pandas.io.stata.os
pandas.pandas.pandas.io.pytables.os
pandas.pandas.pandas.io.parquet.os
pandas.pandas.pandas.io.common.os
pandas.pandas.pandas.core.config_init.os
pandas.pandas.pandas.compat.os
pandas.pandas.pandas.compat.platform.os
pandas.pandas.pandas._testing.os
pandas.pandas.pandas._testing.contexts.os
pandas.pandas.io.stata.os
pandas.pandas.io.pytables.os
pandas.pandas.io.parquet.os
pandas.pandas.io.excel._base.os
pandas.pandas.io.common.os
pandas.pandas.io.common.zipfile.os
pandas.pandas.io.common.tarfile.os
pandas.pandas.io.common.gzip.os
pandas.pandas.core.config_init.os
pandas.pandas.core.common.inspect.os
pandas.pandas.core.common.contextlib.os
pandas.pandas.core.apply.inspect.os
pandas.pandas.compat.os
pandas.pandas.compat.platform.os
pandas.pandas.compat.pickle_compat.contextlib.os
pandas.pandas.compat.pandas.compat.os
pandas.pandas.compat.pandas._testing.os
pandas.pandas.compat.compressors.lzma.os
pandas.pandas.compat.compressors.bz2.os
pandas.pandas.compat._constants.sysconfig.os
pandas.pandas.compat._constants.platform.os
pandas.pandas._typing.np.ctypeslib.os
pandas.pandas._typing.np._pytesttester.os
pandas.pandas._typing.np.__config__.os
pandas.pandas._testing.os
pandas.pandas._testing.pd.compat.os
pandas.pandas._testing.pd._testing.os
pandas.pandas._testing.pa.util.os
pandas.pandas._testing.pa.lib.os
pandas.pandas._testing.pa.ipc.os
pandas.pandas._testing.pa.hdfs.os
pandas.pandas._testing.pa.filesystem.os
pandas.pandas._testing.pa._platform.os
pandas.pandas._testing.pa._lib.os
pandas.pandas._testing.np.ctypeslib.os
pandas.pandas._testing.np._pytesttester.os
pandas.pandas._testing.np.__config__.os
pandas.pandas._testing.contexts.os
pandas.pandas._testing.contexts.uuid.os
pandas.pandas._testing._warnings.inspect.os
pandas.pandas._testing._io.zipfile.os
pandas.pandas._testing._io.uuid.os
pandas.pandas._testing._io.tarfile.os
pandas.pandas._testing._io.pathlib.os
pandas.pandas._testing._io.gzip.os
pandas.pandas._libs.pandas.compat.os
pandas.pandas._libs.pandas._testing.os
pandas.pandas._config.localization.subprocess.os
pandas.pandas._config.localization.platform.os
pandas.io.stata.os
pandas.io.stata.np.ctypeslib.os
pandas.io.stata.np._pytesttester.os
pandas.io.stata.np.__config__.os
pandas.io.sql.np.ctypeslib.os
pandas.io.sql.np._pytesttester.os
pandas.io.sql.np.__config__.os
pandas.io.sql.com.inspect.os
pandas.io.sql.com.contextlib.os
pandas.io.pytables.os
pandas.io.pytables.timezones.pytz.os
pandas.io.pytables.np.ctypeslib.os
pandas.io.pytables.np._pytesttester.os
pandas.io.pytables.np.__config__.os
pandas.io.pytables.com.inspect.os
pandas.io.pytables.com.contextlib.os
```

numpy:
```
numpy.testing.extbuild.os
numpy.testing.extbuild.sysconfig.os
numpy.testing.extbuild.pathlib.os
numpy.testing.extbuild.pathlib.posixpath.os
numpy.testing.extbuild.pathlib.ntpath.os
numpy.testing.extbuild.pathlib.fnmatch.os
numpy.testing._private.utils.os
numpy.testing._private.utils.shutil.os
numpy.testing._private.utils.platform.os
numpy.testing._private.utils.contextlib.os
numpy.testing._private.nosetester.os
numpy.testing._private.extbuild.os
numpy.testing._private.extbuild.sysconfig.os
numpy.testing._private.extbuild.pathlib.os
numpy.rec.sb.shape_base.overrides.os
numpy.rec.sb.overrides.os
numpy.rec.sb.np.ctypeslib.os
numpy.rec.sb.np._pytesttester.os
numpy.rec.sb.np.__config__.os
numpy.rec.sb.multiarray.overrides.os
numpy.rec.sb.fromnumeric.overrides.os
numpy.rec.sb.arrayprint.contextlib.os
numpy.rec.sb._ufunc_config.contextlib.os
numpy.random.mtrand.np.ctypeslib.os
numpy.random.mtrand.np._pytesttester.os
numpy.random.mtrand.np.__config__.os
numpy.random.bit_generator.np.ctypeslib.os
numpy.random.bit_generator.np._pytesttester.os
numpy.random.bit_generator.np.__config__.os
numpy.random._sfc64.np.ctypeslib.os
numpy.random._sfc64.np._pytesttester.os
numpy.random._sfc64.np.__config__.os
numpy.random._philox.np.ctypeslib.os
numpy.random._philox.np._pytesttester.os
numpy.random._philox.np.__config__.os
numpy.random._pcg64.np.ctypeslib.os
numpy.random._pcg64.np._pytesttester.os
numpy.random._pcg64.np.__config__.os
numpy.random._mt19937.np.ctypeslib.os
numpy.random._mt19937.np._pytesttester.os
numpy.random._mt19937.np.__config__.os
numpy.random._generator.np.ctypeslib.os
numpy.random._generator.np._pytesttester.os
numpy.random._generator.np.__config__.os
numpy.random._common.np.ctypeslib.os
numpy.random._common.np._pytesttester.os
numpy.random._common.np.__config__.os
numpy.random._bounded_integers.np.ctypeslib.os
numpy.random._bounded_integers.np._pytesttester.os
numpy.random._bounded_integers.np.__config__.os
numpy.polynomial.polyutils.np.ctypeslib.os
numpy.polynomial.polyutils.np._pytesttester.os
numpy.polynomial.polyutils.np.__config__.os
numpy.polynomial.polynomial.np.ctypeslib.os
numpy.polynomial.polynomial.np._pytesttester.os
numpy.polynomial.polynomial.np.__config__.os
numpy.polynomial.legendre.np.ctypeslib.os
numpy.polynomial.legendre.np._pytesttester.os
numpy.polynomial.legendre.np.__config__.os
numpy.polynomial.laguerre.np.ctypeslib.os
numpy.polynomial.laguerre.np._pytesttester.os
numpy.polynomial.laguerre.np.__config__.os
numpy.polynomial.hermite_e.np.ctypeslib.os
numpy.polynomial.hermite_e.np._pytesttester.os
numpy.polynomial.hermite_e.np.__config__.os
numpy.polynomial.hermite.np.ctypeslib.os
numpy.polynomial.hermite.np._pytesttester.os
numpy.polynomial.hermite.np.__config__.os
numpy.polynomial.chebyshev.np.ctypeslib.os
numpy.polynomial.chebyshev.np._pytesttester.os
numpy.polynomial.chebyshev.np.__config__.os
numpy.polynomial._polybase.os
numpy.polynomial._polybase.np.ctypeslib.os
numpy.polynomial._polybase.np._pytesttester.os
numpy.polynomial._polybase.np.__config__.os
numpy.ma.extras.np.ctypeslib.os
numpy.ma.extras.np._pytesttester.os
numpy.ma.extras.np.__config__.os
numpy.ma.extras.ma.inspect.os
numpy.ma.core.np.ctypeslib.os
numpy.ma.core.np._pytesttester.os
numpy.ma.core.np.__config__.os
numpy.ma.core.mu.overrides.os
numpy.ma.core.inspect.os
numpy.ma.core.inspect.linecache.os
numpy.linalg.linalg.overrides.os
numpy.lib.utils.os
numpy.lib.utils.np.ctypeslib.os
numpy.lib.utils.np._pytesttester.os
numpy.lib.utils.np.__config__.os
numpy.lib.ufunclike.nx.overrides.os
numpy.lib.type_check.overrides.os
numpy.lib.type_check._nx.overrides.os
numpy.lib.twodim_base.overrides.os
numpy.lib.stride_tricks.np.ctypeslib.os
numpy.lib.stride_tricks.np._pytesttester.os
numpy.lib.stride_tricks.np.__config__.os
numpy.lib.shape_base.overrides.os
numpy.lib.shape_base._nx.overrides.os
numpy.lib.scimath.nx.overrides.os
numpy.lib.polynomial.overrides.os
```

matplotlib:
```
matplotlib.os
matplotlib.transforms.np.testing.extbuild.os
matplotlib.transforms.np.polynomial._polybase.os
matplotlib.transforms.np.lib.utils.os
matplotlib.transforms.np.lib.npyio.os
matplotlib.transforms.np.lib._datasource.os
matplotlib.transforms.np.ctypeslib.os
matplotlib.transforms.np.compat.py3k.os
matplotlib.transforms.np.char.overrides.os
matplotlib.transforms.np._pytesttester.os
matplotlib.transforms.np.__config__.os
matplotlib.transforms._api.deprecation.inspect.os
matplotlib.transforms._api.deprecation.contextlib.os
matplotlib.ticker.np.testing.extbuild.os
matplotlib.ticker.np.polynomial._polybase.os
matplotlib.ticker.np.lib.utils.os
matplotlib.ticker.np.lib.npyio.os
matplotlib.ticker.np.lib._datasource.os
matplotlib.ticker.np.ctypeslib.os
matplotlib.ticker.np.compat.py3k.os
matplotlib.ticker.np.char.overrides.os
matplotlib.ticker.np._pytesttester.os
matplotlib.ticker.np.__config__.os
matplotlib.ticker.mtransforms.np.ctypeslib.os
matplotlib.ticker.mtransforms.np._pytesttester.os
matplotlib.ticker.mtransforms.np.__config__.os
matplotlib.ticker.mpl.os
matplotlib.ticker.mpl.ticker.mpl.os
matplotlib.ticker.mpl.ticker.logging.os
matplotlib.ticker.mpl.ticker.cbook.os
matplotlib.ticker.mpl.tempfile._shutil.os
matplotlib.ticker.mpl.subprocess.os
matplotlib.ticker.mpl.subprocess.contextlib.os
matplotlib.ticker.mpl.shutil.os
matplotlib.ticker.mpl.shutil.fnmatch.os
matplotlib.ticker.mpl.scale.mpl.os
matplotlib.ticker.mpl.scale.inspect.os
matplotlib.ticker.mpl.rcsetup.os
matplotlib.ticker.mpl.rcsetup.cbook.os
matplotlib.ticker.mpl.path.mpl.os
matplotlib.ticker.mpl.numpy.ctypeslib.os
matplotlib.ticker.mpl.numpy._pytesttester.os
matplotlib.ticker.mpl.numpy.__config__.os
matplotlib.ticker.mpl.logging.os
matplotlib.ticker.mpl.inspect.os
matplotlib.ticker.mpl.inspect.linecache.os
matplotlib.ticker.mpl.contextlib.os
matplotlib.ticker.mpl.colors.mpl.os
matplotlib.ticker.mpl.colors.inspect.os
matplotlib.ticker.mpl.colors.cbook.os
matplotlib.ticker.mpl.colors.Image.os
matplotlib.ticker.mpl.cm.mpl.os
matplotlib.ticker.mpl.cm.cbook.os
matplotlib.ticker.mpl.cbook.os
matplotlib.ticker.mpl.cbook.subprocess.os
matplotlib.ticker.mpl.cbook.shlex.os
matplotlib.ticker.mpl.cbook.matplotlib.os
matplotlib.ticker.mpl.cbook.gzip.os
matplotlib.ticker.mpl.cbook.contextlib.os
matplotlib.ticker.mpl._docstring.inspect.os
matplotlib.ticker.logging.os
matplotlib.ticker.logging.traceback.linecache.os
matplotlib.ticker.cbook.os
matplotlib.ticker.cbook.traceback.linecache.os
matplotlib.ticker.cbook.subprocess.os
matplotlib.ticker.cbook.subprocess.contextlib.os
matplotlib.ticker.cbook.shlex.os
matplotlib.ticker.cbook.np.ctypeslib.os
matplotlib.ticker.cbook.np._pytesttester.os
matplotlib.ticker.cbook.np.__config__.os
matplotlib.ticker.cbook.matplotlib.os
matplotlib.ticker.cbook.matplotlib.subprocess.os
matplotlib.ticker.cbook.matplotlib.shutil.os
matplotlib.ticker.cbook.matplotlib.rcsetup.os
matplotlib.ticker.cbook.matplotlib.logging.os
matplotlib.ticker.cbook.matplotlib.inspect.os
matplotlib.ticker.cbook.matplotlib.contextlib.os
matplotlib.ticker.cbook.matplotlib.cbook.os
matplotlib.ticker.cbook.gzip.os
matplotlib.ticker.cbook.contextlib.os
matplotlib.ticker._api.deprecation.inspect.os
matplotlib.ticker._api.deprecation.contextlib.os
matplotlib.tempfile._shutil.os
matplotlib.tempfile._shutil.fnmatch.os
matplotlib.tempfile._shutil.fnmatch.posixpath.os
matplotlib.tempfile._os.path.os
matplotlib.tempfile._os.path.genericpath.os
matplotlib.subprocess.os
matplotlib.subprocess.threading._os.path.os
matplotlib.subprocess.contextlib.os
matplotlib.shutil.os
matplotlib.shutil.fnmatch.os
matplotlib.shutil.fnmatch.posixpath.os
matplotlib.shutil.fnmatch.posixpath.genericpath.os
matplotlib.scale.np.testing.extbuild.os
matplotlib.scale.np.polynomial._polybase.os
matplotlib.scale.np.lib.utils.os
matplotlib.scale.np.lib.npyio.os
matplotlib.scale.np.lib._datasource.os
matplotlib.scale.np.ctypeslib.os
matplotlib.scale.np.compat.py3k.os
```

plotly:
```
plotly.utils.Image.os
plotly.utils.Image.tempfile._shutil.os
plotly.utils.Image.module.os
plotly.utils.Image.module.module.os
plotly.utils.Image.module.logging.os
plotly.utils.Image.logging.os
plotly.utils.Image.logging.handlers.os
plotly.utils.Image.logging.config.os
plotly.tools.os
plotly.tools.ipython_core_display.os
plotly.tools.ipython_core_display.mimetypes.os
plotly.tools.ipython_core_display.mimetypes.posixpath.os
plotly.tools.ipython_core_display.display_functions.os
plotly.offline.offline.os
plotly.offline.offline.tools.os
plotly.offline.offline.tools.ipython_core_display.os
plotly.offline.offline.pkgutil.os
```
