gavika.administrators
=========

An Ansible role to create administrative users.

Requirements
------------
None

Role Variables
--------------
```yml
administrators_names: ['admin01', 'admin02']
administrators_keys:
  - username: admin01
    key: /path/to/id_rsa_pub_admin01
```

Dependencies
------------

None

Example Playbook
----------------
```yml
  - hosts: servers  
    vars:
      - administrators_names: ['admin01', 'admin02']
      - administrators_keys:
          - username: admin01
            key: /path/to/id_rsa_pub_admin01
    roles:
       - role: gavika.administrators
```

License
-------

Apache

Author Information
------------------
Sudheer Satyanarayana

* Gavika: https://www.gavika.com
* Blog: https://www.techchorus.net
* Twitter: https://www.twitter.com/bngsudheer
* Github: https://github.com/bngsudheer
