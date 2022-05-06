#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceYuntaskPublishResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceYuntaskPublishResponse, self).__init__()
        self._success = None

    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceYuntaskPublishResponse, self).parse_response_content(response_content)
        if 'success' in response:
            self.success = response['success']
