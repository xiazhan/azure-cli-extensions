# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_connectedmachine.generated._client_factory import cf_machine
    connectedmachine_machine = CliCommandType(
        operations_tmpl='azext_connectedmachine.vendored_sdks.connectedmachine.operations._machine_operations#MachineOp'
        'erations.{}',
        client_factory=cf_machine)
    with self.command_group('connectedmachine', connectedmachine_machine, client_factory=cf_machine) as g:
        g.custom_command('list', 'connectedmachine_list')
        g.custom_show_command('show', 'connectedmachine_show')
        g.custom_command('delete', 'connectedmachine_delete', confirmation=True)

    from azext_connectedmachine.generated._client_factory import cf_machine_extension
    connectedmachine_machine_extension = CliCommandType(
        operations_tmpl='azext_connectedmachine.vendored_sdks.connectedmachine.operations._machine_extension_operations'
        '#MachineExtensionOperations.{}',
        client_factory=cf_machine_extension)
    with self.command_group('connectedmachine extension', connectedmachine_machine_extension,
                            client_factory=cf_machine_extension, is_experimental=True) as g:
        g.custom_command('list', 'connectedmachine_extension_list')
        g.custom_show_command('show', 'connectedmachine_extension_show')
        g.custom_command('create', 'connectedmachine_extension_create', supports_no_wait=True)
        g.custom_command('update', 'connectedmachine_extension_update', supports_no_wait=True)
        g.custom_command('delete', 'connectedmachine_extension_delete', supports_no_wait=True, confirmation=True)
        g.custom_wait_command('wait', 'connectedmachine_extension_show')
