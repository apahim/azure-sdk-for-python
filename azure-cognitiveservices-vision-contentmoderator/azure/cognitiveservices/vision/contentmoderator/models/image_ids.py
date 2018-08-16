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


class ImageIds(Model):
    """Image Id properties.

    :param content_source: Source of the content.
    :type content_source: str
    :param content_ids: Id of the contents.
    :type content_ids: list[int]
    :param status: Get Image status.
    :type status:
     ~azure.cognitiveservices.vision.contentmoderator.models.Status
    :param tracking_id: Tracking Id.
    :type tracking_id: str
    """

    _attribute_map = {
        'content_source': {'key': 'ContentSource', 'type': 'str'},
        'content_ids': {'key': 'ContentIds', 'type': '[int]'},
        'status': {'key': 'Status', 'type': 'Status'},
        'tracking_id': {'key': 'TrackingId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ImageIds, self).__init__(**kwargs)
        self.content_source = kwargs.get('content_source', None)
        self.content_ids = kwargs.get('content_ids', None)
        self.status = kwargs.get('status', None)
        self.tracking_id = kwargs.get('tracking_id', None)