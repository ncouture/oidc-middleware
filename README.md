
# Table of Contents

1.  [Document "Installation"](#org6258f7e)
2.  [Build](#org4ab7c81)
3.  [Developers](#org376bcae)
    1.  [gcloud development environment](#org5c06bbb)
    2.  [pre-commit hooks](#org0edefd1)
    3.  [test coverage](#orgdc6494d)
4.  [Firestore](#org379fcf9)
    1.  [Start the local emulation server](#org1b87132)
    2.  [Custom authentication](#org56aadfc)
5.  [References](#orga49badb)

**[aw]sgi firestore middleware**


<a id="org6258f7e"></a>

# TODO Document "Installation"


<a id="org4ab7c81"></a>

# Build

Install bazel as described on <https://docs.bazel.build/versions/3.7.0/install.html>


<a id="org376bcae"></a>

# Developers


<a id="org5c06bbb"></a>

## gcloud development environment

    # appengine enables the datastore API that's firestore
    gcloud services enable appengine.googleapis.com
    # generate
    gcloud alpha firestore databases create --project=project-id --region=region


<a id="org0edefd1"></a>

## pre-commit hooks

    pip install -r requirements-dev.txt
    pre-commit install


<a id="orgdc6494d"></a>

## test coverage

    interrogate -v .


<a id="org379fcf9"></a>

# Firestore


<a id="org1b87132"></a>

## Start the local emulation server

    export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"


<a id="org56aadfc"></a>

## Custom authentication

Generate a Service Account credentials by visiting

Firebase Console > Project Settings > Service Accounts

-   <https://console.firebase.google.com/project/_/settings/serviceaccounts/adminsdk>)

click on ****GENERATE NEW PRIVATE KEYS****.

You will need it in the firestore/exampletokengenerator/auth.html.


<a id="orga49badb"></a>

# References

-   <https://github.com/tiangolo/fastapi>
-   <https://fastapi.tiangolo.com/advanced/middleware/>
-   <https://fastapi.tiangolo.com/tutorial/security/get-current-user/>
-   <https://koxudaxi.github.io/datamodel-code-generator/>
-   <https://pydantic-docs.helpmanual.io/datamodel_code_generator/#example>
-   <https://developers.google.com/protocol-buffers/>
-   <https://developers.google.com/protocol-buffers/docs/pythontutorial>
