# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ImageTemplateDistributor(Model):
    """Generic distribution object.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: ImageTemplateManagedImageDistributor,
    ImageTemplateSharedImageDistributor

    All required parameters must be populated in order to send to Azure.

    :param run_output_name: Required. The name to be used for the associated
     RunOutput.
    :type run_output_name: str
    :param tags: Tags for the images
    :type tags: dict[str, str]
    :param type: Required. Constant filled by server.
    :type type: str
    """

    _validation = {
        'run_output_name': {'required': True, 'pattern': r'^[A-Za-z0-9-_]{1,64}$'},
        'type': {'required': True},
    }

    _attribute_map = {
        'run_output_name': {'key': 'runOutputName', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'type': {'key': 'type', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'managedImage': 'ImageTemplateManagedImageDistributor', 'sharedImage': 'ImageTemplateSharedImageDistributor'}
    }

    def __init__(self, *, run_output_name: str, tags=None, **kwargs) -> None:
        super(ImageTemplateDistributor, self).__init__(**kwargs)
        self.run_output_name = run_output_name
        self.tags = tags
        self.type = None
