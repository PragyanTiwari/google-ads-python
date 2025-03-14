# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import annotations


import proto  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v18.enums",
    marshal="google.ads.googleads.v18",
    manifest={
        "AdCustomizerPlaceholderFieldEnum",
    },
)


class AdCustomizerPlaceholderFieldEnum(proto.Message):
    r"""Values for Ad Customizer placeholder fields."""

    class AdCustomizerPlaceholderField(proto.Enum):
        r"""Possible values for Ad Customizers placeholder fields.

        Values:
            UNSPECIFIED (0):
                Not specified.
            UNKNOWN (1):
                Used for return value only. Represents value
                unknown in this version.
            INTEGER (2):
                Data Type: INT64. Integer value to be
                inserted.
            PRICE (3):
                Data Type: STRING. Price value to be
                inserted.
            DATE (4):
                Data Type: DATE_TIME. Date value to be inserted.
            STRING (5):
                Data Type: STRING. String value to be
                inserted.
        """

        UNSPECIFIED = 0
        UNKNOWN = 1
        INTEGER = 2
        PRICE = 3
        DATE = 4
        STRING = 5


__all__ = tuple(sorted(__protobuf__.manifest))
