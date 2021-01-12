load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
load("@pip//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_binary", "py_library", "py_test")

# Public notice: this file is for internal documentation, testing, and
# reference only. Note that repo maintainers can freely change any part of the
# repository code at any time.
load("@io_bazel_rules_docker//container:container.bzl", "container_image")
load("@io_bazel_rules_docker//python:image.bzl", "py_image")

package(default_visibility = ["//visibility:private"])

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
    visibility = ["//:__pkg__"],
)

# py_test(
#     name = "test",
#     srcs = ["test.py"],
#     deps = [":main"],
# )

py_image(
    name = "docker_py",
    srcs = [
        "__init__.py",
        "app.py",
    ],
    base = "//experimental/python3:python3_root_amd64_debian10",
    main = "app.py",
)

container_image(
    name = "docker_image",
    base = ":app_py",
#    cmd = ["/firestore_middleware/app.py"],
)
