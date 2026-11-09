import re
from urllib import request
import tomli
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def m_package_name(self, requirement):
        return re.split(r"[<>=!~;\[ ]", requirement, maxsplit=1)[0]

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")
        data = tomli.loads(content)
        project = data["project"]

        authors = [author["name"] for author in project.get("authors", [])]
        dependencies = [
            self.m_package_name(dependency)
            for dependency in project.get("dependencies", [])
        ]
        dev_dependencies = [
            self.m_package_name(dependency)
            for dependency in data.get("dependency-groups", {}).get("dev", [])
        ]

        return Project(
            project["name"],
            project["description"],
            project.get("license"),
            authors,
            dependencies,
            dev_dependencies
        )