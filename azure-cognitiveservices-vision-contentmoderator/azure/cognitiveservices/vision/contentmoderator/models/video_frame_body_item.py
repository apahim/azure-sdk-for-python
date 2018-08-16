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


class VideoFrameBodyItem(Model):
    """Schema items of the body.

    All required parameters must be populated in order to send to Azure.

    :param timestamp: Required. Timestamp of the frame.
    :type timestamp: str
    :param frame_image: Required. Content to review.
    :type frame_image: str
    :param reviewer_result_tags:
    :type reviewer_result_tags:
     list[~azure.cognitiveservices.vision.contentmoderator.models.VideoFrameBodyItemReviewerResultTagsItem]
    :param metadata: Optional metadata details.
    :type metadata:
     list[~azure.cognitiveservices.vision.contentmoderator.models.VideoFrameBodyItemMetadataItem]
    """

    _validation = {
        'timestamp': {'required': True},
        'frame_image': {'required': True},
    }

    _attribute_map = {
        'timestamp': {'key': 'Timestamp', 'type': 'str'},
        'frame_image': {'key': 'FrameImage', 'type': 'str'},
        'reviewer_result_tags': {'key': 'ReviewerResultTags', 'type': '[VideoFrameBodyItemReviewerResultTagsItem]'},
        'metadata': {'key': 'Metadata', 'type': '[VideoFrameBodyItemMetadataItem]'},
    }

    def __init__(self, **kwargs):
        super(VideoFrameBodyItem, self).__init__(**kwargs)
        self.timestamp = kwargs.get('timestamp', None)
        self.frame_image = kwargs.get('frame_image', None)
        self.reviewer_result_tags = kwargs.get('reviewer_result_tags', None)
        self.metadata = kwargs.get('metadata', None)