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


class Review(Model):
    """The Review object.

    :param review_id: Id of the review.
    :type review_id: str
    :param sub_team: Name of the subteam.
    :type sub_team: str
    :param status: The status string (<Pending, Complete>).
    :type status: str
    :param reviewer_result_tags: Array of KeyValue with Reviewer set Tags.
    :type reviewer_result_tags:
     list[~azure.cognitiveservices.vision.contentmoderator.models.KeyValuePair]
    :param created_by: The reviewer name.
    :type created_by: str
    :param metadata: Array of KeyValue.
    :type metadata:
     list[~azure.cognitiveservices.vision.contentmoderator.models.KeyValuePair]
    :param type: The type of content.
    :type type: str
    :param content: The content value.
    :type content: str
    :param content_id: Id of the content.
    :type content_id: str
    :param callback_endpoint: The callback endpoint.
    :type callback_endpoint: str
    """

    _attribute_map = {
        'review_id': {'key': 'ReviewId', 'type': 'str'},
        'sub_team': {'key': 'SubTeam', 'type': 'str'},
        'status': {'key': 'Status', 'type': 'str'},
        'reviewer_result_tags': {'key': 'ReviewerResultTags', 'type': '[KeyValuePair]'},
        'created_by': {'key': 'CreatedBy', 'type': 'str'},
        'metadata': {'key': 'Metadata', 'type': '[KeyValuePair]'},
        'type': {'key': 'Type', 'type': 'str'},
        'content': {'key': 'Content', 'type': 'str'},
        'content_id': {'key': 'ContentId', 'type': 'str'},
        'callback_endpoint': {'key': 'CallbackEndpoint', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Review, self).__init__(**kwargs)
        self.review_id = kwargs.get('review_id', None)
        self.sub_team = kwargs.get('sub_team', None)
        self.status = kwargs.get('status', None)
        self.reviewer_result_tags = kwargs.get('reviewer_result_tags', None)
        self.created_by = kwargs.get('created_by', None)
        self.metadata = kwargs.get('metadata', None)
        self.type = kwargs.get('type', None)
        self.content = kwargs.get('content', None)
        self.content_id = kwargs.get('content_id', None)
        self.callback_endpoint = kwargs.get('callback_endpoint', None)