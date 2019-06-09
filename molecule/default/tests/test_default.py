import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

def test_admin01_file_exists(host):
    f = host.file('/etc/sudoers.d/admin01')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

    assert f.is_file
    assert f.contains('admin01 ALL=(ALL) NOPASSWD: ALL')

def test_admin01_user_exists(host):
    user = host.user("admin01")
    assert user.name == 'admin01'
