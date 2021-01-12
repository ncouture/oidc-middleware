pytype_library = py_library

licenses(["notice"])

package(default_visibility = ["//visibility:private"])

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

exports_files(glob(["*"]))
