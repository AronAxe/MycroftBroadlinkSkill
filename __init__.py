# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'AronAxe'

LOGGER = getLogger(__name__)


class MycroftBroadlinkSkill(MycroftSkill):
    def __init__(self):
        super(MycroftBroadlinkSkill, self).__init__(name="MycroftBroadlinkSkill")

    def initialize(self):
        light_on_intent = IntentBuilder("LightOnIntent"). \
            require("LightOnKeyword").build()
        self.register_intent(light_on_intent, self.handle_light_on_intent)

       light_off_intent = IntentBuilder("LightOffIntent"). \
            require("LightOffKeyword").build()
        self.register_intent(light_off_intent,
                             self.handle_light_off_intent)

        device_intent = IntentBuilder("DeviceIntent"). \
            require("DeviceKeyword").build()
        self.register_intent(device_intent,
                             self.handle_device_intent)

    def handle_light_on_intent(self, message):
        self.speak_dialog("light.on")

    def handle_light_off_intent(self, message):
        self.speak_dialog("light.off")

    def handle_hello_world_intent(self, message):
        self.speak_dialog("device")

    def stop(self):
        pass


def create_skill():
    return MycroftBroadlinkSkill()
