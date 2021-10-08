#!/usr/bin/python

import yaml
import os

with open("{0}/{1}/kustomization{2}".format(
        os.environ["INPUT_DEFAULTFOLDER"],
        os.environ["INPUT_ENVIRONMENT"],
        os.environ["INPUT_DEFAULTFILEEXTENSION"])) as f: 
    kustomize_yaml = yaml.safe_load(f.read())

with open("{0}/{1}/kustomization{2}".format(
        os.environ["INPUT_DEFAULTFOLDER"],
        os.environ["INPUT_ENVIRONMENT"],
        os.environ["INPUT_DEFAULTFILEEXTENSION"]), 'w') as f: 
    for image in kustomize_yaml['images']:
        if image['name'] == os.environ["INPUT_IMAGENAME"]:
            image['newTag'] = os.environ["INPUT_NEWIMAGETAG"]
    yaml.dump(kustomize_yaml, f, sort_keys=False)