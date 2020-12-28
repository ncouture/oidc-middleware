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


load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "io_bazel_rules_docker",
    sha256 = "1698624e878b0607052ae6131aa216d45ebb63871ec497f26c67455b34119c80",
    strip_prefix = "rules_docker-0.15.0",
    urls = ["https://github.com/bazelbuild/rules_docker/releases/download/v0.15.0/rules_docker-v0.15.0.tar.gz"],
)

# load("@io_bazel_rules_docker//toolchains/docker:toolchain.bzl",
#     docker_toolchain_configure="toolchain_configure"
# )

# docker_toolchain_configure(
#   name = "docker_config",
# #   # OPTIONAL: Path to a directory which has a custom docker client config.json.
# #   # See https://docs.docker.com/engine/reference/commandline/cli/#configuration-files
# #   # for more details.
# #   client_config="<enter absolute path to your docker config directory here>",
# #   # OPTIONAL: Path to the docker binary.
# #   # Should be set explicitly for remote execution.
# #   docker_path="<enter absolute path to the docker binary (in the remote exec env) here>",
# #   # OPTIONAL: Path to the gzip binary.
# #   gzip_path="<enter absolute path to the gzip binary (in the remote exec env) here>",
# #   # OPTIONAL: Bazel target for the gzip tool.
# #   gzip_target="<enter absolute path (i.e., must start with repo name @...//:...) to an executable gzip target>",
# #   # OPTIONAL: Path to the xz binary.
# #   # Should be set explicitly for remote execution.
# #   xz_path="<enter absolute path to the xz binary (in the remote exec env) here>",
# #   # OPTIONAL: List of additional flags to pass to the docker command.
#   docker_flags = [
#     "--tls",
#     "--log-level=info",
#   ],

# # )
# # End of OPTIONAL segment.
load(
    "@io_bazel_rules_docker//repositories:repositories.bzl",
    container_repositories = "repositories",
)
container_repositories()

load("@io_bazel_rules_docker//repositories:deps.bzl", container_deps = "deps")

container_deps()

load(
    "@io_bazel_rules_docker//container:container.bzl",
    "container_pull",
)

container_pull(
  name = "distroless_python3",
  registry = "gcr.io",
  repository = "/GoogleContainerTools/distroless/",
  # 'tag' is also supported, but digest is encouraged for reproducibility.
  digest = "sha256:4865496ea24dba83025abc1d6a742e2b1dd71594",
)

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
http_archive(
    name = "rules_python",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.1.0/rules_python-0.1.0.tar.gz",
    sha256 = "b6d46438523a3ec0f3cead544190ee13223a52f6a6765a29eae7b7cc24cc83a0",
)
load("@rules_python//python:pip.bzl", "pip_repositories")
pip_repositories()

register_toolchains("//firestore_middleware:all")
