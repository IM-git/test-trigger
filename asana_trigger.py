import json
import asana

from settings import ASANA_TOKEN

from src import AsanaData
from tools import EnumerationTools


class AsanaTrigger:
    """
    Here are collected the main methods of working with the Asana API.
    """

    def __init__(self):
        self.client = asana.Client.access_token(accessToken=ASANA_TOKEN)
        self.me = self.client.users.me()

    def asana_user_info(self):
        print(EnumerationTools().enum_cycle(self.me))
        print(f"Hello world! My name is {self.me['name']}!")
        print(f"My email: {self.me['email']}")
        print(f"My photo: {self.me['photo']['image_21x21']}")
        print(f"My workspaces: {self.me['workspaces']}")

    def delete_specified_project(self, project_gid=1202896578516952):
        """Deletes the specified project."""
        try:
            self.client.projects.delete_project(project_gid, opt_pretty=True)
            print('Deleted!!')
        except:    # Need to create an exception correctly
            print(f'Not Found: project: Unknown object: {project_gid}')

    def create_new_project(self):
        """Create new project, without tasks."""
        workspace = AsanaData.WORKSPACE.value
        project = {'name': 'test_im', 'workspace': workspace}
        self.client.projects.create_project(project)

    def get_a_project(self, project_gid=AsanaData.PROJECT_GID.value):
        """Returns the complete project record for a single project."""
        result = self.client.projects.get_project(project_gid,
                                                  opt_pretty=True)
        print(json.dumps(result, indent=4, sort_keys=True))

    def get_multiple_projects(self):
        """Returns the compact project records for some filtered
        set of projects."""
        result = self.client.projects.get_projects(
            workspace=AsanaData.WORKSPACE.value, opt_pretty=True)
        print(EnumerationTools().enum_cycle(result))

    def get_sections_in_project(self,
                                project_gid=AsanaData.PROJECT_GID.value):
        """Returns the compact records for all sections
        in the specified project."""
        result = self.client.sections.get_sections_for_project(
            project_gid, opt_pretty=True)
        print(EnumerationTools().enum_cycle(result))

    def get_a_section(self, section_gid=AsanaData.SECTION_GID.value):
        """Returns the complete record for a single section."""
        result = self.client.sections.get_section(section_gid,
                                                  opt_pretty=True)
        print(EnumerationTools().enum_cycle(result))

    def get_multiple_tasks(self, project_gid=AsanaData.PROJECT_GID.value):
        """Returns the compact task records for some filtered set of tasks."""
        result = self.client.projects.tasks(project_gid)
        print(EnumerationTools().enum_cycle(result))

    def get_tasks_from_section(self, section_gid=AsanaData.SECTION_GID.value):
        """Board view only: Returns the compact section records for all tasks
        within the given section."""
        result = self.client.tasks.get_tasks_for_section(section_gid,
                                                         opt_pretty=True)
        list_with_values = EnumerationTools().enum_cycle(result)
        print(json.dumps(list_with_values, indent=4, sort_keys=True))

    def get_a_task(self, task_gid=AsanaData.TASK_GID.value):
        """Returns the complete task record for a single task."""
        result = self.client.tasks.get_task(task_gid, opt_pretty=True)
        print(json.dumps(result, indent=4, sort_keys=True))
        return result

    def get_description_from_task(self):
        print(self.get_a_task()['notes'])

    def get_stories_from_task(self, task_gid=AsanaData.TASK_GID.value):
        """Returns the compact records for all stories on the task."""
        result = self.client.stories.get_stories_for_task(task_gid,
                                                          opt_pretty=True)
        list_with_values = EnumerationTools().enum_cycle(result)
        print(json.dumps(list_with_values, indent=4, sort_keys=True))
        return list_with_values

    def get_a_story(self, story_gid=AsanaData.STORY_GID.value):
        """Returns the full record for a single story."""
        result = self.client.stories.get_story(story_gid, opt_pretty=True)
        print(json.dumps(result, indent=4, sort_keys=True))

    def get_comments_from_task(self):
        """Receive comments from the specified task."""
        for value in self.get_stories_from_task():
            if value['type'] == 'comment':
                print(value['text'])


if __name__ == '__main__':
    asana_trigger = AsanaTrigger()
    print("### _API ASANA_ ###")
    asana_trigger.asana_user_info()
    # asana_trigger.delete_specified_project()
    asana_trigger.create_new_project()
    asana_trigger.get_a_project()
    asana_trigger.get_multiple_projects()
    asana_trigger.get_sections_in_project()
    asana_trigger.get_a_section()
    asana_trigger.get_multiple_tasks()
    asana_trigger.get_tasks_from_section()
    asana_trigger.get_a_task()
    asana_trigger.get_description_from_task()
    asana_trigger.get_stories_from_task()
    asana_trigger.get_a_story()
    asana_trigger.get_comments_from_task()

