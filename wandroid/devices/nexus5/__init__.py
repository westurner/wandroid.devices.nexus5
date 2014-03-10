#!/usr/bin/env python
# encoding: utf-8
from __future__ import print_function
"""
n5
"""

import wandroid.adbw as adb
#import adbsh  # adb, adbsu

class Nexus5(object):
    device_name = 'hammerhead'
    LOCKED = 0
    UNLOCKED = 1
    UNTAMPERED = 0
    TAMPERED = 1
    bootloader_conf = dict(
        blockdev = '/dev/block/platform/msm_sdcc.1/by-name/misc',
        lock_offset = 16400,
        tamper_offset = 16404,)
    # THANKS!

    @staticmethod
    def field_test_debug():
        adb.adbsh('am start -n com.lge.SprintHiddenMenu/.sprintspec.Debug')

    @staticmethod
    def field_test_config():
        """
        .. note:: requires MSL code to edit
        """
        adb.adbsh('am start -n com.lge.SprintHiddenMenu/.sprintspec.Data')

    @staticmethod
    def get_lock_status():
        p = adb.adbsu(
            'dd ibs=1 count=1 skip={lock_offset} obs=1 if={blockdev}'.
            format(**Nexus5.bootloader_conf))
        value = p.stdout[:2]
        states = {'\x001': 'Locked', '\x011': 'Unlocked' }
        output = states.get(value, "Unknown")
        print(output)

    @staticmethod
    def set_lock_status(value=1):
        """
        0 = locked
        1 = unlocked
        """
        cmd = ((r"echo -ne '\x0{value}' | "
            r"su -c dd count=1 seek={lock_offset} obs=1 of={blockdev}").
            format(value=value, **Nexus5.bootloader_conf))
        p = adb.adbsu(cmd)
        print(p.stdout)

    @staticmethod
    def get_tamper_status():
        p = adb.adbsu(
            'dd ibs=1 count=1 skip={tamper_offset} obs=1 if={blockdev}'.
            format(**Nexus5.bootloader_conf))
        value = p.stdout[:2]
        states = {'\x001': 'Untampered', '\x011': 'Tampered' }
        output = states.get(value, "Unknown")
        print(output)

    @staticmethod
    def set_tamper_status(value=1):
        """
        0 = not tampered
        1 = tampered
        """
        cmd = ((r"echo -ne '\x0{value}' | "
            r"su -c dd count=1 seek={tamper_offset} obs=1 of={blockdev}").
            format(value=value, **Nexus5.bootloader_conf))
        p = adb.adbsu(cmd)
        print(p.stdout)

    @staticmethod
    def main(*args):
        import logging
        import optparse
        import sys

        prs = optparse.OptionParser(usage="%prog : args")

        prs.add_option('--get-lock-status',
                        dest='get_lock_status',
                        action='store_true',
                        help='Get the status of the bootloader lock')
        prs.add_option('--set-lock-status',
                        dest='set_lock_status',
                        action='store',
                        type='int',
                        help='Set the status of the bootloader lock')

        prs.add_option('--get-tamper-status',
                        dest='get_tamper_status',
                        action='store_true',
                        help='Get the status of the tamper flag')
        prs.add_option('--set-tamper-status',
                        dest='set_tamper_status',
                        action='store',
                        type='int',
                        help='Set the status of the tamper flag')

        prs.add_option('--field-test-debug',
                       dest='field_test_debug',
                       action='store_true',
                       help='Launch field test mode (debug)')

        prs.add_option('--field-test-config',
                       dest='field_test_config',
                       action='store_true',
                       help='Launch field test mode (config)')

        prs.add_option('-v', '--verbose',
                        dest='verbose',
                        action='store_true',)
        prs.add_option('-q', '--quiet',
                        dest='quiet',
                        action='store_true',)
        prs.add_option('-t', '--test',
                        dest='run_tests',
                        action='store_true',)

        args = list(args) if args else sys.argv
        (opts, args) = prs.parse_args(args)

        if not opts.quiet:
            logging.basicConfig()

            if opts.verbose:
                logging.getLogger().setLevel(logging.DEBUG)

        if opts.run_tests:
            import sys
            sys.argv = [sys.argv[0]] + args
            import unittest
            exit(unittest.main())

        if opts.get_lock_status:
            Nexus5.get_lock_status()

        if opts.set_lock_status is not None:
            Nexus5.set_lock_status(opts.set_lock_status)

        if opts.get_tamper_status:
            Nexus5.get_tamper_status()

        if opts.set_tamper_status is not None:
            Nexus5.set_tamper_status(opts.set_tamper_status)

        if opts.field_test_debug:
            Nexus5.field_test_debug()

        if opts.field_test_config:
            Nexus5.field_test_config()

        return 0


import unittest
class Test_nexus5(unittest.TestCase):
    def test_nexus5_main(self):
        retval = Nexus5.main('-h')
        self.assertEqual(retval, 0)


if __name__ == "__main__":
    import sys
    sys.exit(Nexus5.main())
