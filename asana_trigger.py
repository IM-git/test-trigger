import json
import asana
import asana.error
from settings import ASANA_TOKEN

from src import AsanaData
from tools import EnumerationTools


class AsanaTrigger:

    def __init__(self):
        self.client = asana.Client.access_token(accessToken=ASANA_TOKEN)
        self.me = self.client.users.me()

    def asana_user_info(self):
        print(EnumerationTools().enum_cycle(self.me))
        print(f"Hello world! My name is {self.me['name']}!")
        print(f"My email: {self.me['email']}")
        print(f"My photo: {self.me['photo']['image_21x21']}")
        print(f"My workspaces: {self.me['workspaces']}")

    def test_delete_project(self, project_gid=1202896578516952):    # Already deleted
        try:
            self.client.projects.delete_project(project_gid, opt_pretty=True)
            print('Deleted!!')
        except:    # Need to create an exception correctly
            print(f'Not Found: project: Unknown object: {project_gid}')

    def test_create_project(self):
        workspace = AsanaData.WORKSPACE.value
        project = {'name': 'test_im', 'workspace': workspace}
        self.client.projects.create_project(project)

    def test_get_project(self, project_gid=AsanaData.PROJECT_GID.value):
        result = self.client.projects.get_project(project_gid, opt_pretty=True)
        print(json.dumps(result, indent=4, sort_keys=True))

    def test_get_projects(self):
        result = self.client.projects.get_projects(
            workspace=AsanaData.WORKSPACE.value, opt_pretty=True)
        print(result)
        print(EnumerationTools().enum_cycle(result))

    def test_get_tasks(self, project_gid=AsanaData.PROJECT_GID.value):
        result = self.client.projects.tasks(project_gid)
        print(result)
        print(EnumerationTools().enum_cycle(result))

    def test_get_sections(self, project_gid=AsanaData.PROJECT_GID.value):
        result = self.client.sections.get_sections_for_project(project_gid, opt_pretty=True)
        print(result)
        print(EnumerationTools().enum_cycle(result))

    def test_get_section(self, section_gid=AsanaData.SECTION_GID.value):
        result = self.client.sections.get_section(section_gid, opt_pretty=True)
        print(result)
        print(EnumerationTools().enum_cycle(result))

    def test_get_tasks_for_section(self, section_gid=AsanaData.SECTION_GID.value):
        result = self.client.tasks.get_tasks_for_section(section_gid, opt_pretty=True)
        print(result)
        print(EnumerationTools().enum_cycle(result))

    def test_get_task(self, task_gid=AsanaData.TASK_GID.value):
        result = self.client.tasks.get_task(task_gid, opt_pretty=True)
        print(json.dumps(result, indent=4, sort_keys=True))
        print(result['notes'])

    def test_story(self, task_gid=AsanaData.TASK_GID.value):
        """Receive comments from the specified task."""
        result = self.client.stories.get_stories_for_task(task_gid, opt_pretty=True)
        print(result)
        for value in result:
            if value['type'] == 'comment':
                print(value['text'])


if __name__ == '__main__':
    print("### _API ASANA_ ###")
    # AsanaTrigger().asana_user_info()
    # AsanaTrigger().test_delete_project()
    # test_create_project()
    # test_get_project()
    # test_get_projects()
    # AsanaTrigger().test_get_tasks()
    # test_get_sections()
    # test_get_section()
    # test_get_tasks_for_section()
    # test_get_task()
    # test_story()

