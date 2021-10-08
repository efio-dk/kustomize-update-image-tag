# kustomize-update-image-tag
GitHub Action to update Kustomize image tag, in different environments, by name.

## Inputs

## `imageName`

**Required** The name of the image to update.

## `newImageTag`

**Required** The new tag to update to.

## `environment`

**Required** The name of the environment to update. Default `"dev"`.

## `defaultFolder`

**Required** The default folder to find kustomize environment folders.  Default `"./kustomize"`.

## `defaultFileExtension`

**Required** The default file extension for kustomize files.  Default `".yaml"`.

## Example usage

```yaml
name: Update Kustomize Image Tag
on:
  push:
    branches-ignore:
      - '**'
    tags:
      - 'v*.*.*'
jobs:
  update-image-tag:
  runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: efio-dk/kustomize-update-image-tag@v1
        with:
          imageName: 'test-image'
          newImageTag: '1234'
          environment: 'dev' # (optional, default is "dev")
          defaultFolder: './kustomize' # (optional, default is "./kustomize")
          defaultFileExtension: '.yaml' # (optional, default is ".yaml")
```