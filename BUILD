pytype_library = py_library

licenses(["notice"])

package(default_visibility = ["//visibility:public"])

load("@bazel_tools//tools/python:toolchain.bzl", "py_runtime_pair")

pytype_library(
    name = "firestore_middleware",
    srcs = glob(
        [
            "*firestore_middleware/*.py",
        ],
        exclude = [
            "*_test.py",
            "**/*_test.py",
        ],
    ),
    srcs_version = "PY3",
    deps = [
        ":app"
    ],
)

# py_library(
#     name = "firestore_middleware",
#     srcs = ["__init__.py"],
#     deps = [],
# )

# package(default_visibility = ["//visibility:private"])

exports_files(glob(["*"]))

#load("//:external.bzl", "")

#register_toolchains("@local_config_python//:my_py_toolchain")
