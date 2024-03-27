# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from unittest.mock import patch

from ansible_collections.junipernetworks.junos.plugins.modules import junos_vlans
from ansible_collections.junipernetworks.junos.tests.unit.modules.utils import set_module_args

from .junos_module import TestJunosModule, load_fixture


class TestJunosVlansModule(TestJunosModule):
    module = junos_vlans

    def setUp(self):
        super(TestJunosVlansModule, self).setUp()

        self.mock_lock_configuration = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos.lock_configuration",
        )
        self.lock_configuration = self.mock_lock_configuration.start()

        self.mock_unlock_configuration = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos.unlock_configuration",
        )
        self.unlock_configuration = self.mock_unlock_configuration.start()

        self.mock_load_config = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.vlans.vlans.load_config",
        )
        self.load_config = self.mock_load_config.start()

        self.mock_commit_configuration = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.vlans.vlans.commit_configuration",
        )
        self.mock_commit_configuration = self.mock_commit_configuration.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.facts.vlans.vlans."
            "VlansFacts.get_device_data",
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestJunosVlansModule, self).tearDown()
        self.mock_load_config.stop()
        self.mock_lock_configuration.stop()
        self.mock_unlock_configuration.stop()
        self.mock_commit_configuration.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(
        self,
        commands=None,
        format="text",
        changed=False,
        filename=None,
    ):
        def load_from_file(*args, **kwargs):
            output = load_fixture("junos_vlans_config.cfg")
            return output

        self.execute_show_command.side_effect = load_from_file

    def sort_vlans(self, entry_list):
        entry_list.sort(key=lambda i: i.get("name"))

    def test_junos_vlans_merged(self):
        set_module_args(
            dict(
                config=[dict(name="vlan2", vlan_id=2, l3_interface="irb.12")],
                state="merged",
            ),
        )
        commands = [
            '<nc:vlans xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">'
            "<nc:vlan><nc:name>vlan2</nc:name><nc:vlan-id>2</nc:vlan-id>"
            "<nc:l3-interface>irb.12</nc:l3-interface></nc:vlan></nc:vlans>",
        ]
        result = self.execute_module(changed=True, commands=commands)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_junos_vlans_merged_idempotent(self):
        set_module_args(
            dict(config=[dict(name="vlan1", vlan_id=1)], state="merged"),
        )
        result = self.execute_module(changed=True)
        self.assertEqual(result["before"], result["after"])

    def test_junos_vlans_replaced(self):
        """
        :return:
        """
        set_module_args(
            dict(
                config=[
                    dict(name="vlan1", vlan_id=1, l3_interface="irb.10"),
                    dict(name="vlan2", vlan_id=2),
                ],
                state="replaced",
            ),
        )

        commands = [
            '<nc:vlans xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">'
            '<nc:vlan delete="delete"><nc:name>vlan1</nc:name></nc:vlan>'
            '<nc:vlan delete="delete"><nc:name>vlan2</nc:name></nc:vlan>'
            "<nc:vlan><nc:name>vlan1</nc:name><nc:vlan-id>1</nc:vlan-id>"
            "<nc:l3-interface>irb.10</nc:l3-interface></nc:vlan><nc:vlan>"
            "<nc:name>vlan2</nc:name><nc:vlan-id>2</nc:vlan-id></nc:vlan></nc:vlans>",
        ]
        result = self.execute_module(changed=True, commands=commands)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_junos_vlans_replaced_idempotent(self):
        set_module_args(
            dict(config=[dict(name="vlan1", vlan_id=1)], state="replaced"),
        )
        result = self.execute_module(changed=True)
        self.assertEqual(result["before"], result["after"])

    def test_junos_vlans_overridden(self):
        """
        :return:
        """
        set_module_args(
            dict(
                config=[dict(name="vlan3", vlan_id=3, l3_interface="irb.13")],
                state="overridden",
            ),
        )

        commands = [
            '<nc:vlans xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">'
            '<nc:vlan delete="delete"><nc:name>vlan1</nc:name></nc:vlan>'
            "<nc:vlan><nc:name>vlan3</nc:name><nc:vlan-id>3</nc:vlan-id>"
            "<nc:l3-interface>irb.13</nc:l3-interface></nc:vlan></nc:vlans>",
        ]
        result = self.execute_module(changed=True, commands=commands)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_junos_vlans_overridden_idempotent(self):
        set_module_args(
            dict(config=[dict(name="vlan1", vlan_id=1)], state="overridden"),
        )
        result = self.execute_module(changed=True)
        self.assertEqual(result["before"], result["after"])

    def test_junos_vlans_gathered(self):
        """
        :return:
        """
        set_module_args(dict(state="gathered"))
        result = self.execute_module(changed=False)
        gather_list = [{"name": "vlan1", "vlan_id": 1}]
        self.assertEqual(sorted(gather_list), sorted(result["gathered"]))

    def test_junos_vlans_deleted(self):
        """
        :return:
        """
        set_module_args(dict(config=[dict(name="vlan1")], state="deleted"))

        commands = [
            '<nc:vlans xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">'
            '<nc:vlan delete="delete"><nc:name>vlan1</nc:name></nc:vlan></nc:vlans>',
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_junos_vlans_deleted_01(self):
        """
        :return:
        """
        set_module_args(dict(config=[], state="deleted"))

        commands = [
            '<nc:vlans xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">'
            '<nc:vlan delete="delete"><nc:name>vlan1</nc:name></nc:vlan></nc:vlans>',
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_junos_vlans_rendered(self):
        """
        :return:
        """
        set_module_args(
            dict(
                config=[
                    dict(name="vlan1", vlan_id=1),
                    dict(name="vlan2", vlan_id=2, l3_interface="irb.12"),
                ],
                state="rendered",
            ),
        )
        rendered = (
            '<nc:vlans xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">'
            "<nc:vlan><nc:name>vlan1</nc:name><nc:vlan-id>1</nc:vlan-id></nc:vlan>"
            "<nc:vlan><nc:name>vlan2</nc:name><nc:vlan-id>2</nc:vlan-id>"
            "<nc:l3-interface>irb.12</nc:l3-interface></nc:vlan></nc:vlans>"
        )
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(rendered))

    def test_junos_vlans_parsed(self):
        parsed_str = """
            <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
                <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
                    <version>18.4R1-S2.4</version>
                     <vlans>
                        <vlan>
                            <name>vlan1</name>
                            <vlan-id>1</vlan-id>
                        </vlan>
                        <vlan>
                            <name>vlan2</name>
                            <vlan-id>2</vlan-id>
                            <l3-interface>irb.12</l3-interface>
                        </vlan>
                    </vlans>
                </configuration>
            </rpc-reply>
        """
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_list = [
            {"name": "vlan1", "vlan_id": 1},
            {"l3_interface": "irb.12", "name": "vlan2", "vlan_id": 2},
        ]
        self.sort_vlans(result["parsed"])
        self.sort_vlans(parsed_list)
        self.assertEqual(result["parsed"], parsed_list)
