
# Table of Contents

1.  [Developers](#org8517c97)
    1.  [gcloud development environment](#org650dee8)
    2.  [pre-commit hooks](#org69edeb8)
    3.  [test coverage](#org8084094)
2.  [Firestore](#orgb636a2c)
    1.  [Start the local emulation server](#orgc7386d6)
    2.  [Custom authentication](#orge82715a)
3.  [References](#org214ff19)

**[aw]sgi firestore middleware**


<a id="org8517c97"></a>

# Developers


<a id="org650dee8"></a>

## gcloud development environment

    # appengine enables the datastore API that's firestore
    gcloud services enable appengine.googleapis.com
    # generate
    gcloud alpha firestore databases create --project=project-id --region=region


<a id="org69edeb8"></a>

## pre-commit hooks

    pip install -r requirements-dev.txt
    pre-commit install


<a id="org8084094"></a>

## test coverage

    interrogate -v .


<a id="orgb636a2c"></a>

# Firestore


<a id="orgc7386d6"></a>

## Start the local emulation server

    export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"


<a id="orge82715a"></a>

## Custom authentication

Generate a Service Account credentials by visiting

Firebase Console > Project Settings > Service Accounts

-   <https://console.firebase.google.com/project/_/settings/serviceaccounts/adminsdk>)

click on ****GENERATE NEW PRIVATE KEYS****.

You will need it in the firestore/exampletokengenerator/auth.html.


<a id="org214ff19"></a>

# References

-   <https://github.com/tiangolo/fastapi>
-   <https://fastapi.tiangolo.com/advanced/middleware/>
-   <https://fastapi.tiangolo.com/tutorial/security/get-current-user/>
-   <https://koxudaxi.github.io/datamodel-code-generator/>
-   <https://pydantic-docs.helpmanual.io/datamodel_code_generator/#example>
-   <https://developers.google.com/protocol-buffers/>
-   <https://developers.google.com/protocol-buffers/docs/pythontutorial>
