load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
load("@pip//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_binary", "py_library", "py_test")

package(default_visibility = ["//visibility:public"])

py_binary(
    name = "app",
    srcs = ["app.py"],
    # deps = [
    #     "requests"
    # ],
)

py_library(
    name = "firestore_middleware",
    srcs = [
        "__init__.py",
        "app.py"
    ],
    deps = [],
)

# py_test(
#     name = "test",
#     srcs = ["test.py"],
#     deps = [":main"],
# )
