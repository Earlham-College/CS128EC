from setuptools import setup
OPTIONS = {
 'iconfile':'iconTestApp.icns',
}
setup(
 app=["testApp.py"],
 options = {'py2app': OPTIONS},
 setup_requires=["py2app"],
)