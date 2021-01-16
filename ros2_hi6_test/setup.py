import os
from glob import glob
from setuptools import setup
from setuptools import find_packages

package_name = 'ros2_hi6_test'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='hajung',
    author_email='hajung815@gmail.com',
    maintainer='hajung',
    maintainer_email='hajung815@gmail.com',
    description='Interface package test between ros2 and hi6',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'service_client = ros2_hi6_test.service_client:main',
            'status2_service_client = ros2_hi6_test.status2_service_client:main',
            'joystick_jog_test = ros2_hi6_test.joystick_jog_test:main',
            'joint_trajectory_test = ros2_hi6_test.joint_trajectory_test:main',
        ],
    },
)
