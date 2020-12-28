workspace(name = "firestore_middleware")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_python",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.1.0/rules_python-0.1.0.tar.gz",
    sha256 = "b6d46438523a3ec0f3cead544190ee13223a52f6a6765a29eae7b7cc24cc83a0",
)

load("@rules_python//python:pip.bzl", "pip_install")

pip_install(
    # (Optional) You can provide extra parameters to pip.
    # Here, make pip output verbose (this is usable with `quiet = False`).
    extra_pip_args = ["-v"],

    # (Optional) You can exclude custom elements in the data section of the generated BUILD files for pip packages.
    # Exclude directories with spaces in their names in this example (avoids build errors if there are such directories).
    #pip_data_exclude = ["**/* */**"],

    # (Optional) You can provide a python_interpreter (path) or a python_interpreter_target (a Bazel target, that
    # acts as an executable). The latter can be anything that could be used as Python interpreter. E.g.:
    # 1. Python interpreter that you compile in the build file (as above in @python_interpreter).
    # 2. Pre-compiled python interpreter included with http_archive
    # 3. Wrapper script, like in the autodetecting python toolchain.
    #python_interpreter_target = "@python_interpreter//:python_bin",

    # (Optional) You can set quiet to False if you want to see pip output.
    quiet = False,

    # Uses the default repository name "pip"
    requirements = "//:requirements.txt",
)

# You could optionally use an in-build, compiled python interpreter as a toolchain,
# and also use it to execute pip.
#
# Special logic for building python interpreter with OpenSSL from homebrew.
# See https://devguide.python.org/setup/#macos-and-os-x
#_py_configure = """
#if [[ "$OSTYPE" == "darwin"* ]]; then
#    ./configure --prefix=$(pwd)/bazel_install --with-openssl=$(brew --prefix openssl)
#else
#    ./configure --prefix=$(pwd)/bazel_install
#fi
#"""
#
# NOTE: you need to have the SSL headers installed to build with openssl support (and use HTTPS).
# E.g. on Ubuntu: `sudo apt install libssl-dev`
#http_archive(
#    name = "python_interpreter",
#    build_file_content = """
#exports_files(["python_bin"])
#filegroup(
#    name = "files",
#    srcs = glob(["bazel_install/**"], exclude = ["**/* *"]),
#    visibility = ["//visibility:public"],
#)
#""",
#    patch_cmds = [
#        "mkdir $(pwd)/bazel_install",
#        _py_configure,
#        "make",
#        "make install",
#        "ln -s bazel_install/bin/python3 python_bin",
#    ],
#    sha256 = "dfab5ec723c218082fe3d5d7ae17ecbdebffa9a1aea4d64aa3a2ecdd2e795864",
#    strip_prefix = "Python-3.8.3",
#    urls = ["https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tar.xz"],
#)

# Optional:
# Register the toolchain with the same python interpreter we used for pip in pip_install().
#register_toolchains("//:my_py_toolchain")
# End of in-build Python interpreter setup.

# pytype_library = py_library


