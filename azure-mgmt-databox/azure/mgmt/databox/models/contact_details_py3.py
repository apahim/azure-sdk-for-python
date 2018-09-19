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


class ContactDetails(Model):
    """Contact Details.

    All required parameters must be populated in order to send to Azure.

    :param contact_name: Required. Contact name of the person.
    :type contact_name: str
    :param phone: Required. Phone number of the contact person.
    :type phone: str
    :param phone_extension: Phone extension number of the contact person.
    :type phone_extension: str
    :param mobile: Mobile number of the contact person.
    :type mobile: str
    :param email_list: Required. List of Email-ids to be notified about job
     progress.
    :type email_list: list[str]
    :param notification_preference: Notification preference for a job stage.
    :type notification_preference:
     list[~azure.mgmt.databox.models.NotificationPreference]
    """

    _validation = {
        'contact_name': {'required': True},
        'phone': {'required': True},
        'email_list': {'required': True},
    }

    _attribute_map = {
        'contact_name': {'key': 'contactName', 'type': 'str'},
        'phone': {'key': 'phone', 'type': 'str'},
        'phone_extension': {'key': 'phoneExtension', 'type': 'str'},
        'mobile': {'key': 'mobile', 'type': 'str'},
        'email_list': {'key': 'emailList', 'type': '[str]'},
        'notification_preference': {'key': 'notificationPreference', 'type': '[NotificationPreference]'},
    }

    def __init__(self, *, contact_name: str, phone: str, email_list, phone_extension: str=None, mobile: str=None, notification_preference=None, **kwargs) -> None:
        super(ContactDetails, self).__init__(**kwargs)
        self.contact_name = contact_name
        self.phone = phone
        self.phone_extension = phone_extension
        self.mobile = mobile
        self.email_list = email_list
        self.notification_preference = notification_preference
