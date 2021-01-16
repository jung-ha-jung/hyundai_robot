import os
from glob import glob
from setuptools import setup
from setuptools import find_packages

package_name = 'ros2_hi6'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include all launch files
        (os.path.join('share', package_name), glob('launch/*')),
        # Include all source files
        (os.path.join('lib', package_name), glob('src/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='hajung',
    author_email='hajung815@gmail.com',
    maintainer='hajung',
    maintainer_email='hajung815@gmail.com',
    description='Interface package between ros2 and hi6',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'joint_state_publisher = ros2_hi6.joint_state_publisher:main',
            'joystick_jog = ros2_hi6.joystick_jog:main',
            'service_server = ros2_hi6.service_server:main',
            'joint_trajectory = ros2_hi6.joint_trajectory:main',
        ],
    },
)
